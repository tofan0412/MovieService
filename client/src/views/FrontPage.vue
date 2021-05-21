<template>
  <div class="main">
    <h1>메인입니다.</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'main',
  data: function () {
    return {
      movieList: [],
    }
  },
  // 로드될 때 영화 목록을 불러온다.
  created: function () {
    axios({
      url: '',
      method: 'POST',
    })
    .then(resp => {
      console.log(resp)
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>

<style>

</style>