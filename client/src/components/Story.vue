<template>
  <div class="container">
    <h2>Story</h2>
    Title: {{ story.title }}<br/>
    Description: {{ story.description }}<br/>
    <button
      type="button"
      class="btn btn-sm btn-light"
      v-b-modal.story-update-modal
      @click="editStory(story)">
      Update
    </button>

    <b-modal ref="editStoryModal"
             id="story-update-modal"
             title="Update Story"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group"
                      label="Title:"
                      label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-edit-group"
                      label="Description:"
                      label-for="form-description-edit-input">
          <b-form-input id="form-title-description-input"
                        type="text"
                        v-model="editForm.description"
                        required
                        placeholder="Enter description">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import {API_LOCATION} from "@/config";

export default {
  data() {
    return {
      story: {},
      editForm: {
        id: '',
        title: '',
      },
      socketMessage: '',
      showMessage: false,
    };
  },
  components: {
  },
  sockets: {
    storyModified(data) {
      this.socketMessage = data;
      this.showMessage = true;
      this.getStory();
    },
  },
  methods: {
    updateStory(payload) {
      const path = `${API_LOCATION}/story/`;
      axios.put(path, payload)
        .then(() => {
          this.getStory();
          this.message = 'Story updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getStory();
        });
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editStoryModal.hide();
      const payload = {
        title: this.editForm.title,
        description: this.editForm.description,
      };
      this.updateStory(payload, this.editForm.id);
    },
    onResetUpdate() {
    },
    getStory() {
      const path = `${API_LOCATION}/story/`;
      axios.get(path)
        .then((res) => {
          this.story = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    editStory(story) {
      this.editForm = story;
    },
  },
  created() {
    this.getStory();
  },
};

</script>

<style scoped>

</style>
