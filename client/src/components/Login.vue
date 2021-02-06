<template>
  <div class="container">
    <label for="username"/>
    <input id="username" v-model="username" placeholder="edit me">
    <p>Username: {{ username }}</p>
    <button type="button" class="btn btn-primary" @click="doLogin()">Login</button>
  </div>
</template>

<script>
import axios from 'axios';
import { API_LOCATION } from '@/config';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
    };
  },
  methods: {
    doLogin() {
      const path = `${API_LOCATION}/login`;
      axios.post(path, {
        username: this.username,
      })
        .then((res) => {
          if (res.status === 200) {
            console.info(`login successful ${res.data.username}`);
            localStorage.setItem('username', res.data.username);
            this.$router.push('/');
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
  },
};
</script>
