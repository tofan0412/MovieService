<template>
  <div class="signup">
    <label for="username">사용자 아이디</label>
    <input type="text" name="username" id="username" v-model="credentials.username">
    <br>
    <label for="password">비밀번호</label>
    <input type="text" name="password" id="password" v-model="credentials.password">
    <br>
    <label for="password">비밀번호 확인</label>
    <input type="text" name="passwordConfirmation" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    <br>
    <button @click="onSignup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

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
      console.log(SERVER_URL)
      axios({
        url: `${SERVER_URL}/accounts/signup/`,
        method: 'POST',
        data: this.credentials,
      })
      .then(resp => {
        console.log(resp)
        // this.$router.push({name:})
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