<template>
  <div>
    <h1>课程详细页面</h1>
    <div>
      <p>{{detail.course}}</p>
      <p>{{detail.img}}</p>
      <p>{{detail.level}}</p>
      <p>{{detail.slogon}}</p>
      <p>{{detail.title}}</p>
      <p>{{detail.why}}</p>
      <div>
        <ul v-for=" (item,index) in detail.chapter" :key='index'>
          <li>{{ item.name }}</li>
        </ul>
      </div>
      <div>
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
