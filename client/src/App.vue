<template>
  <div id="app" class="container-fluid">
    <div id="nav" class="row justify-content-start align-items-center">
      <img class="box col-3" :src="imgPath" alt="로고" width="220" height="120">
      <router-link class="box col-2" :to="{name: 'FrontPage'}">Main</router-link>
      <router-link class="box col-2" :to="{name: 'Community'}">Community</router-link>
        <div class="box col-3" v-if="!this.$store.state.isLogin">
          <router-link :to="{name: 'Login'}">Login</router-link> | 
          <router-link :to="{name: 'Signup'}">Signup</router-link>
        </div>
        <div class="box col-2" v-else>
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
    }
  },
  methods: {
    // jwt 토큰을 이용한 인증 확인 필요.
    onLogout: function () {
      localStorage.removeItem('jwt')
      this.$store.state.isLogin = false
      axios.defaults.headers.common['Authorization'] = ``
      this.$router.push({name: "Login"})
    }
  },
  created: function () {
    const jwt = localStorage.getItem('jwt')

    if (jwt) {
      this.$store.state.isLogin = true
      // axios.defaults.headers.common['Authorization'] = `${jwt}` // 자식으로 등록 안하면, 소용없나..?
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
  width: 1920px;
  height: 1080px;
  color: #2c3e50;

}
#nav {
  padding: 20px;
  background-color: black;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>