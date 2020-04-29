import Vue from 'vue'
import Router from 'vue-router'


import FormList from '../components/cp/form/FormListPage'
import Register from '../components/Register'
import Login from './../components/Login'

import Form from '../components/form_container/FormContainer'
import FormEditor from '../components/cp/form/editor/FormEditorPage'
import FormDataPage from '../components/cp/form/data/FormDataPage'
import FormReporter from '../components/cp/form/FormReporter'
import FormPublish from '../components/cp/form/FormPublish'

import FormSummary from '../components/cp/form/summary/FormSummary';
import FormPreview from '../components/cp/form/FormPreview';

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
        { path: 'data/:id', name: 'cp_form_data', component: FormDataPage },
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
