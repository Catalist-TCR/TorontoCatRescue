<template>
  <div id="app">
    <Header v-if="main()" />
    <router-view>
        <Welcome />
    </router-view>
  </div>
</template>

<script>
import Welcome from './components/Welcome.vue';
import Add from './components/Add.vue';
import Header from './components/Header.vue';

const routes = [
  { path: '/login', component: Welcome },
  { path: '/addcat', component: Add },
]

export default {
  name: 'app',
  methods: {
    main: function () {
      return this.$route.path.length != 1 && this.$route.path.indexOf('login') == -1;
    }
  },
  components: {
    Welcome,
    Header
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
  margin: 0 10% 0 10%;
}
</style>
