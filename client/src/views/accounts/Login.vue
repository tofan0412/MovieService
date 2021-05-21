<template>
  <div class="login">
    <label for="username">사용자 아이디</label>
    <input type="text" name="username" id="username" v-model="credentials.username">
    <br>
    <label for="password">비밀번호</label>
    <input type="text" name="password" id="password" v-model="credentials.password">
    <br>
    <button @click="onLogin">로그인</button>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    onLogin: function () {

    }
  }
}
</script>

<style>

</style>