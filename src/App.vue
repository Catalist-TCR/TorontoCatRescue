<template>
  <div id="app">
    <Header v-if="main()" />
    <router-view>
        <Welcome />
    </router-view>
    <Footer />
  </div>
</template>

<script>
import Welcome from './components/Welcome.vue';
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Add from './components/Add.vue';
import Waitlist from './components/Waitlist.vue';

const routes = [
  { path: '/login', component: Welcome },
  { path: '/addcat', component: Add },
  { path: '/waitlist', component: Waitlist },
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
    Header,
    Waitlist,
    Footer,
  }
}

</script>

<style>
#app {
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  grid-template-rows: auto auto 50px;
  grid-gap: 10px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0 5%;
}

main{
  grid-column: 2 ;
  grid-row: 2 ;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

input[type="text"]{
  border-radius: 5px;
  border:1px solid #cccccc
}

button[type="submit"]{
  align-self: center;
  color: white;
  background-color: #34A798;
  border-radius: 5px;
  width: 50%;
  max-width: 150px;
  height: 40px;
  border: none;
}

button[type="submit"]:hover{
    color: #34A798;
    background-color: white;
    border: solid 2px #34A798;
    cursor: pointer;
}
</style>
