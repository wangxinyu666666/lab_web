<template>
  <!--写卡片的显示效果的,可以上下显示，左右显示和详情页面展示，前面连个是带有链接功能的，分页效果也在这里-->
<div>
  <el-button type="text" class="button" @click="add">添加</el-button>
  <div class="details">
    
    <div v-if="show" style="margin-left: 20px">
      <div id="line">
        <p align="center">网络与信息安全技术研究中心（NIST）现任领导</p>
      </div>
      <el-row :gutter="10">
        <el-col :span="item.h*1.618+item.w" v-for="(item,index) in getdata" :key="index">
          <el-card :body-style="{ padding: '0px' }">
            <div :style="'width:'+(item.h*1.618+item.w)+'px;'+'height:'+item.h+'px'">
            <div class="images">
              <div :style="'width:'+item.w+'px;'">
                <img :src="item.pictures" class="image" id="imagee">

              </div>
            </div>
              <div class="show">
                <div class="text" v-html="item.html">
                </div>
              </div>
            </div>

          </el-card>
          <div>
              <el-button type="text" class="button" @click="edit(item)">编辑主页面</el-button>
              <el-button type="text" class="button" @click="editdesc(item)">编辑详情</el-button>
              <el-button type="text" class="button" @click="del(item)">删除</el-button>
            </div>
        </el-col>
      </el-row>
    </div>
    <div v-if="shows" style="margin-left: 20px">
      <el-row :gutter="10">
        <el-col :span="item.w" v-for="(item,index) in getdata" :key="index" >
          <el-card :body-style="{  padding:'0px',background:'#11344E' }">
          <div :style="'width:'+item.w+'px;'">

              <img :src="item.pictures" class="iimage">


          </div>
          <div v-if="inshows" :style="'width:'+item.w+'px;'" class="shows" v-html="item.html" >
          </div>
          </el-card>
          <div v-if="outshows" :style="'width:'+item.w+'px;'" class="shows" v-html="item.html" >
          </div>
          <div>
              <el-button type="text" class="button" @click="edit(item)">编辑主页面</el-button>
              <el-button type="text" class="button" @click="editdesc(item)">编辑详情</el-button>
              <el-button type="text" class="button" @click="del(item)">删除</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    </div>
</div>
</template>
<script>
import Axios from 'axios'
import bus from '../assets/eventBus.js'
import {PostDataURL,renderURL} from'../api/httpapi.js'
  export default {
    data () {
      return {
        show:"",
        shows:"",
        inshows:"",
        outshows:"",
        leng:"",
        getdata:[

        ],
      }
    },
    methods: {

      add(){
        switch(this.$store.state.ifstate){
          case "leaders":
            this.$store.state.Editor_key="add_leader";
            break;
          case "teachers":
            this.$store.state.Editor_key="add_teacher";
            break;
          case "jishi":
            this.$store.state.Editor_key="add_jishi";
            break;
          case "happy":
            this.$store.state.Editor_key="add_happy";
            break;
        }
        this.$router.push("/editor");
      },
      del(item){
        //this.$store.state.leaders_key=item.name;
        //alert(item.name);
        var key="delete_"+item.name;
          this.$confirm('确定删除?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          Axios.post(PostDataURL+key)
        //Axios.get('./mock/teachers.json')
        .then(function(res){
           //console.log(PostDataURL+key);
           this.$message({
            type: 'success',
            message: '删除成功!'
          });
      }.bind(this)
      ).catch(function(){
        console.log("error");
      });

        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });


      },
      edit(item){
        this.$store.state.card_key=item;


        //console.log(item.edit);
        this.$store.state.Editor_key="rewrite_"+item.name;
        //alert(this.$store.state.Editor_key);
        this.$router.push("/editor");
      },
      editdesc(item){
        this.$store.state.card_key=item.name;
        this.$store.state.Editor_key="rewrite_desc_"+item.name;
        //alert(this.$store.state.Editor_key);
        this.$router.push("/editor");
      },
    },
    mounted (){
      const _this = this;
      var parm=this.$store.state.ifstate;
      if(!parm){
                parm = JSON.parse(window.localStorage.getItem('card'))
        };
      switch(parm){
          case "leaders":
            window.localStorage.setItem('card', JSON.stringify(parm));
            this.show=true;
            this.shows=false;
            this.inshows=false;
            this.outshows=false;
            break;
          case "teachers":
            window.localStorage.setItem('card', JSON.stringify(parm));
            this.show=false;
            this.shows=true;
            this.inshows=false;
            this.outshows=true;
            break;
          case "jishi":
            window.localStorage.setItem('card', JSON.stringify(parm));
            this.show=false;
            this.shows=true;
            this.inshows=true;
            this.outshows=false;
            break;
          case "happy":
            window.localStorage.setItem('card', JSON.stringify(parm));
            this.show=false;
            this.shows=true;
            this.inshows=true;
            this.outshows=false;
            break;
        };
        console.log(parm);
        var imgReady = (function(){
            var list = [],
            intervalId = null;

        // 用来执行队列
        var queue = function(){

            for(var i = 0; i < list.length; i++){
                list[i].end ? list.splice(i--,1) : list[i]();
            }
            !list.length && stop();
        };

        // 停止所有定时器队列
        var stop = function(){
            clearInterval(intervalId);
            intervalId = null;
        }
        return function(url, ready, error) {
            var onready = {},
                width,
                height,
                newWidth,
                newHeight,
                img = new Image();
                img.src = url;

            // 如果图片被缓存，则直接返回缓存数据
            if(img.complete) {
                ready.call(img);
                console.log(img.complete);
                return;
            }
            width = img.width;
            height = img.height;

        // 加载错误后的事件
        img.onerror = function () {
            error && error.call(img);
            onready.end = true;
            img = img.onload = img.onerror = null;
        };

        // 图片尺寸就绪
        var onready = function() {
            newWidth = img.width;
            newHeight = img.height;
            if (newWidth !== width || newHeight !== height ||
                // 如果图片已经在其他地方加载可使用面积检测
                newWidth * newHeight > 1024
            ) {
                ready.call(img);
                onready.end = true;
            };
        };
        onready();
        // 完全加载完毕的事件
        img.onload = function () {
            // onload在定时器时间差范围内可能比onready快
            // 这里进行检查并保证onready优先执行
            !onready.end && onready();
            // IE gif动画会循环执行onload，置空onload即可
            img = img.onload = img.onerror = null;
        };


        // 加入队列中定期执行
        if (!onready.end) {
            list.push(onready);
            // 无论何时只允许出现一个定时器，减少浏览器性能损耗
            if (intervalId === null) {
                intervalId = setInterval(queue, 40);
            };
          };
        }
      })();
        
        
        var len;
        var datas=[]
        var srcs=[]
        var tem=[]
        var gets = function () {
            return new Promise(function (resolve, reject) {
               Axios.get(renderURL+parm)
        //Axios.get('./mock/teachers.json')
        .then(function(res){

          
          
          datas=res.data.getdata;
          resolve(datas)
          }.bind(this)
      ).catch(function(error){
        console.log("error");
        console.log(error.name);
        console.log(error.message);
      });
            })
          }
          var getsrc = function (datas) {
            return new Promise(function (resolve, reject) {
                len=datas.length
                for(var i=0;i<len;i++)
                {

                   srcs[i]=datas[i].pictures;
                }
                resolve(srcs)
              
            })
          };
          var getwh = function (srcs) {
            return new Promise(function (resolve, reject) {
 
              imgReady(srcs,function(){
                
                
                var ww=this.width;
                var hh=this.height;
                console.log(111);
                var temp=[];
                temp.push({h:hh,w:ww});
　　            console.log('width:' + ww + 'height:' + hh);

               resolve(temp);
                
              });
            })
          };
          var gettem = function (temp,datas,i) {
            return new Promise(function (resolve, reject) {  
                //console.log(temp);         
                len=datas.length                
                  tem[i]={
                    pictures:datas[i].pictures,
                    html:datas[i].html,
                    name:datas[i].name,
                    edit:datas[i].edit,
                    h:temp[0]['h'],
                    w:temp[0]['w'],
                  };                                      
              console.log(tem)
              }
            )
          };
          (async () => {
            let dat=await gets()
            let getsrcs = await getsrc(dat)

            // await只能使用在原生语法
            for (var i=0;i<len;i++) {
                let src = getsrcs[i];

                //console.log("正在获取"+src);
                gettem(await getwh(src),dat,i);
            }

            //console.log('=== 获取完成 ===');
            this.getdata=tem
          //console.log(this.getdata[2]['h'])
            //
          })();
    }
  }
</script>
<style>
  .details{
  width:95%;
  position: relative;
  left:1%;
  background:rgba(234,234,234,0.1);
  border-radius:10px;
  min-height: 400px;
  overflow:visible
}
  .details #line{
    width: 100%;
    border-bottom: 1.5px solid white;
  }
  .details #line p{
    font-family:"微软雅黑"; 
    font-size:18px; 
    font-weight:bold;
    padding-top:15px;
    color:#FFFFFF;}
  .el-col {
    border-radius: 10px;
    margin-top: 20px;
  }
  .show {

    height:100%;
    overflow:auto;

  }

  .shows {
    overflow-y:auto;
    width:100%;
    word-wrap:break-word;
    word-break:break-all;

  }
  .text {
    float:left;
    width:100%;

    word-wrap:break-word;
    word-break:break-all;

  }
  .image {
    width:100%;
    height:100%;

  }
  .images {
    _margin-right:-3px;
    height:100%;
    float:left;
  }


</style>
