import Vue from 'vue'
import VueRouter from 'vue-router'
// router配置
import router from './router'
import VueResource from 'vue-resource'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'

// 引入fontAwesome
import 'font-awesome/css/font-awesome.min.css'

// 引入公共方法
import publicMethods from './publicMethods/publicMethods'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(ElementUI)
Vue.use(publicMethods);


Vue.config.productionTip = false

new Vue({
  // render: h => h(App),
  router,
  render: h => h(App),
}).$mount('#app')
