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
        <svg version="1.1" id="edit-cat" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 24 24" style="enable-background:new 0 0 24 24;" xml:space="preserve">
            <path d="M18.4,8.5l1.4,1.4L7.1,22.6L0,24l1.4-7.1L14.1,4.2l1.4,1.4L3.3,17.9l-0.7,3.6l3.6-0.7C6.1,20.7,18.4,8.5,18.4,8.5z M18.3,0 l-2.8,2.8l5.7,5.7L24,5.7C24,5.7,18.3,0,18.3,0z M6,18.7L17.3,7.4l-0.7-0.7L5.3,18C5.3,18,6,18.7,6,18.7z"/>
        </svg>
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
  margin-bottom: 30px;
  width: 75%;
  position: relative;
}
.card-container:hover{
  -webkit-box-shadow: 0px 2px 2px 0px rgba(52,167,152,0.5);
  -moz-box-shadow: 0px 2px 2px 0px rgba(52,167,152,0.5);
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
#edit-cat{
    position: absolute;
    top: 5%;
    right: 1%;
    width: 35px;
}
#edit-cat:hover{
    cursor: pointer;
    fill: #34A798;
}
</style>
