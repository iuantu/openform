import Vue from 'vue'
import Router from 'vue-router'


import FormList from './../components/FormList'
import Register from '../components/Register'
import Login from './../components/Login'

import OpenForm from './../pages/openform/openForm'
import OpenFormList from './../pages/openFormList/openFormList'
import TheFormSummary from './../components/openform/formSummary'
import FormEditor from '../components/control_panel/FormEditor'
import FormData from '../components/FormData'
import FormReporter from '../components/FormReporter'
import FormPublish from '../components/FormPublish'

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
      path: '/openform/:id',
      component: OpenForm,
      children: [
        { path: 'summary', name: 'cp_form_summary', component: TheFormSummary },
        { path: 'editor', name: 'cp_form_editor', component: FormEditor },
        { path: 'data', name: 'cp_form_data', component: FormData },
        { path: 'reporter', name: 'cp_form_reporter', component: FormReporter },
        { path: 'publish', name: 'cp_form_publish', component: FormPublish },
      ]
    },
    { path: '/cp/form', name: 'cp_form_list', component: FormList},
    {
      path: '/',
      component: OpenFormList
    }
  ]
})
