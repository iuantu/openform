import Vue from 'vue'
import Router from 'vue-router'
import OpenForm from './../pages/openform/openForm'
import FormSummary from './../components/FormSummary'
import OpenFormView from './../pages/openformView/openformView'


import FormList from './../components/FormList'
import ControlPanel from './../components/ControlPanel'

import OpenFormSetting from './../components/openform/openForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'OpenFormView',
      component: OpenFormView,
      children: [
        { path: '/form/:id/', name: "cp_form_summary", component: FormSummary},
        { path: '/', component: FormList},
      ]
    },{
      path: '/openform',
      name: 'OpenForm',
      component: OpenForm,
      children: [
        { path: '/', component: OpenFormSetting},
      ]
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
