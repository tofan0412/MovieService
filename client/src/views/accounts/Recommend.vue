<template>
  <div class="recommend container">
    <h1>추천 페이지입니다.</h1>
    <h3>좋아하는 영화를 선택해 주세요.</h3>
    <div class="row">
      <div :id="'movie-'+ movie.id" 
        class="card col-3" :class="{selected: movie.selected}"
        v-for="movie in movies" 
        :key="movie.id" 
        @click="onSelect(movie)"
      >
        <input type="text" disabled="disabled">
        <img :src="movie.image" alt="" width="300px" height="500px">
        <h5 class="card-title">{{ movie.title }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Recommend',
  data: function () {
    return {
      movies: [],
      myMovies: [],
      isSelected: true,
    }
  },
  methods: {
    onSelect: function (movie) {
      movie.selected = !movie.selected

      if (!this.myMovies.includes(movie.id)) {        
        this.myMovies.push(movie.id)
      }
      else if (this.myMovies.includes(movie.id)){
        this.myMovies.splice(this.myMovies.indexOf(movie.id))
      }
    }
  },
  created: function () {
    axios({
      url: `${this.$store.state.SERVER_URL}/movies/recommend/`,
      method: 'POST',
    })
    .then(resp => {
      for (let i = 0; i < resp.data.length; i++){
        resp.data[i].selected = false
      }
      this.movies = resp.data
    
    })
    .catch(err => {
      console.log(err)
    })
  },
}
</script>

<style>
.selected > *{
  opacity: 0.3;
}
</style>