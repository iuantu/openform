<template>
  <div class="collaborator">
    <div class="header">
      <div class="title">协作</div>
      <el-button class="add" type="primary" round plain @click="addCollaborator">添加</el-button>
    </div>
    <div class="body">
      <el-table
              :data="collaboratorList"
              style="width: 100%;margin-top: 40px;"
      >
        <el-table-column prop="name" align="left" label="名字" />
        <el-table-column width="100" align="center" label="身份">
          <template slot-scope="scope">
            <span v-show="scope.row.status === 0">编辑</span>
            <span v-show="scope.row.status === 1">查看</span>
            <span v-show="scope.row.status === 2">管理</span>
          </template>
        </el-table-column>
        <el-table-column align="center" width="150" label="操作">
          <template slot-scope="scope">
            <span v-if="scope.row.ischeck" class="del-btn" @click="delCollaborator(scope.row)">移除</span>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <Add ref="add"></Add>
  </div>
</template>

<script>
  import Add from './add'
  export default {
    components: { Add },
    data() {
      return {
        collaboratorList: [
          {
            name: '协作者1',
            status: 0,
            ischeck: false, // 操作权限
          },
          {
            name: '协作者2',
            status: 1,
            ischeck: true, // 操作权限
          },
          {
            name: '协作者3',
            status: 2,
            ischeck: true, // 操作权限
          }
        ]
      }
    },
    methods: {
      addCollaborator() {
        this.$refs.add.show()
      },
      delCollaborator(/*row*/) {
        this.$confirm('此操作将永久删除记录， 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.close()
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

<style lang="scss" scoped>
.collaborator {
  margin-top: 40px;
  min-height: 390px;
  padding: 20px 40px;
  border: 1px solid #f0f0f0;
  box-shadow: 0 1px 8px #f3f3f3;
  .header {
    display: flex;
    justify-content: space-between;
  }
  .title {
    font-size: 22px;
    margin-left: -20px;
  }
  .add {
    font-size: 16px;
  }
  .del-btn {
    cursor: pointer;
    color: #780000;
  }
}
</style>
