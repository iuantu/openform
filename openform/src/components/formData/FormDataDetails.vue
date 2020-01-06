<template>
  <el-dialog
          width="80%"
          :visible.sync="showDialog"
          @open="getData"
          @closed="closed"
          @close="close"
  >
    <el-row style="margin: 0 20px;">
      <el-col :span="16">
        <div class="title">数据</div>
        <div v-for="(item, index) in formData" :key="index" class="form-item">
          <div class="form-item-title">
            {{ item.title }}
          </div>
          <div class="form-item-list">
            <div v-for="(subItem, subIndex) in item.list" :key="subIndex"  class="form-list-item">
              {{ subItem }}
            </div>
          </div>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="title">基本信息</div>
        <div>
          <span class="info-label">序号：</span>
          <span>1</span>
        </div>
        <div>
          <span class="info-label">提交人：</span>
          <span>1</span>
        </div>
        <div>
          <span class="info-label">填写设备：</span>
          <span>1</span>
        </div>
      </el-col>
    </el-row>
    <el-button-group class="next-prev">
      <el-button size="mini" icon="el-icon-arrow-left"></el-button>
      <el-button size="mini" icon="el-icon-arrow-right"></el-button>
    </el-button-group>
    <span slot="footer" class="dialog-footer">
      <el-button type="primary" @click="changHandle">修 改</el-button>
      <el-button type="danger" @click="deleteHandle">删除</el-button>
    </span>
  </el-dialog>
</template>

<script>
  export default {
    props: {
      detailsId: {
        type: Number,
        default: 0
      }
    },
    data() {
      return {
        showDialog: false,
        formData: [
          {
            title: '标题1',
            list: [
              '答案一',
              '答案二'
            ]
          },
          {
            title: '标题2',
            list: [
              '答案一',
              '答案二'
            ]
          },
        ]
      }
    },
    methods: {
      show() {
        this.showDialog = true
      },
      closed() {
      },
      close() {
        this.showDialog = false
      },
      getData() {

      },
      changHandle() {

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
  .next-prev {
    position: absolute;
    bottom: 20px;
    left: 20px;
  }
.title {
  font-size: 16px;
  margin-bottom: 20px;
}
.info-label {
  width: 80px;
  display: inline-block;
  margin-bottom: 8px;
}
.form-item {
  margin-bottom: 12px;
  &-title {
    font-size: 14px;
    color: #1a1a1a;
    margin-bottom: 8px;
  }
  &-list {
    font-size: 14px;
    color: #494949;
    line-height: 1.5;
  }
}
</style>
