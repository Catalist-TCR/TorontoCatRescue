<template>
    <div class="card-container">
        <div class="image">
            <img class="kitty-image" src="../../images/cat1.jpg" />
        </div>
        <div class="personal-details">
            <h2 style="font-size: 18px;">Hugely Big</h2>
            <p><b>22/06/2042</b></p>
            <p><b>Male</b></p>
            <span>S/N: <span><b>No</b></span></span>
            <div id="medical">
                <legend>Medical Documents:</legend>
                <a href="#">attachment 1</a>
                <br/>
                <a href="#">attachment 2</a>
            </div>
        </div>
        <div class="extra-info">
            <p><span>Requested Date:</span><b>Date</b></p>
            <p><span> FIV: </span><b>test result</b></p>
            <p><span> FLV: </span><b>test result</b></p>
            <p><span> FVRCP Vaccination: </span><b>test result</b></p>
            <p><span> Rabies Vaccination: </span><b>test result</b></p>
            <p><span> Medical Description: </span><b>test result</b></p>
            <p><span> Behaviour Description: </span><b>test result</b></p>
        </div>
        <img id="edit-cat-info" src="" />
    </div>
</template>


<script>
export default {
  name: 'card',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card-container{
  display: grid;
  grid-template-columns: 150px 1fr 2fr;
  grid-gap: 10px;
  background-color: #fff;
  color: #444;
  font-size: 14px;
  -webkit-box-shadow: 0px 2px 2px 0px rgba(186,186,186,0.5);
  -moz-box-shadow: 0px 2px 2px 0px rgba(186,186,186,0.5);
  box-shadow: 0px 2px 2px 0px rgba(186,186,186,0.5);
  border-bottom: 2px solid black;
  margin-bottom: 10px;
}
.card-container:hover{
  border-bottom: 2px solid #34A798;
}
#medical a{
    margin-left: 20%;
    color: #00558C;
}
.card-container p{
    margin: 5px 0;
}
.card-container div{
  background-color: white;
  color: black;
}
.kitty-image{
    max-width: 150px;
}
.personal-details, .extra-info{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: end;
    max-height: 200px;
}
.personal-details h2{
    color: #00558C;
    margin: 0;
}
</style>
