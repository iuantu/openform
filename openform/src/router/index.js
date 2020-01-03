import Vue from 'vue'
import Router from 'vue-router'
// import OpenForm from './../pages/openform/openForm'
import FormSummary from './../components/FormSummary'


import FormList from './../components/FormList'
import ControlPanel from './../components/ControlPanel'
import Register from '../components/Register'
import Login from '../components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'OpenForm',
    //   component: OpenForm
    // },
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
      path: '/cp', component: ControlPanel,
      children: [
        { path: 'form/', name: 'cp_form_list', component: FormList},
        { path: 'form/:id/', name: "cp_form_summary", component: FormSummary},
        
      ]
    },
  ]
})
