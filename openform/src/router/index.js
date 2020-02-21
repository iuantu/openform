import Vue from 'vue'
import Router from 'vue-router'
import FormSummary from './../components/FormSummary'
import FormData from './../components/TheFormData'
import FormList from './../components/FormList'
import FormControlPanel from './../components/FormControlPanel'
import Register from '../components/Register'

import OpenFormSetting from './../components/openform/openForm'
import Login from './../components/Login'
import OpenForm from './../pages/openform/openForm'

import OpenFormList from './../pages/openFormList/openFormList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/openform',
      name: 'OpenForm',
      component: OpenForm,
      children: [
        { path: '/', component: OpenFormSetting},
      ]
    },
    { path: '/cp/form', name: 'cp_form_list', component: FormList},
    {
      path: '/cp/form/:id', component: FormControlPanel,
      children: [
        { path: 'data', name: "cp_form_data", component: FormData},
        { path: 'summary', name: "cp_form_summary", component: FormSummary},
      ]
    },
    {
      path: '/openFormList',
      component: OpenFormList
    }
  ]
})
