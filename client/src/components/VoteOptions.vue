<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h2>Possible Story Points:</h2>
        <br>
        <b-button-group size="lg">
          <b-button
            v-for="(btn, idx) in getVoteButtons()"
            :key="idx"
            :pressed.sync="btn.isSelected"
            variant="primary"
            v-on:click="doVote(btn.value)"
          >
            {{ btn.value }}
          </b-button>
        </b-button-group>
        <br>
        Your vote: {{ myVote }}
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import {API_LOCATION} from "@/config";

export default {
  data() {
    return {
      voteOptions: [],
      myVote: '',
    };
  },
  components: {},
  sockets: {
    votesCleared() {
      this.myVote = '';
    },
  },  methods: {
    getVoteOptions() {
      const path = `${API_LOCATION}/vote_options`;

      axios.get(path)
        .then((res) => {
          this.voteOptions = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    doVote(vote) {
      console.info(`voting ${vote}`);
      const path = `${API_LOCATION}/votes/${localStorage.username}`;

      axios.post(path, {vote})
        .then((res) => {
          if (res.status === 200) {
            this.myVote = vote;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getVoteButtons() {
      let result = [];
      for (let i = 0; i < this.voteOptions.length; ++i) {
        result.push({value: this.voteOptions[i], isSelected: this.voteOptions[i] === this.myVote});
      }
      return result;
    },
  },
  created() {
    this.getVoteOptions();
  },
};
</script>
