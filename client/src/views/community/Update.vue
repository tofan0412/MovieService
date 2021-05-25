<template>
  <div class="update">
    <form>
      <div class="mb-3">
        <h1>글 수정하기</h1>
      </div>
      <div class="mb-3">
        <textarea name="" id="제목" cols="60" rows="1" v-model.trim="article.title" placeholder="제목:"></textarea>
      </div>
      <textarea name="" id="" cols="60" rows="3" v-model.trim="article.content" placeholder="내용:"></textarea>
      <p><button type="submit" class="btn btn-primary" @click="onUpdate">글 수정하기</button></p>
    </form>

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