import Vue from 'vue'
import Router from 'vue-router'
import FormSummary from './../components/FormSummary'
import FormData from './../components/FormData'
import FormList from './../components/FormList'
import FormControlPanel from './../components/FormControlPanel'
import Register from '../components/Register'

import OpenFormSetting from './../components/openform/openForm'
import Login from './../components/Login'
import OpenForm from './../pages/openform/openForm'

import OpenFormView from '../pages/openformView/openformView'
import DataForm from '../components/dataForm/DataForm'
import ReportForm from '../components/reportForm/ReportForm'
import Collaborator from '../components/Collaborator/collaborator'
import Publish from '../components/Publish'

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
    },{
      path: '/openFormView',
      name: 'OpenFormView',
      component: OpenFormView,
      children: [
        { path: '/form/:id/', name: "cp_form_summary", component: FormSummary},
        { path: '/dataForm', name: "DataForm", component: DataForm},
        { path: '/reportForm', name: "ReportForm", component: ReportForm},
        { path: '/publish', name: "Publish", component: Publish},
        { path: '/collaborator', name: "Collaborator", component: Collaborator},
      ]
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
        { path: 'form/', name: 'cp_form_list', component: FormList},
        { path: 'form/:id/', name: "cp_form_summary", component: FormSummary},
        { path: 'data', name: "cp_form_data", component: FormData},
        { path: 'summary', name: "cp_form_summary", component: FormSummary},
      ]
    },
  ]
})
