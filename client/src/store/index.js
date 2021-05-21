import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 로그인 확인 변수
    isLogin: false,
    // Server URL 변수
    SERVER_URL: process.env.VUE_APP_SERVER_URL,
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
