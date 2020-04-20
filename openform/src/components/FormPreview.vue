<template>
  <el-row type="flex" class="form-preview">
    <el-col>
      <el-row justify="center">
        <el-col class="devices">
          <el-radio-group size="small" v-model="device">
            <el-radio-button label="computer">浏览器</el-radio-button>
            <el-radio-button label="mobile">手机</el-radio-button>
          </el-radio-group>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <div :class="{ smartphone: device == 'mobile' }">
            <div class="preview-content">
              <h1>{{form.title}}</h1>
              <div class="form-description" v-html="form.description"></div>
              <form-fields :fields="fields"></form-fields>
            </div>
          </div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import FormFields from "./FormFields";
export default {

  props: {
    id: {
      type: Number,
      default: 0
    },
    form: {
      type: Object
    },
    fields: {

    }
  },
  data() {
    return {
        device: 'computer'
    };
  },
  components: {
    FormFields
  },
  methods: {
    onComponentChange() {
    }
  }
};
</script>

<style lang="scss">
.devices {
  text-align: center;
  margin: 40px 0;
}

.preview-content {
  padding: 30px;
}

.form-description {
  margin: 30px 0;
}

/* The device with borders */
.smartphone {
  position: relative;
  width: 360px;
  height: 640px;
  margin: auto;
  top: 20px;
  border: 16px #ccc solid;
  border-top-width: 60px;
  border-bottom-width: 60px;
  border-radius: 36px;
}

/* The horizontal line on the top of the device */
.smartphone:before {
  content: '';
  display: block;
  width: 60px;
  height: 5px;
  position: absolute;
  top: -30px;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #efefef;
  border-radius: 10px;
}

/* The circle on the bottom of the device */
.smartphone:after {
  content: '';
  display: block;
  width: 35px;
  height: 35px;
  position: absolute;
  left: 50%;
  bottom: -65px;
  transform: translate(-50%, -50%);
  background: #efefef;
  border-radius: 50%;
}

/* The screen (or content) of the device */
.smartphone .content {
  width: 360px;
  height: 640px;
  background: white;
}


</style>
