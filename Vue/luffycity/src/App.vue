<template>
  <div id="app">

    <router-link to="/index">首页</router-link>
    <router-link to="/course">课程</router-link>
    <router-link to="/micro">微职位</router-link>
    <router-link to="/news">深科技</router-link>
    <router-link to="/login">登录</router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
