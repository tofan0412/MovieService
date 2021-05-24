<template>
  <div class="article">
    <div>
      <h1>게시글입니다.</h1>
      <p>{{ this.article.title }}</p>
      <p>{{ this.article.content }}</p>
      <p>{{ this.article.created_at }}</p>
      <p>{{ this.article.updated_at }}</p>
      <button @click="toUpdatePage">게시글 수정</button>
      <button @click="onDelete">게시글 삭제</button>
    </div>
    <div>
      <div v-for="comment in comments" :key="comment.id">
        {{ comment.user }}
        {{ comment.content }}
        <button @click="onDelete_Comment(comment)">X</button>
      </div>
      <h1>댓글 작성</h1>
      <input name="comment" id="comment" v-model="comment_content">
      <button @click="commentSubmit">작성</button>
      
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
    // 게시글에 작성된 댓글 목록을 불러온다.
    this.onLoad()

  },
  methods: {
    onLoad: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/community/${this.$store.state.article.id}/comment_list_create/`,
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
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
        url: `${this.$store.state.SERVER_URL}/community/${this.$store.state.article.id}/`,
        method: 'DELETE',
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
      axios({
        url: ``,
        method: 'DELETE',
      })
      .then(resp => {
        console.log(resp)
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