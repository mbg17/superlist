<template>
  <div>
    <h1>课程详细页面</h1>
    <div>
      <p>课程id：{{detail.course}}</p>
      <p>课程缩略图：<img :src="detail.img" alt="" style="width: 100px;height: 100px;"></p>
      <p>课程难度：{{detail.level}}</p>
      <p>课程口号：{{detail.course_slogan}}</p>
      <p>课程名称：{{detail.title}}</p>
      <p>为什么学习：{{detail.why_study}}</p>
      <span>授课老师：<p v-for='(teacher,index) in detail.teachers' :key='index'>姓名:{{teacher.name}} 级别:{{teacher.role}}</p></span>
      <div>
        <h3>章节列表</h3>
        <ul v-for=" (item,index) in detail.chapter" :key='index'>
          <li>{{ item.name }}</li>
        </ul>
      </div>
      <div>
        <h3>推荐课程</h3>
        <ul v-for=" (item,index) in detail.recommends" :key='index'>
          <li><a @click="changeDetail(item.id)">{{item.title}}</a></li>
          <!-- <li>{{item.id}}-{{item.title}}</li> -->
        </ul>
      </div>
      <div></div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        detail: {
          course: null,
          img: null,
          level: null,
          slogon: null,
          title: null,
          why: null,
          chapter: [],
          recommends: [],
          teachers:[]
        }
      }
    },
    mounted() {
      var nid = this.$route.params.id;
      this.initDetail(nid)
    },
    methods: {
      initDetail(nid) {
        var that = this
        this.$axios.request({
          url: 'http://127.0.0.1:8001/api/v1/course/' + nid + '/',
          method: 'GET'
        }).then(function(arg) {
          if (arg.data.code === 1000) {
            that.detail = arg.data.data;
          } else {
            alert(arg.data)
          }
        })
      },
      changeDetail(nid){
        console.log(nid);
        this.initDetail(nid);
        this.$router.push({name:'detail',params:{id:nid}});

      }
    }
  }
</script>

<style scoped>

</style>
