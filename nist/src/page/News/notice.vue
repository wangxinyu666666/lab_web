<template>
  <div class="intro">
    <div class="details">
    <div v-for="item in notice">
     <el-button type="text">{{item}}</el-button>
     <hr/>
   </div>
    </div>
      <br/><br/>

      <el-pagination
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
         notice:[],
         length:'',
    }
  },
  methods:{
    ChangeNews(changePage){
    //  alert(changePage);
    //changePage是当前分页符号的页数
    }
  },
  mounted() {
    //do something after mounting vue instance
    Axios.get("../../../mock/test.json")
    .then(function(res){
        var tem=[];
        var len=res.data.notice.length;
        this.length=len;
        for(var i=0;i<len;i++){
          tem.push(res.data.notice[i].name);
        }
        this.notice=tem;
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
