<template>
  <div class="login">
    <label for="username">사용자 아이디</label>
    <input type="text" name="username" id="username" v-model="credentials.username">
    <br>
    <label for="password">비밀번호</label>
    <input type="text" name="password" id="password" v-model="credentials.password">
    <br>
    <button @click="onLogin">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    onLogin: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/accounts/api/token/auth/`,
        method: 'POST',
        data: this.credentials,
      })
      .then(resp => {
        localStorage.setItem('jwt', resp.data.token)
        // login 여부 값을 true로 변경하고, 
        // 모든 axios 요청에 jwt 토큰을 기본적으로 함께 전송한다.
        this.$store.state.isLogin = true
        axios.defaults.headers.common['Authorization'] = `JWT ${localStorage.getItem('jwt')}`
        this.$router.push({name: 'FrontPage'})
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>