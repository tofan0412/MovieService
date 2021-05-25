<template>
  <div class="article">
    <div>       
    <form>
      <p><h2>제목: {{ this.article.title }}</h2><p>
      <p><h2>내용: {{ this.article.content }}</h2><p>
      <p><h5>생성시간: {{ this.article.created_at }}</h5><p>
      <p><h5>수정시간: {{ this.article.updated_at }}</h5><p>
      <button @click="toUpdatePage"  class="btn btn-outline-secondary">게시글 수정</button>
      <button @click="onDelete"  class="btn btn-outline-secondary">게시글 삭제</button>
      
      <div class="mb-3">
        <h3>댓글 작성</h3>
        <input name="comment" id="comment" v-model="comment_content">
        <button @click="commentSubmit">작성</button>
      </div>

      
      <div v-for="comment in comments" :key="comment.id">
        <p>{{ comment.user }} : {{ comment.content }}
        생성시간: {{ comment.created_at }} 수정시간: {{ comment.updated_at }}
        <button @click="onDelete_Comment(comment)">X</button></p>
      </div>
    </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Article',
  data: function () {
    return {
      article: this.$store.state.article,
      comments: [],
      comment_content: '',
    }
  },
  created: function () {
    this.onLoad()
  },
  methods: {
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
    }

  },
}
</script>

<style>

</style>