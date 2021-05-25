<template>
  <div class="main container">

  <!-- 헤더에 배경 이미지 넣고 출력할 것. -->
  <!-- <header class="d-flex flex-column justify-content-center align-items-center">
    <div class="display-2 text-white fw-bold">SSAFY BOX</div>
  </header> -->


    <!-- card 형태로  영화 목록을 출력한다. -->
    <div class="row">
      <h3>추천 영화</h3>
      <div class="card col-2" v-for="movie in recommendMovieList" :key="movie.id" @click="onDetail(movie)">
        <img :src="movie.image" alt="">
        <span>{{movie.title}}</span>
      </div>
    </div>
    
    <div class="row">
      <h3>최신 영화</h3>
      <div class="card col-3" v-for="movie in movieList" :key="movie.id" @click="onDetail(movie)">
        <img :src="movie.image" alt="">
        <span>{{movie.title}}</span>
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
    }
  },
  // 로드될 때 영화 목록을 불러온다.
  created: function () {
    axios({
      url: `${this.$store.state.SERVER_URL}/movies/`,
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
    onDetail: function (movie) {
      this.$router.push({name: 'MovieDetail', query: {movieObj: movie, }})
    },
    recommendMovie: function () {
      if (this.$store.state.isLogin === true) {
        axios({
          url: `${this.$store.state.SERVER_URL}/movies/favorite/list/user`,
          method: 'POST',
          // token이 있는 경우에만 headers를 전송한다
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`,
          },
        })
        .then(resp => {
          console.log(resp)
        })
        .catch(err => {
          console.log(err)
        })
      }
      else if (this.$store.state.isLogin === false) {
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

</style>