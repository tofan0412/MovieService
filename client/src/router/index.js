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
    // 게시글 목록 Read 페이지
    path: '/community',
    name: 'Community',
    component: () => import(/* webpackChunkName: "about" */ '@/views/community/Community')
  },
  {
    // 게시글 Read 페이지
    path: `/community/article/`,
    name: 'Article',
    component: () => import(/* webpackChunkName: "about" */ '@/views/community/Article')
  },
  {
    // 게시글 Create 페이지
    path: `/community/article/create`,
    name: 'Create',
    component: () => import(/* webpackChunkName: "about" */ '@/views/community/Create')
  },
  {
    // 게시글 Update 페이지
    path: `/community/article/update`,
    name: 'Update',
    component: () => import(/* webpackChunkName: "about" */ '@/views/community/Update')
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
