<template>
  <div id="app" class="container-fluid">
    <div id="nav" class="row justify-content-start align-items-center">
      <div class="col-2" @click="toMainPage()" style="cursor: pointer;">
        <img src="@/assets/images/logo2.png" alt="" width="80px">
        <img :src="imgPath" alt="로고" height="40px">
      </div>
      <router-link class="box col-2" :to="{name: 'FrontPage'}">Movies</router-link>
      <router-link class="box col-2" :to="{name: 'Community'}">Community</router-link>
      <!-- 로그인 하지 않은 경우 -->
      <div class="box col-2" v-if="!isLogin">
        <router-link :to="{name: 'Signup'}">Signup</router-link>
      </div>
      <div class="box col-2" v-if="!isLogin">
        <router-link :to="{name: 'Login'}">Login</router-link> 
      </div>
      <!-- 로그인한 경우 -->
      <div class="box col-2" v-if="isLogin">
        <router-link :to="{name: 'Recommend'}">Recommend</router-link>
      </div>
      <div class="box col-2" v-if="isLogin">
        <router-link r-link to="#" @click.native="onLogout">Logout</router-link>
      </div>
    </div>
    <router-view class="mt-5"/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      imgPath: require('@/assets/images/logo.png'),
      isLogin: '',
    }
  },
  methods: {
    // jwt 토큰을 이용한 인증 확인 필요.
    onLogout: function () {
      localStorage.removeItem('jwt')
      this.$store.state.isLogin = false
      this.$store.state.userId = 'Anonymous'
      axios.defaults.headers.common['Authorization'] = ``
      this.$router.push({name: "Login"})
    },
    checkLogin: function () {
      const jwt = localStorage.getItem('jwt')

      if (jwt) {
        this.isLogin = true
      } else {
        this.isLogin = false
      }
    },
    toMainPage: function () {
      this.$router.push({name: 'FrontPage'})
    }
  },
  updated: function () {
    this.checkLogin()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 1920px;
  height: 1080px;
  color: #2c3e50;

}
#nav {
  padding: 20px;
  background-color: rgb(3, 37, 65);
}
#nav a {
  font-weight: bold;
  color: white;
  font-size: 25px;
  text-decoration: none;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>