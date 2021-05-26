/<template>
  <div class="login container">
    <div class="row6yt8ii/">
      <div class="col-6 mt-5">
        <input type="text" id="username" class="form-control"
          v-model="credentials.username" placeholder="아이디">
        <br>
        <input 
          type="password" name="password" id="password" class="form-control" 
          v-model="credentials.password" placeholder="비밀번호">
        <br>
        <div class="row justify-content-between align-items-center">
          <div class="col-3">
            <input type="checkbox">&nbsp;아이디 기억하기
          </div>
          <div class="col-4">
            <button id="loginBtn" class="btn btn-lg btn-primary" @click="onLogin">로그인</button>
          </div>
        </div>
        <div class="col-6">
          <img src="" alt="">
        </div>
      </div>
    </div>
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
        this.$store.state.userId = this.credentials.username
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
.login{
  border: 1px solid grey;
  border-radius: 0.45rem;
}
</style>