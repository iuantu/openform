<template>
  <el-row>
    <el-col>
      <div>
        <el-form :inline="true">
          <el-form-item>
            <el-input id="url" v-model="formURL" style="width: 350px;"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button @click="copy">复制地址</el-button>
            <a :href="formURL" target="_blank"><el-button>打开</el-button></a>
          </el-form-item>
        </el-form>
      </div>
    </el-col>
  </el-row>
</template>
<style scoped>
</style>
<script>
export default {
  props: {
    id: {
      type: Number,
      default: -1
    },
  },
  computed: {
    formURL() {
      const formURL = [document.location.protocol, "//", document.location.hostname];
      if (document.location.port != 80) {
        formURL.push(':');
        formURL.push(document.location.port);
      }
      formURL.push("/form/");
      formURL.push(this.id);

      return formURL.join("");
    }
  },
  methods: {
    copy() {
      let testingCodeToCopy = document.querySelector('#url')
      // testingCodeToCopy.setAttribute('type', 'text')    // 不是 hidden 才能複製
      testingCodeToCopy.select()

      try {
        document.execCommand('copy');
      } catch (err) {
        alert('Oops, unable to copy');
      }
      window.getSelection().removeAllRanges()
    }
  }
}
</script>