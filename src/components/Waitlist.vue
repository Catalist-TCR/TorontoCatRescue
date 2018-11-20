<template>
  <main id="waitlist">
    <section>
      <h2>{#} Cats</h2>
      <p>These cats have been proposed to Toronot Cat Rescue by a shelter, and are currently on the waitlist.</br>You can still edit their information if required.
      </p>
    </section>
    <Card />
    <Card />
    <Card />
    <Card />
    <button type="submit">Submit</button>
  </main>
</template>

<script>
import Card from './Card.vue';

//this is to export variables here, to be passed up to parent files
export default {
  name: 'Waitlist',
  components: {
    Card
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
.text-input{
    display: block;
}
#add-cat{
    display: flex;
    flex-direction: column;
    justify content: center;
    align-items: end;
}
#main label, #main span {
    color: #34A798;
}
input[type=radio] {
    width: 30px;
    height: 2em;
}
#waitlist{
    grid-column: 2;
}

#waitlist section{
  width: 100%;
  margin-left: 25%;
  text-align: left;
}
</style>
