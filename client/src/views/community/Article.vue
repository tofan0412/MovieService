<template>
  <div class="article">
    <div class="container">
    <div class="card">
        <div class="card-body">
            <h2 class="card-title" align="start">제목: {{ this.article.title }}</h2>      
        </div>
        <div class="card-body">
            <h2 align="start">내용: {{ this.article.content }}</h2>    
        </div>     
        <div class="card-body">
            <h5 align="left">생성시간: {{ this.article.created_at }}</h5>  
            <h5 align="left">수정시간: {{ this.article.updated_at }}</h5>
        </div>   
    </div>
    <div class="row mt-3">
      <div class="col-auto">
          <button type="button"
            v-if="article.user === user_id"
            @click="toUpdatePage"  
            class="btn btn-outline-secondary">
            게시글 수정
          </button>
      </div>
      <div class="col-auto mb-5">
          <form>                
              <button type="button"              
                v-if="article.user === user_id"
                @click="onDelete"  
                class="btn btn-outline-secondary">
                게시글 삭제
              </button>
          </form>
      </div>
       </div>
    </div>
    <div class="mb-4">
        <h3 >댓글 작성</h3>
        <input name="comment" id="comment" v-model="comment_content"><button @click="commentSubmit" class="btn btn-outline-secondary">작성</button>        
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
          </button></h6>
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
    toUpdatePage: function () {
      this.$router.push({name: 'Update'})
    },
    commentSubmit: function () {
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

</style>