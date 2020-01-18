<template>
  <div class="publish">
    <div class="form-url">
      <div class="publish-title">表单地址</div>
      <div class="form-url-input">
        <el-input :value="formUrl" disabled></el-input>
        <el-button class="open-link" type="primary" @click="openLink">打开网址</el-button>
      </div>
    </div>
    <div class="form-share">
      <div class="publish-title">分享</div>
      <div class="form-share-info">
        <div class="form-share-info--img"><img :src="shareInfo.imgUrl" alt=""></div>
        <div class="form-share-info--txt">
          <div class="label">{{ shareInfo.title }}</div>
          <div>{{ shareInfo.describe }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        formUrl: 'http://www.baidu.com',
        shareInfo: {
          title: '标题',
          describe: '描述',
          imgUrl: 'https://dss0.baidu.com/73F1bjeh1BF3odCf/it/u=1519004667,78780781&fm=85&s=F23BE16CAEE5977600537F830300E08C'
        }
      }
    },
    methods: {
      openLink() {
        window.open(this.formUrl)
      }
    }
  }
</script>

<style lang="scss" scoped>
.publish {
  margin-top: 40px;
  height: 390px;
  border: 1px solid #f0f0f0;
  box-shadow: 0 1px 8px #f3f3f3;
  &-title {
    font-size: 22px;
    line-height: 22px;
    margin-bottom: 12px;
  }
  .form-url {
    padding: 25px;
    border-bottom: 1px solid #f0f0f0;
    &-input {
      width: 520px;
      display: flex;
      .open-link {
        margin-left: 15px;
      }
    }
  }
  .form-share {
    padding: 25px;
    &-info {
      display: flex;
      &--img {
        width: 200px;
        height: 120px;
        margin-right: 30px;
        img {
          width: 100%;
          height: 100%;
          object-fit: cover;
        }
      }
      &--txt {
        font-size: 20px;
        .label {
          margin-bottom: 17px;
        }
      }
    }
  }
}
</style>
