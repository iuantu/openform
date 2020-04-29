import RowAssembler from "./RowAssembler";
import ValueHTTP from "../../api/value";
import { getMeta } from "../../components/fields";
import {FormModelAssembler} from "../../components/ModelApater";
import FormHTTP from "../../api/form";

const valueHTTP = new ValueHTTP();
const formHTTP = new FormHTTP();
const assembler = new RowAssembler();

const state = {
  $message: null,
  page: 1,
  currentPage: 1,
  pageSize: 1,
  perPageSize: 50,
  total: 50,
  form: null,
}

const getters = {}

const actions = {
  async load({ commit }, { formId, page }) {
    const assembler2 = new FormModelAssembler();

    const value = await valueHTTP.fetch(formId, page);
    const form = assembler2.toViewModel((await formHTTP.fetchOne(formId)));
    const rows = assembler.assembleToDataTableRows(value.data, form.fields);
    const columns = assembler.assembleToDataTableColumns(form);


    commit('formDataLoaded', { form, rows, columns, paginator: value.page_result})
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

    try {
      const value = await valueHTTP.add(form.formId, request);
    } catch (e) {
      const exceptions = { valueError: e, form };
      commit('throwExceptionFromSubmit', exceptions);
    }
    commit("onAdded");
    // commit("message", "hello", { root: true});
    dispatch('refresh', state.page);
  }
};

const mutations = {
  formDataLoaded(state, { form, rows, columns, paginator }) {
    state.form = form;
    state.rows = rows;
    state.columns = columns;

    state.perPageSize = paginator.per_page_size;
    state.pageSize = paginator.page_size;
    state.total = paginator.total;
  },

  setForm(state, form) {

    state.form = assembler.toViewModel(form);
  },

  throwExceptionFromSubmit(state, { valueError, form }) {
    const fields = {};
    form.fields.forEach((field) => {
      field.has_error = true;
      field.errors = [];
      fields[field.id] = field;
    });

    valueError.errors.forEach((error) => {
      const field = fields[error.name];
      field.errors.push(error.description);
    });
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