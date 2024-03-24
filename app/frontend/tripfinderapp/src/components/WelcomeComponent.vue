<template>
  <div class="welcome">
    <h1>Bem-vindo ao CB Viagens!</h1>
    <h3>Encontre aqui as melhores opções para sua próxima viagem!</h3>
    <hr class="solid" />
    <h3>
      Para iniciar sua pesquisa, selecione "Calculadora de Viagem" no menu ao
      lado!
    </h3>
  </div>
</template>

<script>
export default {
  name: "WelcomeComponent",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.welcome {
  justify-content: center;
  align-items: center;
  text-align: start;
  margin-left: 5%;
  margin-right: 5%;
  color: #2c3e50;
}

hr.solid {
  border-top: 1px solid #bbb;
}
</style>
