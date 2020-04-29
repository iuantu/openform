import moment from 'moment';





function assembleToDataTableValues(values, fields) {
  return values.map((v) => {
    const row = {};
    for (const field of fields) {
      const fieldValue = v.values[field.id];
      
      row[field.id] = formatValue(field, fieldValue)
      row.sequence = v.sequence;
      row.created_at = moment(v.created_at).format('YYYY-MM-DD HH:mm');
      row.updated_at = moment(v.updated_at).format('YYYY-MM-DD HH:mm');
    }
    return row;
  });
}

export default function assembleToDataTable(form, values, optionColumns = null) {

  return {
    columns: assembleToDataTableColumns(form),
    values: assembleToDataTableValues(values.data, form.fields),
    paginator: values.page_result,
  }
}