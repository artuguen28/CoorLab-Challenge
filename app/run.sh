#!/bin/bash
sudo apt install gnome-terminal

# Run Flask backend
echo "Starting Flask backend..."
cd backend
pip install -r requirements.txt
cd api
#python3 main.py
gnome-terminal -- bash -c "python3 main.py; exec bash"
cd ../..

# Run Vue.js frontend
echo "Starting Vue.js frontend..."
cd frontend/tripfinderapp
gnome-terminal -- bash -c "npm install && npm run serve; exec bash"
#npm install
#npm run serve