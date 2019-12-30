<template>
    <el-container>
        <el-main>
            <el-table :data="values" style="width: 100%;">
                <el-table-column
                    v-for="(column, key) in columns"
                    :key="key"
                    :prop="column.property"
                    :label="column.label"
                    width="180">
                </el-table-column>
            </el-table>
        </el-main>
    </el-container>
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
        let response = await fetch(`http://localhost:5000/api/v1/form/1`);
        let data = await response.json();

        let val_res = await fetch(`http://localhost:5000/api/v1/cp/value/1`);
        let val = await val_res.json();

        this.columns = data.fields.map((column) => {
            return {
                property: new String(column.id),
                label: column.title
            }
        })

        this.values = val.data.map((v) => {
            for (const field of data.fields) {
                if (field.discriminator == "select_field") {
                    let vv = v.values[field.id];
                    for (const opt of field.options) {
                        if (opt.value == vv) {
                            v.values[field.id] = opt.label;
                            break
                        }
                    }
                }
            }
            return v.values;
        })

        // console.debug("Form summary created");
    }
}
</script>