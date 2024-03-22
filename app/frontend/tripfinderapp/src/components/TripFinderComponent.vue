<template>
  <div class="main">
    <div class="tripCalc">
      <div class="topBar">
        <img alt="Calculator Icon" src="../assets/bus.png" />
        <h2>Calculadora de Viagem</h2>
      </div>
      <div class="tripMain">
        <div class="tripForm">
          <div class="tripFormTitle">
            <img alt="Money Hand" src="../assets/handMoney.png" />
            <h3>Calcule o Valor da Viagem</h3>
          </div>
          <div class="inputBox">
            <p>Destino</p>
            <select class="citySelect" v-model="selectedCity">
              <option value="" disabled selected>Selecione o destino</option>
              <option v-for="city in cityNames" :key="city" :value="city">
                {{ city }}
              </option>
            </select>
          </div>
          <div class="inputBox">
            <p>Data</p>
            <date-picker
              v-model="tripDate"
              valueType="date"
              class="date-picker"
            ></date-picker>
          </div>
          <button class="searchButton" @click="getTripResults">Buscar</button>
        </div>
        <div class="result">
          <p v-if="showResults">Nenhum dado selecionado</p>
          <ResultGrid
            v-else
            :fastestInfo="fastestInfo"
            :cheapestInfo="cheapestInfo"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ResultGrid from "./ResultGrid.vue";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";

export default {
  name: "TripFinderComponent",
  components: { DatePicker, ResultGrid },
  data() {
    return {
      selectedCity: "",
      cityNames: [],
      tripDate: null,
      showResults: false,
      fastestInfo: {},
      cheapestInfo: {},
    };
  },
  methods: {
    getCityNames() {
      const path = "http://127.0.0.1:3000/cities";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data["city_names"]);
          this.cityNames = res.data["city_names"];
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getTripResults() {
      const path = "http://127.0.0.1:3000/trips";
      const requestData = {
        cityName: this.selectedCity,
        date: String(this.tripDate),
      };
      axios
        .post(path, requestData)
        .then((res) => {
          this.cheapestInfo = res.data["trips"]["cheapest"];
          this.fastestInfo = res.data["trips"]["fastest"];
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getCityNames();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main {
  padding-right: 10%;
  padding-left: 10%;
  height: 100%;
  padding-bottom: 20%;
  padding-top: 10%;
}
.tripCalc {
  background-color: white;
  border-color: gray;
  border-width: 1px;
  border-style: solid;
  border-radius: 4px;
  box-shadow: 1px 2px 8px #888888;
  height: 70%;
}
.topBar {
  display: grid;
  text-align: center;
  align-items: center;
  justify-content: start;
  background-color: #2c3e50;
  color: white;
  border-top-right-radius: 3px;
  border-top-left-radius: 3px;
}
.topBar img {
  grid-column: 1;
  margin: 10px;
  filter: invert(1);
}
.topBar h2 {
  font-size: 20px;
  grid-column: 2;
}
.tripMain {
  display: grid;
  height: auto;
}
.tripForm {
  grid-column: 1;
  margin: 5%;
  background-color: rgb(233, 233, 233);
  border-radius: 3px;
  padding: 5%;
  height: 100%;
}
.tripFormTitle {
  align-items: center;
  display: grid;
}
.tripFormTitle h3 {
  text-align: start;
  grid-column: 2;
  font-size: 13px;
}
.tripFormTitle img {
  margin: 7px;
  grid-column: 1;
  height: 30px;
}
.tripForm h1 {
  font-size: 15px;
}
.inputBox {
  text-align: start;
  margin: 10px;
}
.citySelect {
  width: 100%;
  height: 30px;
  border-radius: 5px;
}
.inputBox p {
  font-size: 15px;
}
.date-picker {
  border-radius: 5px;
  width: 100%;
  height: 30px;
}
.searchButton {
  background-color: aqua;
  border-radius: 5px;
  border-width: 1px;
  border-color: aqua;
  width: 70%;
  height: 25px;
  margin-top: 10%;
}
.result {
  text-align: center;
  align-items: center;
  grid-column: 2;
}
.result h1 {
  font-size: 15px;
}
</style>
