<template>
  <div class="article my-5">
    <div class="container">

      <div>
        <h2 class="text-start" align="start"><strong>{{ this.article.title }}</strong></h2>      
      </div>
      <!-- 작성자, 작성일, 최종 수정 시간.. -->
      <div class="row justify-content-start  align-items-center mt-5">
        <div class="col-1 text-start username">
          {{ this.article.user }}
        </div>
        <div class="col-2 text-start" style="color: lightslategray;">
          last update: {{ this.article.updated_at.substring(0, 10) }}
        </div>
      </div>
        
      <div class="mt-5 text-start">
        <span style="font-size: 40px;">{{ this.article.content.substring(0,1) }}</span>
        {{ this.article.content.substring(1,) }}
      </div>     
      <div class="mt-3" align="right" style="color: lightslategray;">
        craeted at: {{ this.article.created_at.substring(0, 10) }}
      </div>   

      <div class="row mt-3">
        <div class="col-auto">
          <button type="button"
            v-if="article.user === user_id"
            @click="$router.push({name: 'Update'})"  
            class="btn btn-outline-secondary">
            게시글 수정
          </button>
        </div>
        <div class="col-auto">
          <form>                
            <button type="button"              
              v-if="article.user === user_id"
              @click="onDelete()"  
              class="btn btn-outline-secondary">
              게시글 삭제
            </button>
          </form>
        </div>
        <div class="col-auto">
          <button class="btn btn-outline-secondary" @click="$router.push({name: 'Community'})">목록으로</button>
        </div>
      </div>
    </div>

    <!-- 댓글 부분 --> 
    <div class="mb-4">
      <h3 >댓글 작성</h3>
      <input name="comment" id="comment" v-model="comment_content"><button @click="commentSubmit()" class="btn btn-outline-secondary">작성</button>        
    </div>

    <div class="container">
      <div class="card">
          <div class="card-body">
            <div v-for="comment in comments" :key="comment.id">
              <h6 align="start"> {{ comment.user }} : {{ comment.content }}
                생성시간: {{ comment.created_at }} 수정시간: {{ comment.updated_at }}
                <button 
                  v-if="comment.user === user_id"
                  @click="onDelete_Comment(comment)" 
                  class="btn btn-outline-secondary">
                  X
                </button>
              </h6>
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
  name: 'Article',
  data: function () {
    return {
      article: this.$store.state.article,
      comments: [],
      comment_content: '',
      user_id: '',
    }
  },
  created: function () {
    this.onLoad()
    this.checkUser()
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
    // 게시글에 작성된 댓글 목록을 불러온다.
    onLoad: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/community/${this.$store.state.article.id}/comment_list/`,
        method: 'GET',
      })
      .then(resp => {
        this.comments = resp.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    onDelete: function () {
      const conf = confirm('게시글을 삭제하시겠습니까?')
      
      if (!conf) {
        return
      }
      axios({
        url: `${this.$store.state.SERVER_URL}/community/${this.$store.state.article.id}/article_update_delete/`,
        method: 'DELETE',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        console.log(resp)
        this.$router.push({name: 'Community'})
      })
      .catch(err => {
        console.log(err)
      })
    },
    commentSubmit: function () {
      if (!localStorage.getItem('jwt')){
        alert('로그인이 필요합니다.')
        this.$router.push({name: 'Login'})
      }

      const comment = {
        content : this.comment_content,
      }
      axios({
        url: `${this.$store.state.SERVER_URL}/community/${this.$store.state.article.id}/comment_list_create/`,
        method: 'POST',
        data: comment,
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
    onDelete_Comment: function (comment) {
      console.log(comment)
      axios({
        url: `${this.$store.state.SERVER_URL}/community/${comment.id}/comment_delete/`,
        method: 'DELETE',
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
  }  
}
</script>

<style>
.username{
  color: dodgerblue;
  font-size: 20px;
}
</style>