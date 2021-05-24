<template>
  <div class="community">
    <h1>게시판입니다.</h1>
    <div v-for="article in articles" :key="article.id">
      {{ article.title }}
      {{ article.content }}
      {{ article.created_at }}
    </div>
    <router-link :to="{name: 'Create'}">글 작성하기</router-link>
    <router-view/>
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
  created: function () {
    axios({
      url: `${this.$store.state.SERVER_URL}/community/`,
      method: 'GET',
    })
    .then(resp => {
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