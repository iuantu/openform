<template>
  <el-row type="flex" v-loading="!isFetched" justify="center">
    <data-editor
      :visible="detailVisible"
      :form_id="$route.params.id"
      :id="0"
      @submit="add($event)"
    >
    </data-editor>
    <el-col>
      <el-row>
        <el-col>
          <el-button type="primary" size="mini">添加数据</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col v-if="isFetched">
          <DataTable
            v-bind:values="values"
            v-bind:columns="columns"
          />

          <el-pagination background
            :page-size="perPageSize" :pager-count="pageSize"
            layout="prev, pager, next" :total="total" @current-change="pageChanged"
            :current-page.sync="currentPage">
          </el-pagination>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>
<script>
import DataTable from './DataTable'
import DataEditor from "./FormDataEditor";
import { loadValues } from './service/form'
import { mapActions, mapMutations } from 'vuex'

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
      detailVisible: true,
    }
  },

  async created() {
    // this.$store._mutations.$message = this.$message;
    // debugger;
    // console.log(this.$store.state.$message);
    this.setMessage(this.$message);

    await this.loadFormData();
  },

  components: {
    DataTable,
    DataEditor,
  },

  methods: {
    async loadFormData() {
      this.id = this.$route.params.id;
      this.isFetched = false;

      const { form, values, columns, paginator } = await loadValues(
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
      await this.loadFormData();
    },

    ...mapActions('row', ['add']),
    ...mapMutations('row', ['setMessage']),
  }
    
}
</script>