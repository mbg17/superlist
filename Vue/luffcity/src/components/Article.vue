<template>
  <div>
    <div>{{news.title}}</div>
    <p>{{news.content}}</p>
    <p>{{news.date}} 阅读数：{{news.view_num}} 评论数：{{news.comment_num}} 收藏数：{{news.collect_num}} </p>
    <p>--评论区--</p>
    <div v-for="(row,index) in news.comment" :key='index'>
      <p>{{row.account}} {{row.content}}</p>
      <p>反对：{{row.disagree_number}} 赞同：{{row.agree_number}}</p>
      <div v-if='row.son_comment.length>0'>
        <p>子评论</p>
        <div v-for="(row,index) in row.son_comment" :key='index'>
          <p>{{row.account}} {{row.content}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "newsdetail",
    data() {
      return {
        newdetail: [],
        nid:this.$route.params.newid
      }
    },
    mounted: function() {
      this.initNewDetail(this.nid)
    },
    methods: {
      initNewDetail(nid) {
        var that = this;
        this.$axios.request({
          url: 'http://127.0.0.1:8001/api/v1/article/' + nid + '/',
          method: 'GET'
        }).then(function(arg) {
          if (arg.data.code === 1000) {
            that.newdetail = arg.data.data;
            console.log(arg.data);
          } else {
            alert(arg.data)
          }
        }).catch(function(ret) {
          console.log(ret);
        })
      }
    },
    computed: {
      news: function() {
        // this.initNewDetail(this.nid);
        // `this` 指向 vm 实例
        return this.newdetail;
      }
    }
  }
</script>

<style>
</style>
