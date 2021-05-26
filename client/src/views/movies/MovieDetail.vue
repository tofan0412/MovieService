<template>
  <div class="movieDetail p-3">
    <div class="movie">
      <div class="movie-header">
        <div class="container">
          <div class="row align-items-center">
            <div class="col-6 my-3">
              <img class="movie-image" :src="this.movie.image" alt="">
            </div>
            <div class="col-6 my-3">
              <div class="row mb-5">
                <h1>{{ this.movie.title }}</h1>
                <h3>{{ this.movie.subtitle }}</h3> 
              </div>
              <div class="row text-start">
                <div class="col-10">
                  <p>개봉일 : {{ this.movie.pubDate }}</p>
                  <p>사용자 평점 : {{ this.movie.userRating }}</p>
                </div>
                <div class="col-2" >
                  <img :src="like?like_img_path:unlike_img_path" alt="" width="30px;" @click="doLike()">
                </div>
              </div>
              <div class="row text-start">
                <h4>개요</h4>
                <p>{{ this.movie.overview }}</p>
              </div>
              
            </div>
          </div>
        </div>
      </div>
      <div class="container mt-5">
        <div class="row">
          <div class="col-6 text-start">
            <h3>관람객 평점</h3>
            <div class="row mt-3" v-for="rev in reviews" :key="rev.id">
              <div class="col-10">
                <p>
                <span v-for="index in Number(rev.rank)" :key="index">
                  <img :src="start_img_path" alt="" width="15px">
                </span>
                &nbsp;<strong><span>{{ rev.rank }}</span></strong>
                </p>
                <h5>{{ rev.title }}</h5>
                {{ rev.content }}
                <p class="text-secondary">{{ rev.user_id }} | {{ rev.created_at }}</p>  
              </div>
              <div class="col-2 d-flex justify-content-center align-items-middle">
                <button v-if="rev.user_id === user_id" class="btn btn-light del-btn" @click="delReview(rev)"
                >X</button>
              </div>
              <hr>
            </div>
          </div>
          <div class="col-6 reviewCreate text-start p-3">
            <!-- <label for="reviewTitle">제목</label> -->
            <textarea name="" id="제목" cols="60" rows="1" v-model.trim="params.title" placeholder="제목:"></textarea>
            <br>
            <!-- <label for="reviewContent">내용</label> -->
            <textarea name="reviewContent" id="reviewContent" cols="60" rows="5" v-model="params.content" placeholder="내용:"></textarea>
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
            <button @click="onSubmit" class="btn btn-primary">관람평 작성</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie: this.$route.query.movieObj,
      reviews: [],
      params: {
        title: null,
        content: null,
        rank: null,
      },
      like: false,
      user_id: this.$store.state.userId,
      start_img_path: require('@/assets/images/star.png'),
      like_img_path: require('@/assets/images/like.png'),
      unlike_img_path: require('@/assets/images/unlike.png'),
    }
  },
  methods: {
    onLoad: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/movies/detail/${this.$route.query.movieObj.id}/review_list/`,
        method: 'GET',
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
        // 비워주자.
        this.params.title = ''
        this.params.content = ''
        this.params.rank = '선택'
      })
      .catch(err => {
        console.log(err)
      })
    },
    delReview: function (rev) {
      const factor = confirm("관람객 평점을 삭제하시겠습니까?")
      if (factor) {
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
    doLike: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/movies/like/`,
        method: 'POST',
        data: this.movie,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        // resp.data.status가 202이면 좋아요, 204면 좋아요 취소
        if (resp.data.status === 202) {
          this.like = true
        } else if (resp.data.status === 204) {
          this.like = false
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    checkLike: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/movies/check/like/`,
        method: 'POST',
        data: this.movie,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        if (resp.data.status === 202) {
          this.like = true
        } else if (resp.data.status === 204) {
          this.like = false
        }
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created: function () {
    this.onLoad()
    this.checkLike()
  },
}
</script>

<style>
.movie-header{
  background-color: rgb(3, 37, 65);
  width: 100%;
  height: 25%;
  color: white;
  border-radius: 0.8rem;
}
.movie-image{
  width: 400px;
  height: 520px;
}
.reviewCreate{
  border: 2px solid grey;
  border-radius: 0.45rem;
}
</style>