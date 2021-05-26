import createPersistedState from "vuex-persistedstate"
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    // 로그인 확인 변수
    article: {
      type: Object,
    },
    
    // Server URL 변수
    SERVER_URL: process.env.VUE_APP_SERVER_URL,
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
  
})
