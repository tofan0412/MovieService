<template>
  <div class="community">
    <h1>게시판입니다.</h1>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'Community',
  data: function () {
    return {
      articles: [],
    }
  },
  methods: {

  },
  // Vue 객체가 생성될 때 게시글 목록을 불러온다.
  created: function () {
    axios({
      url: '',
      method: 'POST',
    })
    .then(resp => {
      console.log(resp)
      this.articles = resp.data
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>

<style>

</style>