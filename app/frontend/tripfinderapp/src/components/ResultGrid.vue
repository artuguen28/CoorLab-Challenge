<template>
  <div class="resultPanel">
    <h3>
      Estas são as melhores alternativas de viagem para a data selecionada:
    </h3>
    <div class="resultGrid">
      <div class="fastestTrip">
        <div class="fastestTripImage">
          <img alt="Money Hand" src="../assets/handMoney.png" />
        </div>
        <div class="fastestTripInfo">
          <h3>{{ fastestInfo.name }}</h3>
          <p>Leito: {{ fastestInfo.bed }}</p>
          <p>Tempo Estimado: {{ fastestInfo.duration }}h</p>
        </div>
        <div class="fastestTripPrice">
          <h3>Preço</h3>
          <p>R$ {{ fastestInfo.price_confort }}</p>
        </div>
      </div>
      <div class="cheapestTrip">
        <div class="cheapestTripImage">
          <img alt="Money Hand" src="../assets/time.png" />
        </div>
        <div class="cheapestTripInfo">
          <h3>{{ cheapestInfo.name }}</h3>
          <p>Poltrona: {{ cheapestInfo.seat }}</p>
          <p>Tempo Estimado: {{ cheapestInfo.duration }}h</p>
        </div>
        <div class="cheapestTripPrice">
          <h3>Preço</h3>
          <p>R$ {{ cheapestInfo.price_econ }}</p>
        </div>
      </div>
    </div>
    <button class="clearButton" @click="clearFetchedData">Limpar</button>
  </div>
</template>

<script>
export default {
  name: "ResultGrid",
  props: {
    fastestInfo: Object,
    cheapestInfo: Object,
  },
  methods: {
    clearFetchedData() {
      this.$emit("clear-data");
    },
  },
};
</script>

<style scoped>
.resultPanel {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-right: 4%;
  padding-top: 10%;
}
.resultPanel h3 {
  font-size: 18px;
  margin-bottom: 20px;
}
.resultGrid {
  display: flex;
  flex-direction: column;
  width: 90%;
}
.fastestTrip,
.cheapestTrip {
  align-items: center;
  display: flex;
  flex-direction: row;
  border-radius: 5px;
  overflow: hidden;
  margin-top: 5px;
  margin-bottom: 5px;
  margin-left: 3%;
  height: 90px;
}
.cheapestTripImage,
.fastestTripImage {
  height: 100%;
  background-color: #03a8b5;
}
.cheapestTripInfo,
.fastestTripInfo {
  flex: 2;
  height: 100%;
  text-align: start;
  padding-left: 3%;
  padding-top: 5%;
  padding-right: 3%;
  background-color: rgb(233, 233, 233);
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}
.cheapestTripPrice,
.fastestTripPrice {
  flex: 1;
  height: 100%;
  border-radius: 10px;
  margin-left: 3%;
  padding-left: 3%;
  padding-top: 10%;
  text-align: start;
  padding-bottom: 5%;
  background-color: rgb(233, 233, 233);
  width: 100%;
}
.cheapestTripPrice h3,
.fastestTripPrice h3,
.cheapestTripInfo h3,
.fastestTripInfo h3 {
  font-size: 15px;
  margin-top: 0px;
  margin-bottom: 0px;
}
.cheapestTripPrice p,
.fastestTripPrice p,
.cheapestTripInfo p,
.fastestTripInfo p {
  font-size: 12px;
  margin-top: 0px;
  margin-bottom: 0px;
}
.fastestTrip img {
  height: 60px;
  margin: 10px;
}
.cheapestTrip img {
  height: 40px;
  margin: 20px;
}
.clearButton {
  background-color: #fda300;
  border-radius: 5px;
  border-width: 1px;
  border-color: transparent;
  width: 50%;
  height: 25px;
  margin-top: 10%;
  margin-bottom: 10%;
}
</style>
