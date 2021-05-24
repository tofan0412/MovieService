<template>
  <div class="update">
    <h1>글 수정하기</h1>
    <label for=""></label>
    <input type="text" name="title" id="title" v-model.trim="article.title"><br>
    <label for=""></label>
    <textarea name="" id="" cols="30" rows="10" v-model.trim="article.content"></textarea>
    <button @click="onUpdate">글 수정하기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Update',
  data: function () {
    return {
      article: {
        title: this.$store.state.article.title,
        content: this.$store.state.article.content,
      }
    }
  },
  methods: {
    onUpdate: function () {
      const article = {
        title: this.article.title,
        content: this.article.content,
      }
      
      axios({
        url: `${this.$store.state.SERVER_URL}/community/${this.$store.state.article.id}/article_update_delete/`,
        method: 'PUT',
        data: article,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        console.log(resp)
        this.$store.state.article = resp.data
        this.$router.push({name: 'Article'})
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