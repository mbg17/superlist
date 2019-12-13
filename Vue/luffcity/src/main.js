// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import Vuex from 'vuex'
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)
// import VueCookies from 'vue-cookies'
// Vue.use(VueCookies)
// 在vue的全局变量中设置了 $axios=axios
// 以后每个组件使用时：this.$axios
Vue.prototype.$axios = axios
Vue.prototype.$cookies = VueCookies
Vue.use(Vuex)
Vue.config.productionTip = false
const store = new Vuex.Store({
  state: {
    username: $cookies.get('username'),
    token: $cookies.get('token')
  },
  mutations: {
    setCookies(state, value) {
      state.username = value.username;
      state.token = value.token;
      $cookies.set('token', value.token, '1min');
      $cookies.set('username', value.username, '1min');
    },
    clearCookies(state) {
      state.username = '';
      state.token = '';
      $cookies.remove('token');
      $cookies.remove('username');
    }
  },
  actions: {
    login(context, value) {
      context.commit('setCookies', value)
    },
    logout(context) {
      context.commit('clearCookies', )
    }
  }
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {
    App
  },
  template: '<App/>'
})

// 路由守卫
router.beforeEach((to, from, next) => {
  if (to.meta.requiredAuth) {
    if (store.state.token) {
      next()
    } else {
      next({
        path: '/login',
        query: {
          redirect: to.fullPath
        },
      })
    }
  }else{
    next()
  }
})
