<template>
  <div id="app">
    <div id="nav" class="navbar sticky-top bg-dark">
      <router-link :to="{name: 'FrontPage'}">Main</router-link> |
      <router-link :to="{name: 'Community'}">Community</router-link> |
      <router-link :to="{name: 'Signup'}">Signup</router-link> |
      <router-link :to="{name: 'Login'}">Login</router-link> |
      <router-link to="#" @click.native="onLogout">Logout</router-link> |
    </div>
    <router-view class="mt-5"/>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  methods: {
    // jwt 토큰을 이용한 인증 확인 필요.
    onLogout: function () {
      console.log('로그아웃 메서드입니다.')
      localStorage.removeItem('jwt')
      this.$store.state.isLogin = false
      axios.defaults.headers.common['Authorization'] = ``
      this.$router.push({name: "Login"})
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>