<template>
  <div class="signup">
    <label for="username">사용자 아이디</label>
    <input type="text" name="username" id="username" v-model.trim="credentials.username">
    <br>
    <label for="password">비밀번호</label>
    <input type="password" name="password" id="password" v-model.trim="credentials.password">
    <br>
    <label for="password">비밀번호 확인</label>
    <input type="password" name="passwordConfirmation" id="passwordConfirmation" v-model.trim="credentials.passwordConfirmation">
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
      axios({
        url: `${this.$store.state.SERVER_URL}/accounts/signup/`,
        method: 'POST',
        data: this.credentials,
      })
      .then(resp => {
        console.log(resp)
        // 사용자 정보가 DB에 저장되었으므로, 토큰을 발급한 후에 페이지 이동한다.
        this.authorization()
      })
      .catch(err => {
        //  확인 비밀번호와 일치하지 않는 경우, 이 곳으로 오게 된다.
        console.log(err)
      })
    },
    authorization: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/accounts/api/token/auth/`,
        method: 'POST',
        data: {
          username: this.credentials.username,
          password: this.credentials.password,
        },
      })
      .then(resp => {
        localStorage.setItem('jwt', resp.data.token)
        this.$store.state.isLogin = true
        this.$store.state.userId = this.credentials.username
        this.$router.push({name: 'Recommend'})
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