import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  // 회원 관련 URL
  {
    path: '/signup',
    name: 'Signup',
    component: () => import(/* webpackChunkName: "about" */ '@/views/accounts/Signup')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "about" */ '@/views/accounts/Login')
  },
  // 영화 페이지 관련 URL
  {
    path: '/frontPage',
    name: 'FrontPage',
    component: () => import(/* webpackChunkName: "about" */ '@/views/FrontPage')
  },
  {
    path: '/movieDetail',
    name: 'MovieDetail',
    component: () => import(/* webpackChunkName: "about" */ '@/views/movies/MovieDetail')
  },
  // 커뮤니티 관련 URL
  {
    path: '/community',
    name: 'Community',
    component: () => import(/* webpackChunkName: "about" */ '@/views/community/Community')
  },
  {
    path: `/community/article/`,
    name: 'Article',
    component: () => import(/* webpackChunkName: "about" */ '@/views/community/Article')
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
