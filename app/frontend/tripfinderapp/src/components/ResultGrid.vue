<template>
  <div class="resultPanel">
    <h3>
      Estas são as melhores alternativas de viagem para a data selecionada:
    </h3>
    <div class="resultGrid">
      <div class="fastestTrip">
        <img alt="Money Hand" src="../assets/handMoney.png" />
        <div class="fastestTripInfo">
          <h3>Fastest: {{ fastestInfo.name }}</h3>
          <p>Leito: {{ fastestInfo.bed }}</p>
          <p>Tempo Estimado: {{ fastestInfo.duration }}h</p>
        </div>
        <div class="fastestTripPrice">
          <h3>Preço</h3>
          <p>R$ {{ fastestInfo.price_confort }}</p>
        </div>
      </div>
      <div class="cheapestTrip">
        <img alt="Money Hand" src="../assets/handMoney.png" />
        <div class="cheapestTripInfo">
          <h3>Cheapest: {{ cheapestInfo.name }}</h3>
          <p>Poltrona: {{ cheapestInfo.seat }}</p>
          <p>Tempo Estimado: {{ cheapestInfo.duration }}h</p>
        </div>
        <div class="cheapestTripPrice">
          <h3>Preço</h3>
          <p>R$ {{ cheapestInfo.price_econ }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultGrid",
  props: {
    fastestInfo: Object,
    cheapestInfo: Object,
  },
};
</script>

<style scoped>
.resultPanel {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.resultPanel h3 {
  font-size: 20px;
  margin-bottom: 20px;
}
.resultGrid {
  display: flex;
  justify-content: space-around;
  width: 100%;
}
.fastestTrip,
.cheapestTrip {
  flex-basis: 45%;
  border: 1px solid gray;
  border-radius: 5px;
  overflow: hidden;
}
.fastestTripInfo h3 .cheapestTripInfo h3 {
  font-size: 5px;
}
.fastestTrip p .cheapestTrip p {
  font-size: 10px;
}
.fastestTrip img,
.cheapestTrip img {
  background-color: aquamarine;
  height: 70px;
  padding: 10%;
  border-radius: 10px;
}
.fastestTripInfo,
.fastestTripPrice,
.cheapestTripInfo,
.cheapestTripPrice {
  padding: 10px; /* Added padding for spacing */
}
</style>
