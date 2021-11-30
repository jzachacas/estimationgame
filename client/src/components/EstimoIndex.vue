<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Q&D Estimation Game</h1>
        <EstimoStory/>
        <EstimoUsers/>
        <EstimoVoteOptions/>
        <hr>
        Voting as {{ getUserName() }}
        <button type="button" class="btn" @click="doLogout()">Logout</button>
      </div>
    </div>
  </div>
</template>

<script>

import EstimoUsers from './EstimoUsers.vue';
import EstimoStory from './EstimoStory.vue';
import EstimoVoteOptions from './EstimoVoteOptions.vue';

export default {
  name: 'App',
  components: {
    EstimoStory,
    EstimoUsers,
    EstimoVoteOptions,
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
