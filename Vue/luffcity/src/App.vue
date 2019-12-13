<template>
  <div id="app">

    <router-link to="/index">首页</router-link>
    <router-link to="/course">课程</router-link>
    <router-link to="/micro">微职位</router-link>
    <router-link to="/news">深科技</router-link>
    <div v-if="this.$store.state.token">{{this.$store.state.username}}
    <button @click="logout">注销</button>
    </div>
    <div v-else>
      <router-link to="/login">登录</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
  export default {
    name: 'App',
    methods:{
      logout(){
        this.$store.dispatch('logout');
      }
    }
  }
</script>

<style>

</style>
