<template>
  <div>
    <h1>深科技</h1>
    <div v-for="(row,index) in articleList" :key='index'>
      <div style="clear:left;">
        <img :src="row.head_img" style="width: 350px;height: :350px;float: left;"/>
        <h3><router-link :to="{name:'newsdetail',params:{newid:row.id}}">{{row.title}}</router-link></h3>
        <p>{{row.brief}}</p>
        <p>#{{row.article_type_choices}}#   阅读数：{{row.view_num}}   评论数：{{row.comment_num}}      收藏数：{{row.collect_num}}   </p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        articleList: []
      }
    },
    mounted: function() {
      this.initArticle();
    },
    methods: {
      initArticle: function() {
        /*
        this.courseList = [
          {id:1,title:'Python全栈'},
          {id:2,title:'Linux运维'},
          {id:3,title:'金融分析'},
        ]
        */
        // 通过ajax向接口发送请求，并获取课程列表
        // axios 发送ajax请求
        // npm install axios --save
        // 第一步：在main.js中配置
        // 第二步：使用axios发送请求
        var that = this;
        this.$axios.request({
          url: 'http://127.0.0.1:8001/api/v1/article/',
          method: "GET"
        }).then(function(ret) {
          // ajax请求发送成功后，获取的响应内容
          if (ret.data.code === 1000) {
            that.articleList = ret.data.data;
            console.log(that.articleList)
          }
        }).catch(function(ret) {
          // ajax请求失败之后，获取响应的内容
          console.log(ret);
        })
      }
    }
  }
</script>

<style scoped>

</style>
