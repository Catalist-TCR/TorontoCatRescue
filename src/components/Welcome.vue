<template>
  <div class="welcome">
    <img alt="Catalist" src="../../images/TCR-Logo.svg">
    <h1>Welcome to Catalist</h1>
      <Login />
  </div>
</template>

<script>
import Login from './Login.vue';

//this is to export variables here, to be passed up to parent files
export default {
  name: 'Welcome',
  props: {
    msg: String
  },
  components: {
    Login
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.welcome img {
  width: 50%;
  max-width: 300px;
}
</style>
