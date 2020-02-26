<template>
  <el-row type="flex" v-loading="!isFetched" justify="center">
    <el-col v-if="isFetched">
      <DataTable v-bind:values="values" v-bind:columns="columns" />
      <el-pagination background
        :page-size="perPageSize" :pager-count="pageSize"
        layout="prev, pager, next" :total="total" @current-change="pageChanged" 
        :current-page.sync="currentPage">
      </el-pagination>
    </el-col>
  </el-row>
</template>
<script>
import DataTable from './DataTable'
import { loadForFormData } from './service/form'

export default {
  data() {
    return {
      id: 0,
      form: null,
      values: [],
      columns: [],
      isFetched: false,
      currentPage: 1,
      perPageSize: 0,
      pageSize: 0,
      total: 0,
    }
  },

  async created() {
    await this.loadFormData();
  },

  components: {
    DataTable: DataTable
  },

  methods: {
    async loadFormData() {
      this.id = this.$route.params.id;
      this.isFetched = false;

      const { form, values, columns, paginator } = await loadForFormData(
        this.id, this.currentPage
      );
      this.form = form;
      this.values = values;
      this.columns = columns;

      this.perPageSize = paginator.per_page_size;
      this.pageSize = paginator.page_size;
      this.total = paginator.total;

      this.isFetched = true;
    },

    async pageChanged() {
      this.loadFormData();
    }
  }
    
}
</script>