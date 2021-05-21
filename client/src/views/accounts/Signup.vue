<template>
  <div class="signup">
    <label for="username">사용자 아이디</label>
    <input type="text" name="username" id="username" v-model.trim="credentials.username">
    <br>
    <label for="password">비밀번호</label>
    <input type="text" name="password" id="password" v-model.trim="credentials.password">
    <br>
    <label for="password">비밀번호 확인</label>
    <input type="text" name="passwordConfirmation" id="passwordConfirmation" v-model.trim="credentials.passwordConfirmation">
    <br>
    <button @click="onSignup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: function() {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    onSignup: function () {
      console.log(this.$store.state.SERVER_URL)
      axios({
        url: `${this.$store.state.SERVER_URL}/accounts/signup/`,
        method: 'POST',
        data: this.credentials,
      })
      .then(resp => {
        this.$router.push({name: 'FrontPage'})
      })
      .catch(err => {
        console.log(err)
      })
    }
  }  
}
</script>

<style>

</style>