<template>
  <el-row type="flex" justify="center">
    <el-col :md="12" class="box login-box">
      <el-row type="flex" justify="center">
        <el-col :md="20">
          <el-row>
            <el-col><h2>注册Open Form</h2></el-col>
            <el-col>
              <el-form ref="registerForm" :model="registration" :rules="constraints" label-width="0px" class="register-form">
                <el-form-item prop="username">
                  <label>用户名</label>
                  <el-input class="form-field" v-model="registration.username" placeholder="请输入用户名"></el-input>
                </el-form-item>
                <el-form-item prop="email">
                  <label>电子邮件</label>
                  <el-input class="form-field" v-model="registration.email" placeholder="请输入电子邮件"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                  <label>密码</label>
                  <el-input class="form-field" v-model="registration.password" placeholder="请输入你的密码"></el-input>
                </el-form-item>
                <el-form-item prop="passwordConfirm">
                  <label>再次输入密码</label>
                  <el-input class="form-field" v-model="registration.passwordConfirm" placeholder="请再次输入你的密码"></el-input>
                </el-form-item>
                <el-button class="form-field" type="primary" round @click="onRegisterFormSubmit('registerForm')">注册</el-button>
              </el-form>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>
<style scoped>
h2 {
  font-size: 18px;
  margin-top: 35px;
  margin-bottom: 25px;
}

.form-field {
  margin: 0px 0px 0px 0px;
}

.box {
  box-shadow: 0px 1px 8px 0px #F2F2F2;
}

.register-form {
  margin-bottom: 50px;
}

.login-box {
  margin-top: 100px;
}

.bottom {
  background-color: #FCFCFC;
  height: 66px;
  line-height: 66px;
}

.el-form-item__content {
  margin-left: 0px;
}
</style>
<script>
import { SecurityService } from '../functions';

export default {
  data() {
    const emailValidator = (rule, email, callback) => {
      
      var re = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;
      if (!re.test(String(email).toLowerCase())) {
        callback(new Error('EMail地址不正确'));
      } else {
        callback();
      }
    };

    const passwordConfirmValidator = (rule, passwordConfirm, callback) => {
      if (this.registration.password != passwordConfirm) {
        callback(new Error('两次密码输入不一致'));
      } else {
        callback()
      }
    }

    return {
      registration: {
        username: '',
        email: '',
        password: '',
      },
      constraints: {
        username: [
          { required: true, trigger: 'blur', message: '请输入用户名'},
          { min: 2, max: 50, trigger: 'blur', message: '用户名长度在2到50个字符之间' }
        ],
        email: [
          { required: true, trigger: 'blur', message: '请输入电子邮件地址'},
          { validator: emailValidator, trigger: 'blur' },
        ],
        password: [
          { required: true, trigger: 'blur', message: '请输入密码'},
          { min: 2, max: 50, trigger: 'blur', message: '密码长度在2到50个字符之间' },
        ],
        passwordConfirm: [
          { required: true, trigger: 'blur', message: '请输入密码'},
          { min: 2, max: 50, trigger: 'blur', message: '密码长度在2到50个字符之间' },
          { validator: passwordConfirmValidator, trigger: 'blur' },
        ]
      }
    }
  },
  methods: {
    onRegisterFormSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.service.register(this.registration.username, this.registration.email, this.registration.password)
          .then((uiRegister) => {
            if (!uiRegister.isSuccess) {
              this.$message(uiRegister.message);
            } else {
              this.$router.replace({name: "cp_form_list"});
            }
          })
        } else {
          return false;
        }
      });
    }
  },

  created() {
    this.service = new SecurityService();
  }
}
</script>