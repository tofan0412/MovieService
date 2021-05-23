<template>
  <div class="create">
    <h1>글 작성하기</h1>
    <input type="text" name="title" id="title" v-model.trim="article.title"><br>
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
      axios({
        url: '',
        method: 'POST',
        params: this.article,
      })
      .then(resp => {
        console.log(resp)
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