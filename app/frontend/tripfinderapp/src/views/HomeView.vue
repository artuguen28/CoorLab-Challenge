<template>
  <div class="home">
    <div class="sidebar">
      <img class="CB-logo" alt="CB Viagens logo" src="../assets/logo.png" />
      <SidebarButton
        class="sidebarButton"
        @click="handleButtonClick"
        :disabled="isDisabled"
        buttonMsg="Calculadora de Viagem"
      />
    </div>
    <div class="main">
      <TripFinderComponent v-if="showTripForm" />
      <WelcomeComponent v-else />
    </div>
  </div>
</template>

<script>
import WelcomeComponent from "@/components/WelcomeComponent.vue";
import SidebarButton from "@/components/SidebarButton.vue";
import TripFinderComponent from "@/components/TripFinderComponent.vue";

export default {
  name: "HomeView",
  components: {
    WelcomeComponent,
    SidebarButton,
    TripFinderComponent,
  },
  data() {
    return {
      showTripForm: true,
      isDisabled: false,
    };
  },
  methods: {
    handleButtonClick() {
      this.showTripForm = true;
    },
  },
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: row;
}
.CB-logo {
  margin: 10px;
  width: 5cm;
}
.main {
  flex: 5;
  background-color: white;
  height: 100%;
}

.sidebar {
  flex: 1;
  background-color: #2c3e50;
  height: 100%;
}
</style>
