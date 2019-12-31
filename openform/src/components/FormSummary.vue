<template>
    <el-table :data="values" style="width: 100%;">
        <el-table-column
            v-for="(column, key) in columns"
            :key="key"
            :prop="column.property"
            :label="column.label"
            width="180">
            <template slot-scope="scope">
                <div v-if="!Array.isArray(scope.row[scope.column.property])">{{scope.row[scope.column.property]}}</div>
                <div v-if="Array.isArray(scope.row[scope.column.property])">
                    <ul>
                        <li v-for="(value, key) in scope.row[scope.column.property]" :key="key">{{value}}</li>
                    </ul>
                </div>
            </template>
        </el-table-column>
    </el-table>
</template>
<script>
export default {
    data() {
        return {
            "values": [],
            "columns": [],
        }
    },
    async created() {
        let response = await fetch(`http://localhost:5000/api/v1/form/${this.$route.params.id}`);
        let data = await response.json();

        let val_res = await fetch(`http://localhost:5000/api/v1/cp/value/${this.$route.params.id}`);
        let val = await val_res.json();

        this.columns = data.fields.map((column) => {
            return {
                property: new String(column.id),
                label: column.title,
                width: "*",
            }
        })

        const fieldsMapping = {}
        data.fields.forEach((field) => {
            fieldsMapping[field.id] = field;
        })

        this.values = val.data.map((v) => {
            const row = {};
            for (const field of data.fields) {
                const fieldValue = v.values[field.id];
                // const field = fieldsMapping[fieldValue.field_id];
                
                row[field.id] = this.fieldValue(field, fieldValue)
            }
            return row;
        })

        console.debug("Form summary created");
    },

    methods: {
        fieldValue(field, fieldValue) {
            if (field.discriminator == "text_field") {
                return fieldValue;
            }

            if (field.discriminator == 'select_field') {
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

            return fieldValue
        }
    }
    
}
</script>