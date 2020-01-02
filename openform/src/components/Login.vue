<template>
  <el-row type="flex" justify="center">
    <el-col :md="12" class="box login-box">
      <el-row type="flex" justify="center">
        <el-col :md="20">
          <el-row>
            <el-col><h2>登录Open Form</h2></el-col>
            <el-col>
              <el-form ref="loginForm" :model="login" :rules="constraints" label-width="0px">
                <el-form-item prop="username">
                  <el-input class="form-field" v-model="login.username" placeholder="请输入电子邮件、用户名或手机号码"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                  <el-input class="form-field" v-model="login.password" placeholder="请输入你的密码"></el-input>
                </el-form-item>
                <el-button class="form-field" type="primary" round @click="onLoginFormSubmit('loginForm')">登录</el-button>
              </el-form>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-row>
            <el-col :offset="2">
              <div class="bottom">
                <span>首次使用OpenForm吗？</span>
                <a href="">现在注册</a>
              </div>
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
  margin: 15px 0px 15px 0px;
}

.box {
  box-shadow: 0px 1px 8px 0px #F2F2F2;
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
    return {
      login: {
        username: 'cj',
        password: '111111',
      },
      constraints: {
        username: [
          { required: true, trigger: 'blur', message: '请输入电子邮件、用户名或手机号码'},
          { min: 2, max: 50, trigger: 'blur', message: '电子邮件、用户名或手机号码长度在2到50个字符之间' }
        ],
        password: [
          { required: true, trigger: 'blur', message: '请输入电子邮件、用户名或手机号码'},
          { min: 2, max: 50, trigger: 'blur', message: '密码长度在2到50个字符之间' }
        ]
      }
    }
  },
  methods: {
    onLoginFormSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.service.login(this.login.username, this.login.password)
          .then((uiLogin) => {
            if (!uiLogin.isSuccess) {
              this.$message(uiLogin.message);
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