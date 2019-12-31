import Vue from 'vue'
import Router from 'vue-router'
import OpenForm from './../pages/openform/openForm'
import FormSummary from './../components/FormSummary'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'OpenForm',
      component: OpenForm
    },
    { path: '/form/:id', component: FormSummary}
  ]
})
