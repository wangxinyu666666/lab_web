<template>
  <div class="index">
    <div class="left">
    <Carousel></Carousel>
    </div>

    <div class="right">
      <div class="news">
        <el-card class="notice-card">
           <div slot="header" class="clearfix">
              <span style="float:left">中心新闻</span>
              <el-button style="float: right; padding: 3px 0" type="text" @click="allnews">more+</el-button>
           </div>
           <div class="text">
             <el-carousel trigger="click" height="120px">
                <el-carousel-item v-for="item1 in news_pages">
                  <div v-for="item in 3 ">
                    <el-button type="text" @click="details(item)" style="padding: 3px 0">{{item}}</el-button>
                    <span>{{item}}</span>
                    <hr/>
                  </div>
               </el-carousel-item>
            </el-carousel>
         </div>
        </el-card>
      </div>

      <div class="notice">
      </div>
   </div>
 </div>
</template>

<script>
import Carousel from '../components/carousel.vue'
export default{
 components:{Carousel},
  data(){
    return{
       news:[],  //记录所有的新闻内容
       notice:[],  //记录所有的通知内容
       news_pages:2, //新闻的分页数
       notice_pages:2, //通知分页数
    }
  },
  mounted() {
   //发送信息得到所有的新闻信息和通知信息然后进行填充

 },
  methods: {
    allnews(){
      //console.log("显示所有的新闻跳转到新闻页面");
      this.$store.state.newsactive='/'
      this.$router.push('/news');
    },
    allnotice(){
      //console.log("显示所有的通知公告");
      this.$store.state.newsactive='/notice'
      this.$router.push('/news/notice');
    },
    noticedetails(item){
      console.log("处理显示detail页面");
      this.$store.state.notice_key=item.name;
    //  alert(this.$store.state.notice_key);
      this.$store.state.newsactive='/noticedetails';
      this.$router.push('/news/noticedetails');
    },
    details(item){
        this.$store.state.news_key=item.name ;
      //  alert("新闻"+this.$store.state.news_key);
        this.$store.state.newsactive='/details';
        this.$router.push('/news/details');
    }
  },
}
</script>

<style>
.index .left{
  float:left;
  width: 60%;
}
.index .right{
  float:left;
  width:32%;
  min-height:440px;
  position: relative;
  left:5%;
  overflow: hidden;
}
/*对于战士的卡片的css*/
.right .news{
  min-height: 200px;
}
.right .notice{
  min-height: 200px;
}
 .clearfix:before,
 .clearfix:after {
   display: table;
   content: "";
 }
 .clearfix:after {
   clear: both
 }
 .right .notice-card{
   min-height: 200px;
   background:#11334D;
   color:white;
 }
.index .right .text{
   background:#4C72A5;
 }
 .index .right  span{
   float:right
 }
</style>
