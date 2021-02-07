<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Q&D Estimation Game</h1>
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
      this.$router.push('/logout');
    },
    getUserName() {
      return localStorage.username;
    },
  },
};
</script>
