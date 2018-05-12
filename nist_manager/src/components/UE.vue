<template>
  <div>
  <div class="editor-container">
    <script id="editor" type="text/plain"></script>
  </div>
  <br/>
 <center><div>
  <el-button type="primary" @click="postUEContent()">提交内容</el-button>
  <el-button  @click="render_in_editor()">重新渲染</el-button>
  </div>
</center>
  <br/><br/>
</div>
</template>

<script>
import Axios from 'axios'
import bus from '../assets/eventBus.js'
import{PostDataURL, renderURL}from'../api/httpapi.js'
  export default {
    data () {
      return {
        editor: null,
        key:"", //url里面带的key值
        defaultMsg:"",
        config: {
          toolbars: [
         ['preview','inserttitle', 'fontsize', //字号
        'paragraph', //段落格式
        'simpleupload', //单图上传
        'insertimage','link', //超链接
        'emotion', //表情
        'spechars',
         'forecolor',
         'customstyle'
         ],
         [  'justifyleft', //居左对齐
            'justifyright', //居右对齐
            'justifycenter', //居中对齐
            'justifyjustify'
         ],
      ['bold', 'italic', 'underline', 'superscript', 'subscript', 'removeformat', 'formatmatch', 'blockquote', '|', 'insertorderedlist', 'insertunorderedlist', 'selectall', 'cleardoc']
  ],
           initialFrameWidth :'100%',
           initialFrameHeight:400
      }
    }
  },
    mounted() {
      const _this = this;
      this.editor = UE.getEditor('editor', this.config); // 初始化UE
      this.editor.ready(function(){
      // _this.editor.setContent(_this.defaultMsg); // 确保UE加载完成后，放入内容。
      _this.init();       //初始化，确定网址OR重新渲染网页

      })
    },
    methods: {
      init(){
         //根据编辑的内容不一样，重新进行渲染,查询editor_key;
         var edit_key=this.$store.state.Editor_key;
         switch (edit_key) {
           case "add_news":
             //alert("新增新闻");
               this.key="add_news";
               break;
           case "add_notice":
               //alert("新增通知");
               this.key="add_notice"
               break;
           case "change_title":
               //  alert("编辑新闻/通知");
               //  alert(this.$store.state.news_key)
               this.key=this.$store.state.news_key;   //新闻或者是通知的关键字
               this.renderHTML(this.key);
               break;
           case "index_imgs_html":
                      this.key="index_imgs_html";
                      this.renderHTML(this.key);
                      break;
          case "rewrite_"+this.$store.state.card_key.name:

                      this.defaultMsg=this.$store.state.card_key.edit;
                      this.key=this.$store.state.Editor_key;
                      this.render_in_editor();
                      break;
          case "rewrite_desc_"+this.$store.state.card_key:
                      this.key="rewrite_desc_"+this.$store.state.card_key;
                      this.renderHTML("desc_"+this.$store.state.card_key);
                      break;
          case "add_leader":
                      this.key=this.$store.state.Editor_key;
                      this.renderHTML(this.key);
                      break;
          case "add_teacher":
                      this.key=this.$store.state.Editor_key;
                      this.renderHTML(this.key);
                      break;
          case "add_jishi":
                      this.key=this.$store.state.Editor_key;
                      this.renderHTML(this.key);
                      break;
        case "add_happy":
                      this.key=this.$store.state.Editor_key;
                      this.renderHTML(this.key);
                      break;
        case "index_imgs_html":
                this.key="index_imgs_html";
                this.renderHTML(this.key);
                break;
        case "intro":
               //实验室简介
               this.key="intro";
               this.renderHTML(this.key);
               break;
       case "lab_attack":
              //攻防
              this.key="lab_attack";
              alert(this.key);
              this.renderHTML(this.key);
              break;
       case "lab_virtual" :
              //虚拟化
              this.key="lab_virtual";
              this.renderHTML(this.key);
              break;
      case "lab_cloud":
         //云计算
         this.key="lab_cloud";
         this.renderHTML(this.key);
         break;
      case "lab_domains":
       //域名
       this.key="lab_domains";
       this.renderHTML(this.key);
       break;
       case "projects":
         //科研项目
         this.key="projects";
         this.renderHTML(this.key);
         break;
       case "article":
          //论文
          this.key="article";
          this.renderHTML(this.key);
          break;
       case "friends":
          //合作伙伴
          this.key="friends";
          this.renderHTML(this.key);
          break;
       case "gains":
           //系统类证书
           this.key="gains";
           this.renderHTML(this.key);
           break;
       case "patent":
       　　//专利
       this.key="patent";
       this.renderHTML(this.key);
       break;
       case "soft":
       　//软文
       this.key="soft";
       this.renderHTML(this.key);
       break;
       case  "union":
            //联合实验室
            this.key="union";
            this.renderHTML(this.key);
            break;
      case　"enviro_imgs_html":
             this.key="enviro_imgs_html";
             this.renderHTML(this.key);
             break;
      default:
               alert("出现错误");
        }
      },
      renderHTML(key){
         const _this=this;
         //alert("url的key:"+key);
         //var renderURL="/api/getdata?key=";
         var content="chushi";
         Axios.get(renderURL+key)
         .then(function(res){
             this.defaultMsg=res.data.HTML;
             //alert(this.defaultMsg);
           }.bind(this))
         .catch(function(){
           console.log("error");
         });
         setTimeout(_this.render_in_editor,500);
         _this.render_in_editor();
  },
      render_in_editor(){
        const　_this=this;
         //alert("hi");
        this.editor.ready(function(){
         _this.editor.setContent(_this.defaultMsg); // 确保UE加载完成后，放入内容。
        })
    },
      postUEContent() {
        let content=this.editor.getContent();       //获取内容
        var mydata={"HTML":content};
        //var PostDataURL='/api/postdata?key='
        var KEY=this.key;
        Axios.post(PostDataURL+KEY,mydata)
        .then(function(res){
            if(res.data.state=="SUCCESS")
            {
              alert("提交成功");
            }
            else{
              alert(res.data.error);
            }
        })
        .catch(function(){
              console.log("出现错误");
            })
     },
},
    destroyed() {
      this.editor.destroy();
    }
  }
</script>

<style>
.editor-container{
      width:80%;
      position: relative;
      left:10%
  }
</style>
