<template>
  <div class="movieDetail">
    <div class="movie">
      <h1>영화 디테일입니다.</h1>
      <h1>{{ $route.query.movieObj.title }}</h1>  
      <h2>{{ $route.query.movieObj.subtitle }}</h2>  
      <img :src="$route.query.movieObj.image" alt="">
      <p>감독 : {{ $route.query.movieObj.director }}</p>
      <p>출연 배우 : {{ $route.query.movieObj.actor }}</p>
      <p>관람객 평점 : {{ $route.query.movieObj.userRating }}</p>
    </div>
    <!-- 관람평 목록 출력 -->
    <ul class="reviewList">
      <h1>작성한 관람평</h1>
      <li v-for="rev in reviews" :key="rev.id">
        {{ rev.id }}
        {{ rev.title }}
        {{ rev.content }}
        <button @click="delReview(rev)" class="del-btn">X</button>
        <hr>
      </li>
    </ul>

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
      reviews: [],
      params: {
        title: null,
        content: null,
        rank: null,
      },
    }
  },
  methods: {
    onLoad: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/movies/detail/${this.$route.query.movieObj.id}/review_list_create/`,
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        this.reviews = resp.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    onSubmit: function () {
      const review = {
        title: this.params.title,
        content: this.params.content,
        rank: this.params.rank,
      }
      
      axios({
        url: `${this.$store.state.SERVER_URL}/movies/detail/${this.$route.query.movieObj.id}/review_list_create/`,
        method: 'POST',
        data: review,
        // headers 설정이 있어야 request.user를 사용할 수 있다! 안 그러면 AnonymousUser..
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        console.log(resp)
        this.onLoad()
      })
      .catch(err => {
        console.log(err)
      })
    },
    delReview: function (rev) {
      console.log("리뷰 삭제합니다..")
      axios({
        method: 'DELETE',
        url: `${this.$store.state.SERVER_URL}/movies/detail/${rev.id}/review_delete/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        console.log(resp)
        this.onLoad()
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted: function () {
    this.onLoad()
  },
}
</script>

<style>
</style>