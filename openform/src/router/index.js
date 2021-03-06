import Vue from 'vue'
import Router from 'vue-router'


import FormList from './../components/FormList'
import Register from '../components/Register'
import Login from './../components/Login'

import Form from './../pages/Form/Form'
import FormEditor from '../components/control_panel/FormEditor'
import FormData from '../components/FormData'
import FormReporter from '../components/FormReporter'
import FormPublish from '../components/FormPublish'

import FormSummary from '../components/FormSummary';
import FormPreview from '../components/FormPreview';

// import OpenFormPublic from './../pages/openFormPublic/openFormPublic'

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
      path: '/form',
      component: Form,
      children: [
        { path: 'summary/:id', name: 'cp_form_summary', component: FormSummary },
        { path: 'editor', name: 'cp_form_editor', component: FormEditor },
        { path: 'editor/:id', name: 'cp_form_editor_edit', component: FormEditor },
        { path: 'preview/:id', name: 'cp_form_preview', component: FormPreview },
        { path: 'data/:id', name: 'cp_form_data', component: FormData },
        { path: 'reporter/:id', name: 'cp_form_reporter', component: FormReporter },
        { path: 'publish/:id', name: 'cp_form_publish', component: FormPublish },
      ]
    },
    { path: '/cp/form', name: 'cp_form_list', component: FormList},
    {
      path: '/',
      component: FormList
    }
  ]
})
