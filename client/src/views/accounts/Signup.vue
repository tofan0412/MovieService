<template>
  <div class="signup">
    <div class="card ">
        <div>
          <img class="img-responsive img" src="@/assets/images/SSAFYDB.png" alt="">
        </div>

        <div class="card-body">
            <p><label for="username">사용자 아이디</label></p>
          <input v-model.trim="credentials.username" placeholder="홍길동">
          <br>
        </div>
        <div class="card-body">
            <p><label for="password">비밀번호</label></p>
          <input type='password' v-model.trim="credentials.password">
          <br>
        </div>     
        <div class="card-body">
            <p><label for="password">비밀번호 확인</label></p>
          <input  type='password' v-model.trim="credentials.passwordConfirmation"> 
          <br>
        </div>
    </div>
    <button @click="onSignup" class="btn btn-outline-secondary mt-5">회원가입</button>   
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
.img {
  width:250px;
  height:250px;
}
</style>