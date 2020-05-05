<template>
  <el-row type="flex" v-loading="!isFetched" justify="center">
    <data-editor
      :visible="dialogVisible"
      :form="form"
      :row="selectedRow"
      :is-detail="isDetail"
      @submit="add($event)"
      @close="hidedAddDialog()"
    >
    </data-editor>
    <el-col>
      <el-row>
        <el-col>
          <el-button type="primary" size="mini" @click="showAddDialog()">添加数据</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col v-if="isFetched">
          <DataTable
            v-bind:values="rows"
            v-bind:columns="columns"
            @row-click="value => { detail(value) }"
          />
          <el-pagination background
            :page-size="perPageSize"
            :page-count="pageSize"
            layout="prev, pager, next" :total="total" @current-change="pageChanged"
            :current-page.sync="currentPage">
          </el-pagination>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>
<script>
import DataTable from '../DataTable'
import DataEditor from "./FormDataEditor";
import { mapActions, mapMutations, mapState } from 'vuex'

export default {
  data() {
    return {
      id: 0,
      isFetched: false,
      currentPage: 1,
    }
  },

  async created() {
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

      await this.load({ formId: this.id, page: 1 });

      this.isFetched = true;
    },

    async pageChanged() {
      await this.loadFormData();
    },

    ...mapActions('row', ['load', 'add', 'detail']),
    ...mapMutations('row', ['setMessage', 'setForm', 'showAddDialog', 'hidedAddDialog']),
  },
  computed: {
    ...mapState('row', [ 'form', 'selectedRow', 'columns', 'rows', 'perPageSize', 'pageSize', 'total', 'dialogVisible',
      'isDetail'
    ]),
  }
    
}
</script>