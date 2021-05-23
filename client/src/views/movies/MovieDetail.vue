<template>
  <div class="movieDetail">
    <div class="movie">
      <h1>영화 디테일입니다.</h1>
      <h1>{{ $route.params.movieObj.title }}</h1>  
      <h2>{{ $route.params.movieObj.subtitle }}</h2>  
      <img :src="$route.params.movieObj.image" alt="">
      <p>감독 : {{ $route.params.movieObj.director }}</p>
      <p>출연 배우 : {{ $route.params.movieObj.actor }}</p>
      <p>관람객 평점 : {{ $route.params.movieObj.userRating }}</p>
    </div>
    <!-- 관람평 목록 출력 -->
    <div class="reviewList">
      <div v-for="review in reviews" :key="review.id">


      </div>
    </div>

    <div class="reviewCreate">
      <h1>관람평 작성하기</h1>
      <label for="reviewTitle">제목</label>
      <input type="text" name="reviewTitle" id="reviewTitle" v-model="params.title">
      <br>
      <label for="reviewContent">내용</label>
      <textarea name="reviewContent" id="reviewContent" cols="30" rows="10" v-model="params.content"></textarea>
      <br>
      <label for="reviewRank">별점</label>
      <select v-model="params.rank">
        <option value="default">선택</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
      </select>
      <button @click="onSubmit">관람평 작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie_id: this.$route.params.movieObj.id,
      reviews: [],
      params: {
        title: null,
        content: null,
        rank: null,
      }
    }
  },
  created: function () {
    // vue 객체가 생성될 때, axios 통해 관람평 데이터를 불러온다.
    // 방식은 GET 방식 ...

    axios({
      url: `${this.$store.state.SERVER_URL}/movies/detail/${this.movie_id}/rank_list_create/`,
      method: 'GET',
    })
    .then(resp => {
      this.reviews = resp.data
    })
    .catch(err => {
      console.log(err)
    })
  },
  methods: {
    // 새로운 관람평 작성 함수.
    onSubmit: function () {
      const review = {
        title: this.params.title,
        content: this.params.content,
        rank: this.params.rank,
      }
      console.log(review)
      axios({
        url: `${this.$store.state.SERVER_URL}/movies/detail/${this.movie_id}/rank_list_create/`,
        method: 'POST',
        data: review,
      })
      .then(resp => {
        console.log(resp)
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>