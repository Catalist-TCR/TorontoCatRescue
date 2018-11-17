<template>
  <div id="login-field">
    <h2>Login Here</h2>
    <form id="login-form">
        <label for="email">E-mail:</label>
        <input id="email-input" type="text"/>
        <br />
        <label for="password">Password:</label>
        <input id="password-input" type="text"/>
        <br/>
        <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>

export default {
  name: 'Login',
  props: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #login-field{
      text-align: center;  
    }
    #login-form{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>
