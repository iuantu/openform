import { loadValues } from "../../components/service/form";
import RowAssembler from "./RowAssembler";
import ValueHTTP from "../../api/value";
import { getMeta } from "../../components/fields";

const valueHTTP = new ValueHTTP();
const assembler = new RowAssembler();

const state = {
  $message: null,
  page: 1,
}

const getters = {}

const actions = {
  async load({ commit }, page) {
    let rows = [];

    commit('setRows', rows)
  },

  refresh({dispatch}, page) {
    if (page === 1) {
      dispatch('load', page);
    }
  },

  async add({ state, dispatch, commit }, form) {
    // const request = assembler.viewToRequest(form)
    const request = { fields: {} };
    form.fields.forEach((field) => {
      const meta = getMeta(field.discriminator);
      request.fields[field.id] = meta.assembler.toFormValueForRequest(field);
    });

    const response = await valueHTTP.add(form.formId, request);
    commit("onAdded");
    commit("message", "hello", { root: true});
    dispatch('refresh', state.page);
  }
};

const mutations = {
  setRows(state, rows) {

  },
  onAdded(state, value) {
    state.message("hello");
  },
  setMessage(state, message) {
    state.message = message;
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}