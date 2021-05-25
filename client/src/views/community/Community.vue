<template>
  <div class="community">
    <h1>게시판입니다.</h1>
    <router-link :to="{name: 'Create'}">글 작성하기</router-link>

  <div v-for="article in articles" 
    :key="article.id" 
    @click="onDetail(article)">
      {{ article.id }}
      {{ article.title }}
      {{ article.content }}
  </div>

  <nav aria-label="Page navigation example" class="mb-3">
  <ul class="pagination" >
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
  </nav>
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
    },
    onLoad: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/community/`,
        method: 'GET',
      })
      .then(resp => {
        this.articles = resp.data
        this.$store.state.article = null // 선택할 게시글 객체 초기화
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created: function () {
    this.onLoad()
  }
}
</script>

<style>

</style>