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
  valueId: null,
  selectedRow: null,
  dialogVisible: false,
  isDetail: true,
}

const getters = {}

const actions = {
  async load({ commit, dispatch }, { formId, page }) {
    const assembler2 = new FormModelAssembler();

    const value = await valueHTTP.fetch(formId, page);
    const form = assembler2.toViewModel((await formHTTP.fetchOne(formId)));
    const rows = assembler.assembleToDataTableRows(value.data, form.fields);
    const columns = assembler.assembleToDataTableColumns(form);
    commit('formDataLoaded', { form, rows, columns, paginator: value.page_result})
    // dispatch('detail', rows[0]);
  },

  refresh({dispatch}, page) {
    if (page === 1) {
      dispatch('load', page);
    }
  },

  async add({ state, dispatch, commit }, form) {
    const request = { fields: {} };
    form.fields.forEach((field) => {
      const meta = getMeta(field.discriminator);
      request.fields[field.id] = meta.assembler.toFormValueForRequest(field);
    });

    try {
      if (state.valueId > 0) {
        const value = await valueHTTP.update(form.formId, state.valueId, request);
        console.log(value);
      } else {
        const value = await valueHTTP.add(form.formId, request);
        console.log(value);
      }
    } catch (e) {
      const exceptions = { valueError: e, form };
      commit('throwExceptionFromSubmit', exceptions);
    }
    commit("onAdded");
    // commit("message", "hello", { root: true});
    dispatch('refresh', state.page);
  },

  async detail({commit}, value) {
    commit('showEditDialog', value);
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

    // state.selectedRow = rows[0];
    // state.isDetail = true;
    // state.dialogVisible = true;
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

  showAddDialog(state) {
    console.log('show add dialog');
    state.selectedRow = null;
    state.isDetail = false;
    state.dialogVisible = true;
  },

  showEditDialog(state, value) {
    state.form.fields.forEach((field) => {
      field.value = value[field.id];
    });

    state.selectedRow = value;
    state.isDetail = true;
    state.dialogVisible = true;
    state.valueId = value.id;
    console.log(state.isDetail)
  },

  hidedAddDialog(state) {
    state.selectedRow = null;
    state.isDetail = true;
    state.dialogVisible = false;
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