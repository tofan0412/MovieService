<template>
  <div class="signup">
    <label for="username">사용자 아이디</label>
    <input type="text" name="username" id="username">
    <br>
    <label for="password">비밀번호</label>
    <input type="text" name="password" id="password">
    <button @click="onSignup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  methods: {
    onSignup: function () {
      console.log(SERVER_URL)
      axios({})
    }
  }  
}
</script>

<style>

</style>