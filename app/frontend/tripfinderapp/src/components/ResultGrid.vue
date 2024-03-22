<template>
  <div class="resultPanel">
    <h3>
      Estas são as melhores alternativas de viagem para a data selecionada:
    </h3>
    <div class="resultGrid">
      <div class="fastestTrip">
        <img alt="Money Hand" src="../assets/handMoney.png" />
        <div class="fastestTripInfo">
          <h3>Info Fastest</h3>
        </div>
        <div class="fastestTripPrice">
          <h3>Price Fastest</h3>
        </div>
      </div>
      <div class="cheapestTrip">
        <img alt="Money Hand" src="../assets/handMoney.png" />
        <div class="cheapestTripInfo">
          <h3>Info Cheapest</h3>
        </div>
        <div class="cheapestTripPrice">
          <h3>Info Fastest</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultGrid",
  props: {
    fastestInfo: JSON,
    chapestInfo: JSON,
  },
};
</script>

<style scoped>
.resultPanel {
  align-items: center;
}
.resultPanel h3 {
  font-size: 20px;
}
.resultGrid {
  box-shadow: 1px 2px 5px #888888;
  margin-right: 5%;
  margin-left: 5%;
  border-radius: 5px;
}
.fastestTrip {
  display: grid;
  align-items: center;
  justify-content: center;
  border-width: 1px;
  border-style: solid;
  border-color: gray;
  border-top-right-radius: 5px;
  border-top-left-radius: 5px;
}
.fastestTrip img {
  background-color: aquamarine;
  height: 70px;
  grid-column: 1;
  padding: 10%;
  margin-bottom: 0px;
  border-radius: 10px;
}
.fastestTripInfo {
  background-color: blueviolet;
  grid-column: 2;
  margin-right: 5%;
  margin-left: 5%;
  padding-right: 5%;
  padding-left: 5%;
}
.fastestTripPrice {
  background-color: blueviolet;
  grid-column: 3;
  margin-right: 5%;
  margin-left: 5%;
}
.cheapestTrip {
  display: grid;
  align-items: center;
  justify-content: center;
  border-width: 1px;
  border-style: solid;
  border-color: gray;
  border-bottom-right-radius: 5px;
  border-bottom-left-radius: 5px;
}
.cheapestTrip img {
  background-color: aquamarine;
  height: 70px;
  grid-column: 1;
  padding: 10%;
  border-radius: 10px;
}
.cheapestTripInfo {
  grid-column: 2;
}
.cheapestTripPrice {
  grid-column: 3;
}
</style>
