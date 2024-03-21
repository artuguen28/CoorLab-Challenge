<template>
  <div :class="['div-button', { disabled: disabled }]" @click="handleClick">
    <img alt="Calculator Icon" src="../assets/calculator.png" />
    <p>{{ buttonMsg }}</p>
  </div>
</template>

<script>
export default {
  name: "SidebarButton",
  props: {
    buttonMsg: String,
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    handleClick() {
      if (!this.disabled) {
        this.$emit("click");
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.div-button {
  display: grid;
  background-color: #2c3e50;
  border-top-color: aliceblue;
  border-bottom-color: aliceblue;
  justify-content: start;
  align-items: center;
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  user-select: none;
}

.div-button.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

img {
  margin-left: 5px;
  margin-right: 5px;
  height: 30px;
  width: 30px;
  grid-column: 1;
}

p {
  grid-column: 2;
  font-size: 15px;
  font-weight: bold;
  color: white;
}
</style>
