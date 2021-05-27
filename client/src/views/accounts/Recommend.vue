<template>
  <div class="recommend container">
    <h3>좋아하는 영화를 선택해 주세요.</h3>
    <div class="row bg-dark">
      <div 
        class="card col-3 movie-card p-1" :class="{selected: movie.selected}"
        v-for="movie in movies" 
        :key="movie.id" 
        @click="onSelect(movie)"
      >
        <img :src="movie.image" alt="" height="450px">
        <h5 class="card-title mt-3">{{ movie.title }}</h5>
      </div>
    </div>
    <div class="row fixed-bottom" >
      <button class="btn btn-primary" @click="onSubmit()">선택 완료</button>
    </div>

    <div class="mySelectList">
      <div class="d-flex align-items-center px-2 demo-01" v-for="myMovie in myMoviesObj" :key="myMovie.id">
        {{ myMovie.title }}
        <hr>
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
      myMoviesObj: [],
      isSelected: true,
    }
  },
  methods: {
    onSelect: function (movie) {
      movie.selected = !movie.selected

      if (!this.myMovies.includes(movie.id)) {        
        this.myMovies.push(movie.id)
        this.myMoviesObj.push(movie)
      }
      else if (this.myMovies.includes(movie.id)){
        const pos = this.myMovies.indexOf(movie.id)
        const pos2 = this.myMoviesObj.indexOf(movie)
        if (pos !== -1) {
          this.myMovies.splice(pos, 1)  
        }
        if (pos2 !== -1) {
          this.myMoviesObj.splice(pos2, 1)  
        }
      }
    },
    onSubmit: function () {
      if (this.myMovies.length < 3) {
        alert("3개 이상의 영화를 고르셔야 합니다..")  
        return
      } else {
        axios({
          url: `${this.$store.state.SERVER_URL}/movies/favorite/create/`,
          method: 'POST',
          data: this.myMovies,
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`,
          },   
        })
        .then(resp => {
          console.log(resp.status)
          alert('추천 영화가 등록되었습니다.')
          this.$router.push({name: 'FrontPage'})
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    mouseOver: function (target) {
      target.style = ['background-color: grey;', 'color: white;']
    },
    mouseLeave: function (target) {
      target.style = ''
    },

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
.movie-card{
  background-color: rgb(3, 37, 65);
  border-radius: 0.45rem;
  color: white;
}
.mySelectList{
  border: 2px solid black;
  border-radius: 0.45rem;
  position: fixed;
  left: 80%;
  top: 35%;
  overflow-y: scroll;
  width: 10%;
  height: 30%;
}
.demo-01:hover{
  background-color: grey;
  color: white;
}
</style>