<template>
  <div class="open-form-data">
    <el-button-group style="margin-top: 43px;margin-bottom: 43px;">
      <el-button plain>复制</el-button>
      <el-button plain>刷新</el-button>
      <el-button plain>导出</el-button>
      <el-button plain @click="deleteHandle">删除</el-button>
    </el-button-group>
    <div class="table">
      <el-table
              :data="tableData"
              style="width: 100%"
              @row-click="rowClick"
              @select="selectHandle"
              @select-all="selectHandle"
      >
        <el-table-column
                type="selection"
                width="55">
        </el-table-column>
        <el-table-column prop="name" align="left" label="Name" />
        <el-table-column prop="country" align="left" label="Country" />
        <el-table-column prop="status" align="left" label="Status" />
        <el-table-column prop="birthday" align="left" label="Birthday" />
        <el-table-column prop="ZipCode" align="left" label="Zip Code" />
      </el-table>
    </div>
    <form-data-details ref="details" :detailsId="detailsId" />
  </div>
</template>

<script>
  import FormDataDetails from './FormDataDetails'
  export default {
    components: {FormDataDetails},
    data() {
      return {
        tableData: [
          {
            id: 1,
            name: 'name1',
            country: 'country',
            status: 'status',
            birthday: 'birthday',
            ZipCode: 'ZipCode',
          },
          {
            id: 2,
            name: 'name2',
            country: 'country',
            status: 'status',
            birthday: 'birthday',
            ZipCode: 'ZipCode',
          },
          {
            id: 3,
            name: 'name3',
            country: 'country',
            status: 'status',
            birthday: 'birthday',
            ZipCode: 'ZipCode',
          },
        ],
        detailsId: 0
      }
    },
    methods: {
      rowClick(row) {
        this.detailsId = row.id
        this.$refs.details.show()
      },
      selectHandle(selection) {
        alert(JSON.stringify(selection))
      },
      deleteHandle() {
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
      }
    }
  }
</script>

<style scoped>

</style>
