<template>
  <div class="create">
    <div class="my-5">
      <textarea class="demo" name="" id="제목" cols="60" rows="1" v-model.trim="article.title" placeholder="제목을 입력하세요" style="resize: none;"></textarea>
    </div>
    <textarea class="demo" name="" id="" cols="60" rows="10" v-model.trim="article.content" placeholder="내용을 입력하세요" style="resize: none;"></textarea>
    <p><button type="submit" class="btn btn-outline-secondary" @click="onSubmit()">작성</button></p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Create',
  data: function () {
    return {
      article: {
        title: '',
        content: '',
      },
    }
  },
  methods: {
    onSubmit: function () {
      const article = {
        title: this.article.title,
        content: this.article.content,
      }
      
      if (article.title == '') {
        alert('제목을 입력해 주세요.')
        return
      }

      if (article.content == '' ) { 
        alert('내용을 입력해 주세요.')
        return
      }
      
      axios({
        url: `${this.$store.state.SERVER_URL}/community/articlelist_create/`,
        method: 'POST',
        data: article,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        this.$store.state.article = resp.data
        this.$router.push({name: 'Article'})
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created: function () {
    // 게시글 작성하기 전에, 로그인되어 있는지를 확인한다.
    if (localStorage.getItem('jwt')) {
      // 로그인이 되어 있으므로, 게시글을 작성할 수 있다.
    } else {
      alert('로그인이 필요한 기능입니다.')
      this.$router.push({name: 'Login'})
    }
  },
  mounted: function () {

  },
}
</script>

<style>
.demo{
  border: none;
  border-bottom: 1px black solid;
}
</style>