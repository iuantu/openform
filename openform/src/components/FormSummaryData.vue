<template>
  <el-row>
    <el-col>
      <DataTable v-bind:values="values" v-bind:columns="columns" />
    </el-col>
  </el-row>
</template>
<script>
import DataTable from './DataTable'
import { loadForFormSummary } from './service/form'

export default {
  props: {
    id: {
      type: Number,
      default: 1,
    }
  },
  components: {
    DataTable
  },

  data() {
    return {
      values: [],
      columns: [],
    }
  },

  async created() {
    const { form, values, columns } = await loadForFormSummary(this.id);
    this.form = form;
    this.values = values;
    this.columns = columns;
  },
}
</script>