<template>
  <div id="app">
    <img alt="Catalist" src="../images/TCR-Logo.svg">
    <router-view>
        <Welcome />
    </router-view>
  </div>
</template>

<script>
import Welcome from './components/Welcome.vue';
import Add from './components/Add.vue';

const routes = [
  { path: '/login', component: Welcome },
  { path: '/addcat', component: Add },
]

export default {
  name: 'app',
  components: {
    Welcome
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#app img {
  width: 50%;
  max-width: 300px;
}
</style>
