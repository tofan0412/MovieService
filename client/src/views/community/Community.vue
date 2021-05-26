<template>
  <div class="community">
    <h1>SSAFY BOX 사용자 게시판</h1>
    <h2 align="right"><router-link :to="{name: 'Create'}">글 작성하기</router-link></h2>
    <!-- <div 
      v-for="article in articles" 
      :key="article.id" 
      @click="onDetail(article)">
        {{ article.id }}
        {{ article.title }}
        {{ article.content }}
    </div> -->

    <div class="overflow-auto">
      <b-table
        id="community_article"
        :items="articles"
        :per-page="perPage"
        :current-page="currentPage"
        small
        @row-clicked="onDetail"
      ></b-table>

      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        align="center"
        size="lg"
        first-text="⏮"
        prev-text="⏪"
        next-text="⏩"
        last-text="⏭"
        class="mt-4"
      ></b-pagination>

      <p class="mt-3">Current Page: {{ currentPage }}</p>
    </div>


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
      perPage: 2,
      currentPage: 1,    
    }
  },
  methods: {
    // onDetail: function (article) {
    //   this.$store.state.article = article
    //   this.$router.push({name: 'Article'})
    // },
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
    },
    onDetail(record, index){
    console.log(index)  // index값 사용은 해야해서 넣음 추후 안 보이게 해도 될 듯
    this.$store.state.article = record
    this.$router.push({name: 'Article'})
  }
  },
  computed: {
    rows() {
      return this.articles.length
    }
  },
  created: function () {
    this.onLoad()
  }
}
</script>

<style>

</style>