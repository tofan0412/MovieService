/<template>
  <div class="login container">
    <div class="row mt-5">
      <h1>Login</h1>
    </div>
    <div class="row p-3">
      <div class="col-12 my-3">
        <input type="text" id="username" class="form-control"
          v-model.trim="credentials.username" placeholder="아이디" @keyup="rememberMe2()">
        <br>
        <input 
          type="password" name="password" id="password" class="form-control" 
          v-model.trim="credentials.password" placeholder="비밀번호" @keyup.enter="onLogin()">

        <div class="row justify-content-between align-items-center mt-3">
          <div class="col-12 text-start">
            <input type="checkbox" @click="rememberMe()" :checked="check">&nbsp;remember me
          </div>
          <div class="col-12">
            <button id="loginBtn" class="btn btn-lg btn-primary w-100 mt-5" @click="onLogin()">로그인</button>
          </div>
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
      },
      check: false,
    }
  },
  methods: {
    onLogin: function () {
      // 데이터 검증하기.
      const credentials = {
        username: this.credentials.username,
        password: this.credentials.password,
      }

      if (credentials.username === '' || credentials.username === null || credentials.password === '' || credentials.password === null) {
        alert("아이디 또는 비밀번호를 확인해 주세요.")
        return
      }

      axios({
        url: `${this.$store.state.SERVER_URL}/accounts/api/token/auth/`,
        method: 'POST',
        data: this.credentials,
      })
      .then(resp => {
        localStorage.setItem('jwt', resp.data.token)
        // 모든 axios 요청에 jwt 토큰을 기본적으로 함께 전송한다.
        axios.defaults.headers.common['Authorization'] = `JWT ${localStorage.getItem('jwt')}`
        this.$router.push({name: 'FrontPage'})
      })
      .catch(err => {
        console.log(err)
        alert('아이디 혹은 비밀번호를 잘못 입력하였습니다.')
      })
    },
    rememberMe: function () {
      
      this.check = !this.check
      if (this.check) {
        const user_id = this.credentials.username
        if (this.credentials.username === null || this.credentials.username === ''){
          localStorage.setItem('userId', '')
          this.check = false 
          return 
        }
        localStorage.setItem('userId', user_id)
      } else {
        localStorage.removeItem('userId')
      }
      
    },
    rememberMe2: function () {
      if (this.check){
        if (this.credentials.username === null || this.credentials.username === ''){
          localStorage.setItem('userId', '')
        } else {
          localStorage.setItem('userId', this.credentials.username)
        }
      }
    },
  },
  created: function () {
    const rememberMe = localStorage.getItem('userId')
    if (rememberMe) {
      this.credentials.username = rememberMe
      this.check = true
    }
  }
}
</script>

<style>
.login{
  border: 1px solid grey;
  border-radius: 0.45rem;
  width: 25%;
  height: 40%;
}
</style>