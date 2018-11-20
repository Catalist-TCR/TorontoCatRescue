<template>
  <div id="header" class="sticky">
    <img id="logo-image" alt="Catalist" src="../../images/TCR-Logo.svg">
    <a href="/add">New Request</a>
    <a href="/waitlist">Waitlist</a>
  </div>
</template>

<script>

export default {
  name: 'header',
  // props: {
  // }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
}
#logo-image{
    max-width: 100px;
}
#header{
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: space-around;
    margin: 0 25%;
    height: 60px;
    border-bottom: solid #A7A7A7 2px;
    padding-bottom: 10px;
    z-index: 1;
    grid-column: 1 / span 3;
    position: sticky;
    top: 0;
    background-color: white;
}

#header a{
  text-decoration: none;
  color: black;
}

</style>
