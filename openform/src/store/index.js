import Vue from "vue";
import Vuex from 'vuex';
import row from "./modules/row";

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    row
  },
  strict: debug
})