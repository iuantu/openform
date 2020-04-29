import moment from "moment";

export default class RowAssembler {

  _formatValue(field, fieldValue) {
    if (field.discriminator === "text_field") {
      return fieldValue;
    }

    if (field.discriminator === 'select_field') {
      const options = {};
      for (const opt of field.options) {
        options[opt.value] = opt;
      }
      if (fieldValue) {
        return fieldValue.map((optValue) => {
          const opt = options[optValue.value];
          if (opt.editable) {
            const text = optValue.text || '无'
            return `${opt.label} ${text}`;
          }
          return opt.label;
        });
      }
    }

    return fieldValue;
  }

  assembleToDataTableRows(values, fields) {
    return values.map((v) => {
      const row = {};
      for (const field of fields) {
        const fieldValue = v.values[field.id];

        row[field.id] = this._formatValue(field, fieldValue)
        row.sequence = v.sequence;
        row.created_at = moment(v.created_at).format('YYYY-MM-DD HH:mm');
        row.updated_at = moment(v.updated_at).format('YYYY-MM-DD HH:mm');
      }
      return row;
    });
  }

  assembleToDataTableColumns(form) {
    const valueColumns = form.fields.map((column) => {
      return {
        property: String(column.id),
        label: column.title,
        width: "*",
      }
    });

    const sequenceColumns = [
      {
        property: 'sequence',
        label: '序号',
        width: '50',
      },
    ];

    const datetimeColumns = [
      {
        property: 'created_at',
        label: '创建时间',
        width: '100',
      },
      {
        property: 'updated_at',
        label: '更新时间',
        width: '100',
      },
    ];

    return [...sequenceColumns, ...valueColumns, ...datetimeColumns];
  }

  viewToRequest(view) {

  }
}