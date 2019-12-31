import Vue from 'vue'
import Router from 'vue-router'
import OpenForm from './../pages/openform/openForm'
import FormSummary from './../components/FormSummary'


import FormList from './../components/FormList'
import ControlPanel from './../components/ControlPanel'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'OpenForm',
      component: OpenForm
    },
    {
      path: '/cp', component: ControlPanel,
      children: [
        { path: 'form/:id/', name: "cp_form_summary", component: FormSummary},
        { path: '', component: FormList},
      ]
    },
  ]
})
