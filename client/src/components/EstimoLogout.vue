<template>
  <div class="container">
    Logging out
  </div>
</template>

<script>
import axios from 'axios';
import { API_LOCATION } from '@/config';

export default {
  name: 'EstimoLogin',
  data() {
    return {
      username: localStorage.lastUsername,
    };
  },
  methods: {
    doLogout() {
      console.info('performing logout');
      const path = `${API_LOCATION}/users/${localStorage.username}`;
      localStorage.removeItem('username');
      axios.delete(path);
      this.$router.push('/login');
    },
  },
  created() {
    this.doLogout();
  },
};
</script>
