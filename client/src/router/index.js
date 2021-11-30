import Vue from 'vue';
import Router from 'vue-router';
import EstimoIndex from '../components/EstimoIndex.vue';
import EstimoLogin from '../components/EstimoLogin.vue';
import EstimoLogout from '../components/EstimoLogout.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Index',
      component: EstimoIndex,
    },
    {
      path: '/login',
      name: 'Login',
      component: EstimoLogin,
    },
    {
      path: '/logout',
      name: 'Logout',
      component: EstimoLogout,
    },
  ],
});
