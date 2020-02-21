import assembleToDataTable from './assembler/data_table_assembler';
import { ofFetch } from '../../functions';

export async function loadFormAnalysis(formId) {
  const response = await ofFetch(`/api/v1/cp/form/analysis/${formId}`);
  const data = await response.json();
  return data;
}

export async function loadForFormSummary(formId) {

  const formResponse = await ofFetch(`/api/v1/form/${formId}`);
  const form = await formResponse.json();

  const valueResponse = await ofFetch(`/api/v1/cp/form/${formId}/value`);
  const value = await valueResponse.json();

  const { columns, values } = assembleToDataTable(form, value);


  return {
    form: form,
    values: values,
    columns: columns,
  }
}

export async function loadForm(formId) {

  const formResponse = await ofFetch(`/api/v1/form/${formId}`);
  const form = await formResponse.json();
  return form;
}

export async function loadForFormData(formId, page=1) {

  const formResponse = await ofFetch(`/api/v1/form/${formId}`);
  const form = await formResponse.json();

  const valueResponse = await ofFetch(`/api/v1/cp/form/${formId}/value?page=${page}`);
  const value = await valueResponse.json();

  const { columns, values, paginator } = assembleToDataTable(form, value);


  return {
    form: form,
    values: values,
    columns: columns,
    paginator: paginator,
  }
}