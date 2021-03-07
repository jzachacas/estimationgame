import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import socketio from 'socket.io-client';
import VueSocketIO from 'vue-socket.io';

import { WS_LOCATION, WS_PATH } from '@/config';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

if (localStorage.username === undefined) {
  router.push({ name: 'Login' });
}
Vue.use(BootstrapVue);

const socket = socketio(WS_LOCATION, { path: WS_PATH });

Vue.use(new VueSocketIO({
  debug: true,
  connection: socket,
}));

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
