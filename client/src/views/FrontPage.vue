<template>
  <div class="main">
    <h1>메인입니다.</h1>
    <!-- card 형태로  영화 목록을 출력한다. -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'FrontPage',
  data: function () {
    return {
      movieList: [],
    }
  },
  // 로드될 때 영화 목록을 불러온다.
  
  created: function () {
    axios({
      url: `${this.$store.state.SERVER_URL}/movies/`,
      method: 'GET',
    })
    .then(resp => {
      console.log(`${this.$store.state.SERVER_URL}`)
      console.log(resp.data)
      this.movieList = resp.data
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>

<style>

</style>