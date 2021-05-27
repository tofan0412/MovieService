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
            <h3>관람평</h3>
            <div class="d-flex justify-content-center align-items-center" v-if="reviews.length === 0" style="height: 150px;">
              <p><img src="@/assets/images/caution.png" alt="caution" width="30px"></p>
              <h5 class="text-center " style="color: grey;">이 영화의 첫번째 평을 등록해 주세요.</h5>
              <hr>
            </div>
            <div class="row mt-3 review" :id="'review'+rev.id" v-for="rev in reviews" :key="rev.id" @mouseover="doMouseOver()">
              
              <div class="col-9">
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

              <div class="col-3 d-flex justify-content-center align-items-center">
                <button type="button" v-if="rev.user_id === user_id" 
                  class="btn btn-light update-btn" 
                  data-bs-toggle="modal" data-bs-target="#exampleModal"
                  @click="updateReviewValue(rev)">
                  수정
                </button> 
                <button v-if="rev.user_id === user_id" class="btn btn-light del-btn" @click="delReview(rev)">삭제</button>
              </div>

              <!-- 관람평 수정 관련 modal 창.. -->
              <div class="modal fade" tabindex="-1" id="exampleModal" ref="exampleModal">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title">관람평 수정하기</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                      <textarea id="updateReviewTitle" v-model.trim="updateReview.title" cols="55" rows="1" placeholder="제목:" style="resize: none;"></textarea>
                        <br>
                        <!-- <label for="reviewContent">내용</label> -->
                        <textarea id="updateReviewContent" v-model.trim="updateReview.content" cols="55" rows="5" placeholder="내용:" style="resize: none;"></textarea>
                        <br>
                        <label for="reviewRank">별점</label>
                        <select v-model="updateReview.rank">
                          <option value="default">선택</option>
                          <option value="1">1</option>
                          <option value="2">2</option> 
                          <option value="3">3</option>
                          <option value="4">4</option>
                          <option value="5">5</option>
                        </select>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                      <button type="button" class="btn btn-primary" @click="onUpdate()" data-bs-dismiss="modal">수정하기</button>
                    </div>
                  </div>
                </div>
              </div>
              

              <hr>
            </div>
          </div>
          <div class="col-6 and youtube text-start p-3">
            <!-- 유튜브 영상 출력 부분 -->
            <h3>트레일러 영상</h3>
            <div class="video-container" >
              <iframe 
                class="iframebox mb-3" 
                v-if="teaser"
                id="youtube player" 
                :src="videoURI"
                type="video" 
                frameborder="0"              
              >
              </iframe>
            </div>
          </div>
        </div>
        <!-- 관람평 작성 부분 -->
        <div class="row">
          <div class="col-6">
            <textarea name="" id="제목" cols="75" rows="1" v-model.trim="params.title" placeholder="제목:" style="resize: none;"></textarea>
            <br>
            <!-- <label for="reviewContent">내용</label> -->
            <textarea name="reviewContent" id="reviewContent" cols="75" rows="5" v-model="params.content" placeholder="내용:" style="resize: none;"></textarea>
            <br>
            <div class="d-flex justify-content-between">
              <div>
                <label for="reviewRank">별점</label>&nbsp;
                <select v-model="params.rank">
                  <option value="default">선택</option>
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option value="5">5</option>
                </select>
              </div>
              <button @click="onSubmit" class="btn btn-primary">관람평 작성</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie: this.$route.query.movieObj,
      reviews: [],
      teaser: null,
      // 새로 작성하는 관람평의 내용을 담기 위한 데이터.
      params: {
        title: '',
        content: '',
        rank: '',
      },
      // 수정하는 글의 내용을 담기 위한 데이터.
      updateReview: {
        id: null,
        title: null,
        content: null,
        rank: null,
      },
      like: false,
      user_id: '',
      start_img_path: require('@/assets/images/star.png'),
      like_img_path: require('@/assets/images/like.png'),
      unlike_img_path: require('@/assets/images/unlike.png'),
    }
  },
  methods: {
    checkUser: function () {
      const token = localStorage.getItem('jwt')
      // jwt 토큰이 존재하는 경우

      if (token !== null) {
        const decodedJWT = jwt_decode(token)
        this.user_id = decodedJWT.user_id
      } 
      // jwt 토큰이 존재하지 않는 경우..
      else {
        this.user_id = ''
      }
    },
    doMouseOver: function () {
      
    },
    Youtube: function () {
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const input = this.movie.subtitle + 'trailer'

      const params = {
        key: "AIzaSyB17QVL_fP8qY89CTsNQV1Dl3ZWHeRoCzc",
        part: 'snippet',
        type: 'video',
        q: input,
      }
      axios({
        method: 'GET',
        url: API_URL,
        params,
      }).then(resp => {
        this.teaser  = resp.data.items[0]
      })
      .catch(err => {
        console.log(err)
      })
    },
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
      // 로그인 유무를 확인한다.
      if (!localStorage.getItem('jwt')) {
        alert('로그인 해주세요.')
        this.$router.push({name: "Login"})
        return
      }

      // 데이터 검증한다.
      if (review.title.length === 0 || review.content.length === 0 || review.rank.length === 0 || review.rank === 'default') {
        alert('작성하지 않은 내용이 존재합니다. 확인해 주세요.')
        return
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
        alert('로그인 해주세요.')
        this.$router.push({name: 'Login'})
      })
    },
    delReview: function (rev) {
      const factor = confirm("삭제하시겠습니까?")
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
    updateReviewValue: function (rev) {
      // 모달 창 내 제목, 내용을 입력하는 부분을 기존의 내용으로 채워준다.
      this.updateReview.id = rev.id
      this.updateReview.title = rev.title
      this.updateReview.content = rev.content
      this.updateReview.rank = rev.rank
    },
    hideModal() {
      this.$refs['exampleModal'].hide()
    },
    onUpdate: function () {
      const review = {
        id: this.updateReview.id,
        title: this.updateReview.title,
        content: this.updateReview.content,
        rank: this.updateReview.rank,
      }
      if (review.title.length === 0 || review.content.length === 0 || review.rank.length === 0 || review.rank === 'default') {
        alert('게시글 내용을 정확하게 입력해 주세요.')
        return
      }
      
      axios({
        url: `${this.$store.state.SERVER_URL}/movies/detail/${review.id}/review_update/`,
        method: 'PUT',
        data: review,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        console.log(resp)
        // 업데이트 하였으므로, 다시 관람평 목록을 reload한다.
        this.updateReview.id = null,
        this.updateReview.title = null,
        this.updateReview.content = null,
        this.updateReview.rank = null,
        this.modalShow = false
        this.onLoad()
      })
      .catch(err => {
        console.log(err)
      })
    },
    doLike: function () {
      if (!localStorage.getItem('jwt')) {
        alert('로그인이 필요한 기능입니다.')
        this.$router.push({name: 'Login'})
        return
      }
      
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
      // 사용자가 로그인하지 않은 경우 수행하지 않는다.
      const token = localStorage.getItem('jwt')
      if (token === null) {
        return
      }
      
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
    computed: {
      videoURI: function () {
        const videoId = this.teaser.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      }
    },
  created: function () {
    this.checkUser()  // 사용자 확인
    this.onLoad()     // 관람평 불러오기
    this.checkLike()  // 해당 영화 좋아요 했는지 유무 확인
    this.Youtube()    // 유튜브 티저 영상 불러오기
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

.iframebox{
  display: block;
  border: none;
  height: 40vh;
  width: 23vw;
}
.selectedReview{
  background-color: gray;
}
</style>