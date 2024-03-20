from flask import Flask, jsonify, request
from flask_cors import CORS
import json


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins':'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})


with open('app/data.json') as f:
    database = json.load(f)

    # Breif data cleaning
    for item in database['transport']:

        # Remove the 'h' sufix and converting to integer
        item['duration'] = int(item['duration'][:-1])

        # Remove the 'R$ ' prefix and converting to float
        item['price_econ'] = float(item['price_econ'][2:])
        item['price_confort'] = float(item['price_confort'][2:])

        # Fixing city names
        if item['name'] == "S\u00e3o Paulo":
            item['name'] = "São Paulo"

        if item['name'] == "Rio de Janiero":
            item['name'] = "Rio de Janeiro"

    print("Database loaded!")


@app.route('/cities', methods=['GET'])
def get_city_names() -> json:

    city_names = []
    for trip in database['transport']:
        if trip['city'] not in city_names:
            city_names.append(trip['city'])

    return jsonify({
        'city_names': city_names,  
        'status': 'success' 
    })

    


@app.route('/trips', methods=['POST'])
def get_fastest_cheapest_trip() -> json:

    # Extracting parameters from the request body
    body = request.json
    city_name = body.get('cityName')

    # The date of the trip is provided but won't be used within the scope of the present application
    date = body.get('date')

    # Checking if both parameters are present
    if city_name is None or date is None:
        return jsonify({'error': 'Both parameters are required'}), 400
    
    # Getting the fastest trip by the its name
    def get_fastest(data: list, city_name: str) -> dict:

        cities_by_name = []
        for trip in data['transport']:
            if trip['city'] == city_name:

                cities_by_name.append(trip)

        # Returing the trip with lowest duration
        return min(cities_by_name, key=lambda x: x['duration'])
    
    # Getting the cheapest trip by the its name
    def get_cheapest(data: list, city_name: str) -> dict:

        cities_by_price_econ = []
        for trip in data['transport']:
            if trip['city'] == city_name:

                cities_by_price_econ.append(trip)

        # Returing the trip with lowest price
        return min(cities_by_price_econ, key=lambda x: x['price_econ'])
        
    fastest_trip = get_fastest(database, city_name)
    cheapest_trip = get_cheapest(database, city_name)

    
    return jsonify({
        'trips': {
            'fastest': fastest_trip,
            'cheapest': cheapest_trip,
        },  
        'status': 'success' 
    })

if __name__ == "__main__":
    app.run(debug=True, port=3000)

