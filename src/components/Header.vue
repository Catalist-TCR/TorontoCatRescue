<template>
  <div id="header" class="sticky">
    <img id="logo-image" alt="Catalist" src="../../images/TCR-Logo.svg">
        <ul id="navigation">
            <li>New Request</li>
            <li>Waitlist</li>
        </ul>
  </div>
</template>

<script>

// document.addEventListener("DOMContentLoaded", function(){
//     if (document.getElementsByClassName("welcome")){
//         document.getElementById('header').style.display = 'none';
//     }
// });

export default {
  name: 'Header',
  props: {

  }
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
    justify content: center;
    align-items: center;
    margin: 0 25%;
    height: 70px;
    border-bottom: solid grey 3px;
    padding-bottom: 10px;

}
#navigation{
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: flex-end;
    width: 100%;
    margin: 0;
    padding: 0;
    height: 70px;
}
#navigation li{
    display: inline;
}

</style>
