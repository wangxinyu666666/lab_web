<template>
  <div class="intro">
    <div id="details" >
       <div id="title" v-for="(item,index) in TitleInOnepage" :key="index">
            <el-button  type="text" @click="details(item.id)" style="padding:5px 0">
              <span style="font-size:15px">{{item.name}}</span>
            </el-button>
          <hr/>
       </div>
       <div class="editNews">
          <el-button icon="el-icon-circle-plus" @click="add">新增内容</el-button>
          <el-button icon="el-icon-edit" @click="editNews">点击编辑</el-button>
      </div>
    </div>
    <br/>
    <div class="block">
    <el-pagination
      @current-change="handleCurrentChange"
      current-page.sync=1
      :page-size="onepage"
      layout="prev, pager, next, jumper"
      :total="length">
    </el-pagination>
  </div>
    <br/>
  </div>
</template>

<script>
import Axios from 'axios'
export default{
  data(){
    return{
    //  AllN:[],  //记录所有的新闻内容/通知内容
    //  TitleInOnepage:[],//处理每一页的显示情况
    //  length:0, //总的要显示的标题条数
  //    onepage:0, //计算得到的需要显示每页的数量，剩下需要的分页操作由自己进行
    }
  },
  props:{
    AllN:[],  //记录所有的新闻内容/通知内容
    TitleInOnepage:[],//处理每一页的显示情况
    length:Number, //总的要显示的标题条数
    onepage:Number, //计算得到的需要显示每页的数量，剩下需要的分页操作由自己进行
  },
  methods: {
    add(){
      //alert(this.$store.state.News_All);
      if(this.$store.state.News_All=="news")
      {
        //alert("news");
        this.$store.state.Editor_key="add_news";
      }
      else
      {
        this.$store.state.Editor_key="add_notice"
      }
      this.$router.push("/editor");
    },
    editNews(){
      this.$notify({
        title: 'Tips',
        message:"请点击标题进行编辑" ,
        type: 'success'
      });
  },
    Init_page(url){
      Axios.get(url)
      .then(function(res){
           var len=res.data.data.length;
           this.length=len;            //告诉分页总数
           var tem=[];
           for(var i=0;i<len;i++){
             tem.push({
                 name:res.data.data[i].name,
                 time:res.data.data[i].time,
                 id:res.data.data[i].id
             })
           }
           this.AllN=tem;
           this.TitleInOnepage=tem.slice(0,this.onepage);    //处理显示首页信息
      }.bind(this))
      .catch(function(){
        console.log("error");
      })
    },
    handleCurrentChange(val) {
       //处理分页
       var tem=[];
       tem=this.AllN;
       var start=this.onepage*(val-1);
       var end=this.onepage*val;
       if(end>this.length) end=this.length;
       this.TitleInOnepage=tem.slice(start,end);
     },
    Calcu(){
      //初始化时计算details的高度并且操纵底层dom进行绑定
      //然后对每一条信息进行高度设定并且进行绑定，然后可以控制每页的显示条数，从而进行分页的操作
      alert("hi");
    },
    details(id){
    this.$store.state.news_key=id;  //编辑新闻或者是通知,id就可以区分了，id就是key值
    this.$store.state.Editor_key="change_title"
    this.$router.push('/editor');
},

  }
}
</script>

<style>
.intro{
 position: relative;
 width: 96%;
 min-height: 400px;
}
.intro #details{
  width: 90%;
  position: relative;
  left:5%;
  background:rgba(234,234,234,0.1);
  border-radius:10px;
  height: 400px;
  overflow: hidden;
}
.intro #title{
  width:80%;
  position: relative;
  left:10%;
  overflow: hidden;
  top:10px
}
.block{
float: right;
}

</style>
