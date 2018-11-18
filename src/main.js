import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Welcome from './components/Welcome.vue';
import Add from './components/Add.vue';

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', component: Welcome },
    { path: '/login', component: Welcome },
    { path: '/add', component: Add },
  ]
})

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
