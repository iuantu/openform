import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import './plugins/element.js'

import FormSummary from './components/FormSummary'

Vue.use(VueRouter)
Vue.config.productionTip = false

const routes = [
  { path: '/form/:id', component: FormSummary}
  // { path: '/foo', component: Foo },
  // { path: '/bar', component: Bar }
]

const router = new VueRouter({
  routes // (缩写) 相当于 routes: routes
})

new Vue({
  // render: h => h(App),
  router,
  render: h => h(App),
}).$mount('#app')
