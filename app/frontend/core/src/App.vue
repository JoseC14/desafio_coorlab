<template>
  <MainPage/>
</template>

<script>
import MainPage from './components/MainPage.vue'
export default {
  name: 'App',
  components: {
    MainPage
  }
}
</script>

<style>
body{
  margin: 0;
  padding:0;
  background-color: rgb(92, 132, 158);
  overflow-y:hidden;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
