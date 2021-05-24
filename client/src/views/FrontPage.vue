<template>
  <div class="main container">
    <h1>메인입니다.</h1>
    <!-- card 형태로  영화 목록을 출력한다. -->
    <div class="row">
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
  },
  methods: {
    onDetail: function (movie) {
      this.$router.push({name: 'MovieDetail', query: {movieObj: movie, }})
    }
  }
}
</script>

<style>

</style>