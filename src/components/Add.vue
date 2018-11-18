<template>
  <main id="main">
    <p>To submit a request to Toronto Cat Rescue...</p>
    <form id="add-cat"> 
        <label for="shelter">Shelter:</label>
        <input id="email-input" class="text-input" type="text"/>
        <br />
        <label for="shelter-id">Shelter ID:</label>
        <input id="shelter-id" class="text-input" type="text"/>
        <br/>
        <label for="cat-name">Password:</label>
        <input id="cat-name" class="text-input" type="text"/>
        <br/>
        <label for="DOB">Date of Birth (MM/DD/YYYY):</label>
        <input id="DOB" class="text-input" placeholder="MM/DD/YYYY" type="text"/>
        <br/>
        
        <!-- Sex & Reproductive Ability -->
        <div class="radio-div">
            <span>Sex</span>
            <span>
                <input type="radio" name="gender" value="male"> Male
            </span>
            <span>
                <input type="radio" name="gender" value="male"> Female
            </span>
            <br>
            <span>Spayed/Neutered</span>
            <span>
                <input type="radio" name="gender" value="male"> Yes
            </span>
            <span>
                <input type="radio" name="gender" value="male"> No
            </span>
            <br>
        </div>

        <!-- Disease & Testing -->
        <div class="radio-div">
            <span>FIV</span>
            <span>
                <input type="radio" name="gender" value="male"> Male
            </span>
            <span>
                <input type="radio" name="gender" value="male"> Female
            </span>
            <br>
            <span>FLV</span>
            <span>
                <input type="radio" name="gender" value="male"> Yes
            </span>
            <span>
                <input type="radio" name="gender" value="male"> No
            </span>
            <br>
        </div>


        <button type="submit">Submit</button>
    </form>
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
.text-input{
    display: block;
}
#add-cat{
    display: flex;
    flex-direction: column;
    justify content: center;
    align-items: end;
}
.radio-div{
    display: flex;
    flex-direction: column;
    justify content: center;
    align-items: end;
    align-self: end
}
#main{
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}
#main label, #main span {
    color: #34A798;
}
input{
    border-radius: 5px;
    border:1px solid #cccccc
}
input[type=radio] {
    width: 30px;
    height: 2em;
}
</style>
