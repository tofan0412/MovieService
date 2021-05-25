<template>
  <div class="create">
    <form>
      <div class="mb-3">
        <h1>글 작성하기</h1>
      </div>
      <div class="mb-3">
        <!-- <label for="제목" class="form-label">제목:  </label> -->
        <textarea name="" id="제목" cols="60" rows="1" v-model.trim="article.title" placeholder="제목:"></textarea>
      </div>
      <!-- <label for="내용" class="form-label">내용:  </label> -->
      <textarea name="" id="" cols="60" rows="3" v-model.trim="article.content" placeholder="내용:"></textarea>
      <p><button type="submit" class="btn btn-primary" @click="onSubmit">작성</button></p>
    </form>
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