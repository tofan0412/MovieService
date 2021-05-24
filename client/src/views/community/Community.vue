<template>
  <div class="community">
    <h1>게시판입니다.</h1>
    <div v-for="article in articles" :key="article.id" @click="onDetail(article)">
      {{ article.id }}
      {{ article.title }}
      {{ article.content }}
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
    onDetail: function (article) {
      this.$store.state.article = article
      this.$router.push({name: 'Article'})
    }
  },
  created: function () {
    axios({
      url: `${this.$store.state.SERVER_URL}/community/`,
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}`,
      },
    })
    .then(resp => {
      this.articles = resp.data
      this.$store.state.article = null // 선택할 게시글 객체 초기화
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>

<style>

</style>