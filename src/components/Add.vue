<template>
  <main add-cat="add-cat">
    <p>To submit a request to Toronto Cat Rescue...</p>
  </main>
</template>

<script>

//this is to export variables here, to be passed up to parent files
export default {
  name: 'Add',
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
main{
    background-color: pink;
}
</style>
