<template>
  <div class="main container">
    <div class="row my-5">
      <h3 class="text-start">당신을 위한 추천 영화</h3>
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
        </div>
        <div class="container carousel-inner bg-dark text-white">
          <div 
            class="col-6 carousel-item" :class="{ active: idx === 0 }" 
            v-for="(movie, idx) in recommendMovieList" 
            :key="movie.id" @click="onDetail(movie)"
          >
            <div class="row align-items-center justify-content-center">
              <img class="col-5 p-5" :src="movie.image" alt="..." width="500px" height="650px">
              <div class="col-5 p-5 text-start">
                <div class="row">
                  <div class="col-12">
                    <h2>{{ movie.title }}</h2>
                  </div>
                </div>
                <div class="row">
                  <div class="col-12">
                    {{ movie.overview }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
    
    <!-- card 형태로  영화 목록을 출력한다. -->
    <!-- <div class="row">
      <div class="card col-2" v-for="movie in recommendMovieList" :key="movie.id" @click="onDetail(movie)">
        <img :src="movie.image" alt="">
        <span>{{movie.title}}</span>
      </div>
    </div> -->
    
    <h3 class="text-start">최신 영화</h3>
    <div class="row my-3 justify-content-center bg-dark">
      
      <div class="card col-3 movie-card p-1 mtext-white" v-for="movie in movieList" :key="movie.id" @click="onDetail(movie)">
        <img :src="movie.image" alt="" height="450px">
        <h5 class="card-title mt-3">{{movie.title}}</h5>
        
        
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'FrontPage',
  data: function () {
    return {
      movieList: [],
      recommendMovieList: [],
      pageNum: 2,
    }
  },
  // 로드될 때 영화 목록을 불러온다.
  created: function () {
    // 스크롤 이벤트 감지..
    window.addEventListener('scroll', this.handleScroll)

    axios({
      url: `${this.$store.state.SERVER_URL}/movies?page=1`,
      method: 'GET',
    })
    .then(resp => {
      this.movieList = resp.data
    })
    .catch(err => {
      console.log(err)
    })
    this.recommendMovie()
  },
  methods: {
    handleScroll: function () {
      if (this.pageNum === 20) { 
        return
      }
      // console.log('스크롤..')
      const {scrollTop, clientHeight, scrollHeight} = document.documentElement
      // console.log(scrollTop, clientHeight, scrollHeight)
      if (scrollHeight - scrollTop -1 < clientHeight) {
        axios({
          url: `${this.$store.state.SERVER_URL}/movies?page=${this.pageNum}`,
          method: 'GET',
        })
        .then(resp => { 
          // 마지막에 갖다 붙이기만 하면 된다.
          this.movieList.push(... resp.data)
          this.pageNum++
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    onDetail: function (movie) {
      this.$router.push({name: 'MovieDetail', query: {movieObj: movie, }})
    },
    recommendMovie: function () {
      // 사용자가 로그인한 경우: 사용자 선호 장르 기반 추천
      if (localStorage.getItem('jwt')) {
        axios({
          url: `${this.$store.state.SERVER_URL}/movies/favorite/list/user`,
          method: 'POST',
          // token이 있는 경우에만 headers를 전송한다
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`,
          },
        })
        .then(resp => {
          this.recommendMovieList = resp.data
        })
        .catch(err => {
          console.log(err)
        })
      }
      // 사용자가 로그인하지 않은 경우: 평점 기반 추천
      else if (!localStorage.getItem('jwt')) {
        axios({
          url: `${this.$store.state.SERVER_URL}/movies/favorite/list/anonymousUser`,
          method: 'POST',
        })
        .then(resp => {
          this.recommendMovieList = resp.data
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
  },
}
</script>

<style>
.movie-card{
  background-color: rgb(3, 37, 65);
  border-radius: 0.45rem;
  color: white;
}
</style>