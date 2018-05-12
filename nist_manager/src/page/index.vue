<template>
  <div class="index">
    <div class="left">
    <Carousel :pictures=pictures style="position:relative;left:4%"></Carousel>
    <div class="editimgs">
    <el-button icon="el-icon-edit" @click="editIndexImgs">编辑图片</el-button>
   </div>
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
                <el-carousel-item v-for="i in max_pages" :key="i">
                   <div v-for="item in news[i-1]" :key="i">
                    <el-button type="text" @click="details(item)" style="padding: 3px 0">{{item.name}}</el-button>
                    <span>{{item.time}}</span>
                    <hr/>
                  </div>
               </el-carousel-item>
            </el-carousel>
         </div>
        </el-card>
      </div>

      <div class="notice">
        <el-card class="notice-card">
           <div slot="header" class="clearfix">
              <span style="float:left">通知公告</span>
              <el-button style="float: right; padding: 3px 0" type="text" @click="allnotice">more+</el-button>
           </div>
           <div class="text">
             <el-carousel trigger="click" height="120px">
                <el-carousel-item v-for="i in max_pages" :key="i">
                   <div v-for="item in notice[i-1]" :key="i">
                    <el-button type="text" @click="noticedetails(item)" style="padding: 3px 0">{{item.name}}</el-button>
                    <span>{{item.time}}</span>
                    <hr/>
                  </div>
               </el-carousel-item>
            </el-carousel>
         </div>
        </el-card>
      </div>
   </div>
 </div>
</template>

<script>
import Axios from 'axios'
import {AllNewsURL,AllNoticeURL,IndexIMGURL}from '../api/httpapi.js'
import Carousel from '../components/carousel.vue'
export default{
 components:{Carousel},
  data(){
    return{
      //初始化走马灯的信息
       pictures:[],
       news:[[{

           }]],  //记录所有的新闻内容
       notice:[],  //记录所有的通知内容
       news_pages:2, //新闻的分页数
       notice_pages:2, //通知分页数
       onepage:3,     //每页显示的条数，可以改
       max_pages:3  //最大分页数
    }
  },
  mounted() {
   //发送信息得到所有的新闻信息和通知信息然后进行填充
   //var AllNewsURL='../mock/allnews.json';
   //var AllNoticeURL="../mock/allnotice.json";
   //var IndexIMGURL="../mock/indeximgs.json"
   Axios.get(AllNewsURL)
   .then(function(res){
      var news_res=res.data.data;
    //  var notice_res=res.data.notice;
      this.news=this.News_page(news_res);
    // this.notice=this.News_page(notice_res);
   }.bind(this))
   .catch(function(){
     console.log("出现错误");
   }),
   Axios.get(AllNoticeURL)
   .then(function(res){
      var notice_res=res.data.data;
    //  this.news=this.News_page(news_res);
      this.notice=this.News_page(notice_res);
   }.bind(this))
   .catch(function(){
     console.log("出现错误");
   }),
   Axios.get(IndexIMGURL)
   .then(function(res){
     var len=res.data.pictures.length;
     var tem=[];
     for(var i=0;i<len;i++){
        tem.push(res.data.pictures[i]);
     }
     this.pictures=tem;
   }.bind(this))
   .catch(function(){
     console.log("error");
   })
 },
  methods: {
    editIndexImgs(){
        this.$store.state.Editor_key="index_imgs_html";
        this.$router.push('/editor');
    },
    News_page(arr){
      //处理显示新闻和通知
       var length = arr.length;
       var all=[];      //接收数组信息的信息
       var tem=[];        //存放临时结果
       var result=[];   //存最后的结果
       var start=0;
       var end=0;
       for(var i=0;i<length;i++)
       {
         all.push({
             name:arr[i].name,
             time:arr[i].time,
             id:arr[i].id
         })
       }

       if(length >= this.onepage*this.max_pages)
       {
         for(i=0;i<this.max_pages;i++)
         {
           start=0;
           end=this.onepage;
           tem=all.splice(start,end);
           result.push(tem);
         }
       }
       else{
          this.max_pages = Math.ceil(length/this.onepage); //this.onepag是每页容纳的最大条数
          for(i=0;i<this.max_pages;i++)
          {
            start=0;
            end=this.onepage;
            if(i==this.max_pages-1) end=all.length;
            tem=all.splice(start,end);
          //  console.log(i+"----"+tem);
            result.push(tem);
          }
       }
       return result;
    },

    allnews(){
      //console.log("显示所有的新闻跳转到新闻页面");
      this.$store.state.Second_Acitive='/',      //处理二级页面的选中
      this.$store.state.News_All="news",         //处理通知/详情
      this.$router.push('/news');
    },
    allnotice(){
      //console.log("显示所有的通知公告");
      this.$store.state.Second_Acitive='/notice',
      this.$store.state.News_All="notice",
      this.$router.push('/notice');
    },
    noticedetails(item){
      //console.log("处理显示detail页面");
    //  this.$store.state.News_All="notice";       //判断显示所有新闻还是所有的通知
      this.$store.state.news_key=item.id;      //查询的详情的名字
    //  alert(item.id);
      this.$store.state.Editor_key="change_title";
      this.$router.push('/editor');
    },
    details(item){
      //  this.$store.state.News_All="news";
        this.$store.state.news_key=item.id;
        this.$store.state.Editor_key="change_title"
    //    this.$store.state.Second_Acitive='/';
        this.$router.push('/editor');
    }
  },
}
</script>

<style>
.index .left{
  float:left;
  width: 60%;
  min-height: 450px;
}
.index .right{
  float:left;
  width:32%;
  min-height:440px;
  position: relative;
  left:5%;
  top:10px;
  overflow: hidden;
}
/*对于战士的卡片的css*/
.right .news{
  min-height: 225px;
}
.right .notice{
  min-height: 225px;
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
 .editimgs{
  float:right;
 }
</style>
