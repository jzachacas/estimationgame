<template>
  <div class="container">
    <b-form v-on:submit.prevent="doLogin" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Please enter your Name:"
                    label-for="form-title-edit-input">
        <b-form-input id="form-title-edit-input"
                      type="text"
                      v-model="username"
                      value="lorem"
                      required
                      placeholder="Enter your name here">
        </b-form-input>
      </b-form-group>
    </b-form>
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
      username: localStorage.lastUsername,
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
            localStorage.setItem('lastUsername', res.data.username);
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
