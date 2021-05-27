<template>
  <div class="create">
    <div class="my-5">
      <textarea class="demo" name="" id="제목" cols="60" rows="1" v-model.trim="article.title" placeholder="제목을 입력하세요" style="resize: none;"></textarea>
    </div>
    <textarea class="demo" name="" id="" cols="60" rows="10" v-model.trim="article.content" placeholder="내용을 입력하세요" style="resize: none;"></textarea>
    <div>
      <button type="submit" class="btn btn-outline-secondary" @click="$router.push({name: 'Article'})">취소</button>&nbsp;
      <button type="submit" class="btn btn-outline-secondary" @click="onUpdate()">수정</button>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Update',
  data: function () {
    return {
      article: {
        title: this.$store.state.article.title,
        content: this.$store.state.article.content,
      }
    }
  },
  methods: {
    onUpdate: function () {
      const article = {
        title: this.article.title,
        content: this.article.content,
      }
      
      axios({
        url: `${this.$store.state.SERVER_URL}/community/${this.$store.state.article.id}/article_update_delete/`,
        method: 'PUT',
        data: article,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`,
        },
      })
      .then(resp => {
        console.log(resp)
        this.$store.state.article = resp.data
        this.$router.push({name: 'Article'})
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>
  
<style>
.demo{
  border: none;
  border-bottom: 1px black solid;
}
</style>