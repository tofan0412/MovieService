<template>
  <div class="movieDetail">
    <h1>영화 디테일입니다.</h1>
    <h1>{{ $route.params.movieObj.title }}</h1>  
    <h2>{{ $route.params.movieObj.subtitle }}</h2>  
    <img :src="$route.params.movieObj.image" alt="">
    <p>감독 : {{ $route.params.movieObj.director }}</p>
    <p>출연 배우 : {{ $route.params.movieObj.actor }}</p>
    <p>관람객 평점 : {{ $route.params.movieObj.userRating }}</p>
  </div>
</template>

<script>

export default {
  created: function () {
    
  }
}
</script>

<style>

</style>