<template>
  <div class="community">
    <div class="d-flex flex-column align-items-center">
      <!-- <img src="@/assets/images/banner.jpg" alt="" height="200px" width="100%">  -->
    </div>
    
    <div class="d-flex flex-column justify-content-center align-items-center" v-if="articles.length === 0" style="height: 500px;">
      <div class="m-2"><img src="@/assets/images/caution.png" alt=""></div>
      <div class="m-2"><h3>작성된 게시글이 존재하지 않습니다.</h3></div>
      <div class="m-2"><button class="btn btn-primary" @click="moveToCreate()">게시글 작성하기</button></div>
    </div>
    
    <div class="d-flex m-auto searchDiv">
      <input id="searchBar" type="text" placeholder="검색어를 입력하세요">
      <img id="searchBtn" src="@/assets/images/search.png" alt="" width=25px style="cursor: pointer;">
      <hr>
    </div>
    
    <div class="container my-5 py-2">
      <div class="row align-items-center articles"
        v-for="article in articles" 
        :key="article.id" 
        @click="onDetail(article)">
        <hr>
        <div class="col-3 create_date">
          {{ article.created_at.substring(0, 10).split('-')[0] }}.
          {{ article.created_at.substring(0, 10).split('-')[1] }}.
          {{ article.created_at.substring(0, 10).split('-')[2] }}
        </div>
        <div class="col-9 text-start">
          <p><strong><h3>{{ article.title }}</h3></strong></p>
          <p>{{ article.content }}</p>
          <p class="text-end user-text">{{ article.user }}</p>
        </div>          
      </div>
    </div>
    <button class="createBtn mt-5 btn ms-auto fixed-bottom m-5" @click="toCreate()">Write</button>

    <!-- <div class="overflow-auto">
      <b-table
        id="community_article"
        :items="articles"
        :per-page="perPage"
        small
        @row-clicked="onDetail()"
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
    </div> -->


    <router-view/>
  </div>

</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'Community',
  data: function () {
    return {
      articles: [],
      perPage: 8, 
      user_id: '',
    }
  },
  methods: {
    checkUser: function () {
      const token = localStorage.getItem('jwt')

      if (token !== null) {
        const decodedJWT = jwt_decode(token)
        this.user_id = decodedJWT.user_id
      } 
      else {
        this.user_id = ''
      }
    },
    onDetail: function (article) {
      this.$store.state.article = article
      this.$router.push({name: 'Article'})
    },
    toCreate: function () {
      if (!localStorage.getItem('jwt')) {
        alert('로그인이 필요합니다.')
        this.$router.push({name: 'Login'})
      } else {
        this.$router.push({name: 'Create'})
      }
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
    },
    // onDetail(record, index){
    // console.log(index)  // index값 사용은 해야해서 넣음 추후 안 보이게 해도 될 듯
    // this.$store.state.article = record
    // this.$router.push({name: 'Article'})
    // },
    moveToCreate: function () {
      this.$router.push({name: 'Create'})
    }
  },
  computed: {
    rows() {
      return this.articles.length
    }
  },
  created: function () {
    this.onLoad()
    this.checkUser()
  }
}
</script>

<style>
#searchBar {
  border: none;
  width: 100%;
}
.searchDiv{
  border-bottom: 1px solid lightslategray;
  width: 25%;
}
#searchBtn:hover{
  transition: 0.3s;
  border: 2px solid black;
  border-radius: 0.45rem;
}
.create_date{
  font-size: 35px;
  color: lightslategray
}
.articles:hover{
  background-color: lightsteelblue;
  cursor: pointer;
}
.user-text{
  color: lightslategray;
}
.createBtn{
  background-color: black;
  color: white;
  font-size: 30px;
  width: 200px;
  height: 100px;
  font: italic;
}
</style>