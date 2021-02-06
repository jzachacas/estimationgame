<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h2>Users</h2>
        <alert :message=message v-if="showMessage"></alert>
        <table class="table table-hover">
          <caption>Votes</caption>
          <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Username</th>
            <th scope="col">Vote</th>
            <th scope="col">Actions</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(user, index) in users" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ user.username }}</td>
            <td>
              <span v-if="user['has_voted']">
                {{ user.vote }}
              </span>
              <span v-else>Pending</span>
            </td>
            <td>
              <button type="button" class="btn" @click="deleteUser(user)">Delete User</button>
            </td>
          </tr>
          </tbody>
        </table>
        <button type="button" class="btn" @click="clearCurrentVotes()">Clear Votes</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { API_LOCATION } from '@/config';

import Alert from '@/components/Alert.vue';

export default {
  data() {
    return {
      users: [],
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  sockets: {
    userVoted() {
      this.getUsers();
    },
    userJoined() {
      this.getUsers();
    },
    userDisconnected() {
      this.getUsers();
    },
    votesCleared() {
      this.message = 'Votes have been cleared';
      this.showMessage = true;
      this.getUsers();
    },
  },
  methods: {
    updateUserVotesDisplay() {
      let numVotes = 0;
      for (let i = 0; i < this.users.length; ++i) {
        if (this.users[i].has_voted) {
          ++numVotes;
        }
      }
      this.message = `Voted: ${numVotes} out of ${this.users.length} users.`;
      this.showMessage = true;
    },
    getUsers() {
      const path = `${API_LOCATION}/users`;
      axios.get(path)
        .then((res) => {
          this.users = res.data.users;
          this.updateUserVotesDisplay();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    clearCurrentVotes() {
      console.info('clearing votes');
      const path = `${API_LOCATION}/votes`;
      axios.delete(path)
        .then(() => {
          this.getUsers();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    deleteUser(user) {
      console.info(`deleting ${user.username}`);
      const path = `${API_LOCATION}/users/${user.username}`;

      axios.delete(path)
        .then(() => {
          this.getUsers();
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getUsers();
  },
};
</script>
