<template>
  <div v-if="!this.$store.state.token">
    <p><label for="username">用户</label><input id='username' type="text" v-model="username"></p>
    <p><label for="password">密码</label><input id='password' type="text" v-model="password"></p>
    <p><input type="button" value="登录" @click="Login"></p>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        username:'',
        password:''
      }
    },
    mounted:function () {
      // vue页面刚加载时自动执行
      // this.Login()
    },
    methods:{
      Login:function () {
        var that = this;
        this.$axios.request({
          url:'http://127.0.0.1:8001/api/v1/auth/',
          method:"POST",
          data:{username:this.username,password:this.password},
          headers:{
            'Content-Type':'application/json'
          }
        }).then(function (ret) {
          // ajax请求发送成功后，获取的响应内容
          if(ret.data.code===1000){
            var value = {username:that.username,token:ret.data.token};
            that.$store.dispatch('login',value);
            // 获取路由守卫的query对象中的属性值
            var url =that.$route.query.redirect;
            if(url){
             // 跳转url
              that.$router.push({path:url});
            }else{
              that.$router.push({path:'/index'});
            }
          }else{
            console.log(that.$store.state.username)
          }
        }).catch(function (ret) {
          // ajax请求失败之后，获取响应的内容
           console.log(ret);
        })
      }
    }
  }
</script>

<style scoped>

</style>
