<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Q&D Estimation</h1>
        <Story/>
        <Users/>
        <VoteOptions/>
        <hr>
        Voting as {{ getUserName() }}
        <button type="button" class="btn" @click="doLogout()">Logout</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { API_LOCATION } from "@/config"

import Users from './Users.vue';
import Story from './Story.vue';
import VoteOptions from './VoteOptions.vue';

export default {
  name: 'App',
  components: {
    Story,
    Users,
    VoteOptions,
  },
  beforeCreate() {
  },
  methods: {
    doLogout() {
      console.info('performing logout');
      const path = `${API_LOCATION}/users/${localStorage.username}`;
      localStorage.removeItem('username');
      axios.delete(path);
      this.$router.push('/login');
    },
    getUserName() {
      return localStorage.username;
    },
  },
};
</script>
