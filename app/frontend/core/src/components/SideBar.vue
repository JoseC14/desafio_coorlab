

<template>
    <aside class="sidebar">
      <img class="logo" src="../assets/logo.png">        
      <h3 id="calc_viagem">Calculadora de Viagens</h3>
    </aside>
</template>

<script>
export default {
  name: 'SideBar'
}
</script>

<style scoped>
  aside{
    height: 100vh;
  }
  .sidebar{
    background-color: rgb(62, 62, 62);
    float:left;
    color:white;
    
    padding:10px
  }

  .logo{
    margin-top: 20px;
    height: 3vw;
    width: 15vw;
  }

  #calc_viagem{
    cursor: pointer;
    padding: 15px;
    border-radius:15px;
  }

  #calc_viagem:hover{
    background-color: white;
    color:black
  }
</style>
