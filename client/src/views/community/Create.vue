<template>
  <div class="create">
    <h1>글 작성하기</h1>
    <label for=""></label>
    <input type="text" name="title" id="title" v-model.trim="article.title"><br>
    <label for=""></label>
    <textarea name="" id="" cols="30" rows="10" v-model.trim="article.content"></textarea>
    <button @click="onSubmit">작성</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Create',
  data: function () {
    return {
      article: {
        title: null,
        content: null,
      },
    }
  },
  methods: {
    onSubmit: function () {
      const article = {
        title: this.article.title,
        content: this.article.content,
      }
      
      axios({
        url: `${this.$store.state.SERVER_URL}/community/articlelist_create/`,
        method: 'POST',
        data: article,
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
    }
  },
  created: function () {
  
  },
  mounted: function () {

  },
}
</script>

<style>

</style>