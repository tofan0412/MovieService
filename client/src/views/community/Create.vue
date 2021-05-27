<template>
  <div class="create">

    <!-- <form action="writerAction" method="post">
	<input type="text" name="bdTitle" class="form-control mt-4 mb-2"	placeholder="제목을 입력해주세요." required	>
	<div class="form-group">
		<textarea class="form-control" rows="10" name="bdContent"
			placeholder="내용을 입력해주세요" required
		></textarea>
	</div>
	<button type="submit" class="btn btn-secondary mb-3"  @click="onSubmit">제출하기</button>
</form> -->



  <form>
      <div class="mb-3">
        <h1>글 작성하기</h1>
      </div>
      <div class="mb-3">
        <textarea name="" id="제목" cols="60" rows="1" v-model.trim="article.title" placeholder="제목:"></textarea>
      </div>
      <textarea name="" id="" cols="60" rows="3" v-model.trim="article.content" placeholder="내용:"></textarea>
      <p><button type="submit" class="btn btn-primary" @click="onSubmit">작성</button></p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Create',
  data: function () {
    return {
      article: {
        title: null,
        content: null,
      },
    }
  },
  methods: {
    onSubmit: function () {
      const article = {
        title: this.article.title,
        content: this.article.content,
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
        console.log(resp)
        this.$router.push({name: 'Community'})
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

</style>