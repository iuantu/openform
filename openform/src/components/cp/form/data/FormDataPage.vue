<template>
  <el-row type="flex" v-loading="!isFetched" justify="center">
    <data-editor
      :visible="detailVisible"
      :form="form"
      :row="selectedRow"
      :is-detail="isDetail"
      @submit="add($event)"
      @close="detailVisible = false"
    >
    </data-editor>
    <el-col>
      <el-row>
        <el-col>
          <el-button type="primary" size="mini" @click="onAddDataClick()">添加数据</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col v-if="isFetched">
          <DataTable
            v-bind:values="rows"
            v-bind:columns="columns"
            @row-click="value => { this.isDetail = true; detail(value) }"
          />
<!--
             {* :pager-count="pageSize" *} -->
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
      detailVisible: false,
      currentPage: 1,
      isDetail: false,
    }
  },

  async created() {
    // this.$store._mutations.$message = this.$message;
    // debugger;
    // console.log(this.$store.state.$message);
    this.setMessage(this.$message);

    await this.loadFormData();

    // this.detailVisible = true;
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

    onAddDataClick() {
      this.detailVisible = true;
    },

    ...mapActions('row', ['load', 'add', 'detail']),
    ...mapMutations('row', ['setMessage', 'setForm']),
  },
  computed: {
    ...mapState('row', [ 'form', 'selectedRow', 'columns', 'rows', 'perPageSize', 'pageSize', 'total' ]),
  }
    
}
</script>