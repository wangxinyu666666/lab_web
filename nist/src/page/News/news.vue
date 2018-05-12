<template>
  <div class="intro">
    <div class="details">
    <div v-for="item in news">
     <el-button type="text">{{item}}</el-button>
     <hr/>
   </div>
    </div>
      <br/><br/>

      <el-pagination
        small
        layout="prev, pager, next"
        :total="length"
        @current-change="ChangeNews">
      </el-pagination>
  </div>
</template>

<script>
import Axios from 'axios'
export default{
  data(){
    return{
         news:[],
         length:0,
         AllNews:[]
    }
  },
  methods:{
    ChangeNews(changePage){
    //通过分页重新刷新数据
    var len = this.AllNews.length;
    var  max = Math.ceil(len/10);
    var start=(changePage-1)*10;
    var end=changePage*10;
    if(changePage<max) this.news=this.AllNews.slice(start,end);
    else
    {
      end =len%10;
      if(end==0) this.news=this.AllNews.slice(start,changePage*10);
      else{
        this.news=this.AllNews.slice(start,start+end);
      }
    }

    }
  },
  mounted(){
    //do something after mounting vue instance
    Axios.get("../../../mock/test.json")
    .then(function(res){
        var tem=[];
        var len=res.data.news.length;
        this.length=len;
        for(var i=0;i<len;i++){
          tem.push(res.data.news[i].name);
        }
        if(len<10){this.news=tem;}
        else this.news=tem.slice(0,10);
        this.AllNews=tem;
    }.bind(this))
    .catch(function(){
    console.log("出现错误");
  })
  },
}
</script>

<style>
.intro{
 position: relative;
 width: 96%;
 min-height: 400px
}
.intro .details{
  width: 90%;
  position: relative;
  left:5%;
  background:#11334D;
  top:20px;
  border-radius:10px;
  min-height: 400px;
}
</style>
