<template>
  <div>
    <h3>{{title}}</h3>
    <button @click='frontPage'>上一页</button>
    <img :src="defaultImg" alt="" @mouseOver='stopScroll' @mouseout='startScroll'>
    <button @click='afterPage'>下一页</button>
    <ul>
      <li v-for="(item,i) in images" @click="changePage(item)" class='default' :key="i" :class='{active:isActive(i)}'>{{i+1}}</li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'lunbo',
    data() {
      return {
        title: '轮播图',
        images: [{
            id: 1,
            src: '/src/images/1.jpg'
          },
          {
            id: 2,
            src: '/src/images/2.jpg'
          },
          {
            id: 3,
            src: '/src/images/3.jpg'
          },
          {
            id: 4,
            src: '/src/images/4.jpg'
          }
        ],
        defaultImg: '/src/images/1.jpg',
        pagenum: 0,
        timer: null,
        index: 0,
      }
    },
    created() {
      this.timer = setInterval(this.afterPage, 2000);
    },
    methods: {
      changePage(item) {
        this.defaultImg = item.src;
        this.pagenum = item.id - 1;
      },
      frontPage() {
        if (this.pagenum > 0) {
          this.pagenum -= 1;
        } else {
          this.pagenum = this.images.length - 1
        };
        this.defaultImg = this.images[this.pagenum].src
      },
      afterPage() {
        if (this.pagenum < this.images.length - 1) {
          this.pagenum += 1;
        } else {
          this.pagenum = 0
        };
        this.defaultImg = this.images[this.pagenum].src
      },
      stopScroll() {
        clearInterval(this.timer);
      },
      startScroll() {
        this.timer = setInterval(this.afterPage, 10000);
      },
      isActive(i) {
        return i == this.pagenum
      }
    }
  }
</script>

<style scoped="">
  div{
    float: left;
  }
  ul li{
    padding: 10px 20px;
    border: #2C3E50 solid 2px;
  }
  img{
    width: 600px;
    height: 600px;
  }
  .default {
    background-color: pink;
  }

  .active {
    background-color: red;
  }
</style>
