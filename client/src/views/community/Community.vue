<template>
  <div class="community">    
    <div class="d-flex m-auto searchDiv">
      <input id="searchBar" type="text" placeholder="검색어를 입력하세요" v-model.trim="search_keyword" @keyup.enter="titleSearch()">
      <img id="searchBtn" src="@/assets/images/search.png" alt="" width="25px" style="cursor: pointer;" @click="titleSearch()">
      <img src="@/assets/images/reset.png" width="25px" class="btn btn-outline-secondary" @click="onLoad()">
      <hr>
    </div>
    
    <div class="d-flex flex-column justify-content-center align-items-center" v-if="articles.length === 0" style="height: 500px;">
      <div class="m-2"><img src="@/assets/images/caution.png" alt=""></div>
      <div class="m-2"><h3>작성된 게시글이 존재하지 않습니다.</h3></div>
      <div class="m-2"><button class="btn btn-outline-secondary" @click="$router.push({name: 'Create'})">게시글 작성하기</button></div>
    </div>
    
    <div class="container my-3 py-2">
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
    <button class="createBtn mt-5 btn ms-auto fixed-bottom m-5" v-if="user_id" @click="$router.push({name: 'Create'})">Write</button>

    
      <ul class="d-flex justify-content-center pagination mb-5">
        
        <li class="page-item"><a class="page-link" href="#" @click="nextPage(curr_page-1)">Prev</a></li>
        <!-- 얘를 반복해야 한다. -->
        <li class="page-item" v-for="page in total_page" :key=page>
          <a class="page-link" href="#" @click="nextPage(page)">{{ page }}</a>
        </li>
        
        <li class="page-item"><a class="page-link" href="#" @click="nextPage(curr_page+1)">Next</a></li>
      </ul>
    
  <!-- end of body -->
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
      user_id: '',
      search_keyword: '',
      total_page: 0,
      curr_page: 1,
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
    onLoad: function () {
      axios({
        url: `${this.$store.state.SERVER_URL}/community?page=1`,
        method: 'GET',
      })
      .then(resp => {
        this.articles = resp.data
        this.$store.state.article = null // 선택할 게시글 객체 초기화
        // 페이지네이터를 출력하기 위해, 필요한 페이지 수를 얻어온다.
        axios({
          url: `${this.$store.state.SERVER_URL}/community/getPage/`,
          method: 'GET',
        })
        .then(resp => {
          this.total_page = resp.data
        })
        .catch(err => {
          console.log(err)
        })
      })
      .catch(err => {
        console.log(err)
      })
    },
    titleSearch: function () {
      const result_article = []
      const keyword = this.search_keyword
      if (keyword.length === 0) {
        alert('검색어를 입력해 주세요.')
        this.onLoad()
        return
      }
      for (let i=0; i < this.articles.length; i++) {
        const tmp = this.articles[i]
        const head = tmp.title
        if (head.includes(keyword)) {
          console.log('찾았다')
          result_article.push(tmp)
        }
      }
      if (result_article.length === 0) {
        this.onLoad()
      } else {
        this.articles = result_article
      }
    },
    nextPage: function (page) {
      if (page <= 0 || page > this.total_page) {
        return
      }
      
      axios({
        url: `${this.$store.state.SERVER_URL}/community?page=${page}`,
        method: 'GET',
      })
      .then(resp => {
        this.articles = resp.data
        this.curr_page = page
      })
      .catch(err => {
        console.log(err)
      })
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