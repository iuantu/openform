import Vue from 'vue'
import VueRouter from 'vue-router'
import router from './router'
import VueResource from 'vue-resource'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import App from './App.vue'
import './plugins/element.js'

import FormSummary from './components/FormSummary'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(ElementUI)

Vue.config.productionTip = false

// const routes = [
//   { path: '/form/:id', component: FormSummary}
//   // { path: '/foo', component: Foo },
//   // { path: '/bar', component: Bar }
// ]

const router = new VueRouter({
  routes // (缩写) 相当于 routes: routes
})

new Vue({
  // render: h => h(App),
  router,
  render: h => h(App),
}).$mount('#app')
