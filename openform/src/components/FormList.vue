<template>
  <el-row type="flex" justify="center" v-loading="loading">
    <el-col :md="16">
      <el-row type="flex" class="create-button">
        <el-col>
          <el-button round size="medium">创建表单</el-button>
        </el-col>
      </el-row>
      <el-row type="flex" class="form-table">
        <el-col>
          <el-table
            :data="forms"
            style="width: 100%">
            <el-table-column
              prop="title"
              label="名字"
              width="*">
              <template slot-scope="scope">
                <router-link :to="{ name: 'cp_form_summary', params: { id: scope.row.id } }">{{scope.row.title}}</router-link>
              </template>
            </el-table-column>
            <el-table-column
              prop="form_count"
              label="数据"
              width="50">
            </el-table-column>
            <el-table-column
              width="60"
              label="状态">
              <template slot-scope="scope">
                <el-switch v-model="scope.row.published"></el-switch>
              </template>
            </el-table-column>
            <el-table-column
              prop="created_at"
              width="100"
              label="创建时间">
            </el-table-column>
            <el-table-column
              width="100"
              label="操作">
              <template slot-scope="scope">
                <i class="el-icon-delete" @click="onDeleteClick(scope.row.id)"></i>
              </template>
            </el-table-column>
          </el-table>
          <el-pagination
            background
            layout="prev, pager, next"
            :total="total"
            :current-page.sync="page">
          </el-pagination>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>
<style scoped>
.create-button {
  margin: 50px 0px 20px 0px;
}

.form-table .el-table {
  margin: 0px 0px 20px 0px;
}
</style>
<script>
import { ofFetch } from '../functions'
export default {
  data() {
    return {
      loading: true,
      forms: [],
      page_size: 0,
      page: 1,
      total: 0,
    }
  },
  async created() {
    this.load();
  },
  methods: {
    async onDeleteClick(id) {
      this.$confirm('此操作将永久删除记录， 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '删除成功!'
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });          
      });
    },

    async load() {
      this.loading = true;
      const response = await ofFetch('/api/v1/cp/form')
      const forms = await response.json()
      this.forms = forms.data.map((form) => {
        return {
          id: form.id,
          title: form.title,
          created_at: form.created_at,
          published: true,
          form_count: 10
        }
      })
      const pr = forms.page_result;
      this.total = pr.total;
      this.loading = false;
    }
  }
}
</script>