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
          <button class="searchButton" @click="checkInput">Buscar</button>
        </div>
        <div class="result">
          <ResultGrid
            v-if="showResults"
            :fastestInfo="fastestInfo"
            :cheapestInfo="cheapestInfo"
            @clear-data="clearFetchedData"
          />
          <p v-else>Nenhum dado selecionado</p>
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
    checkInput() {
      if (this.selectedCity === "" || this.tripDate === null) {
        window.alert("Insira todos os dados necessários!");
      } else {
        this.getTripResults();
      }
    },
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
      this.showResults = true;
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
    clearFetchedData() {
      this.fastestInfo = {};
      this.cheapestInfo = {};
      this.showResults = false;
    },
  },
  created() {
    this.getCityNames();
  },
};
</script>

<style scoped>
.main {
  padding-right: 10%;
  padding-left: 10%;
  padding-bottom: 20%;
  padding-top: 10%;
  height: 100%;
}
.tripCalc {
  background-color: white;
  border-color: gray;
  border-width: 1px;
  border-style: solid;
  border-radius: 4px;
  box-shadow: 1px 2px 8px #888888;
  height: 100%;
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
  display: flex;
}
.tripForm {
  flex: 1;
  background-color: rgb(233, 233, 233);
  border-radius: 5px;
  margin-right: 3%;
  margin-left: 3%;
  margin-top: 5%;
  margin-bottom: 5%;
  padding-right: 3%;
  padding-left: 3%;
  padding-top: 10%;
  padding-bottom: 10%;
  height: 100%;
}
.tripFormTitle {
  align-items: center;
  display: grid;
}
.tripFormTitle h3 {
  text-align: start;
  grid-column: 2;
  font-size: 12px;
}
.tripFormTitle img {
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
  flex: 2;
  text-align: center;
  align-items: center;
  justify-content: center;
}
.result p {
  align-items: center;
}
</style>
