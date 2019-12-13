<template>
  <div>
    <h1>LuffyX学位</h1>
   <p>{{title}}</p>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        title:''
      }
    },
    mounted:function() {
      this.initAuth()
    },
    methods: {
      initAuth(){
        var that =this;
        this.$axios.request({
          url:'http://127.0.0.1:8001/api/v1/mirco/',
          method:'GET',
          params:{
            token:this.$store.state.token
          }
        }).then(function(ret){
            if(ret.data.code === 1000){
              that.title = ret.data.title;
            }else{
              console.log(ret);
            }
        }).catch(function(ret){
             console.log(ret);
        })
      }
    }
  }
</script>

<style scoped>

</style>
