import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import socketio from 'socket.io-client';
import VueSocketIO from 'vue-socket.io';

import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

if (localStorage.username === undefined && !window.location.href.endsWith('/login')) {
  window.location.replace('/login');
}

Vue.use(BootstrapVue);

const socket = socketio('http://localhost:5000/', { path: '/prefix/socket.io' });

Vue.use(new VueSocketIO({
  debug: true,
  connection: socket,
}));

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
