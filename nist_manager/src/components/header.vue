<template>
  <div>
    <header style="height:20%">

      <el-row style="height:70%;">
        <el-col :offset="1" :span="5">
          <img src="../assets/school.png" style="width:80%">
        </el-col>
        <el-col :offset="1" :span="2">
          <img src="../assets/WIZEYE.png" style="width:100%">
        </el-col>
        <el-col :offset="1" :span="12">
          <span>网络与信息安全技术研究中心</span><br>
          <span>Network and Information Security Technology Research Center</span><br>
          <span>国家计算机信息内容安全重点实验室（威海）</span><br>
          <span>State key Laboratory of Computer Information Security, Weihai</span>
        </el-col>
      </el-row>


          <!--纯CSS3实现导航功能-->
          <!--ul id="NAV">
       		    <li>首页</li>
       		    <li>中心介绍
       		      <ul class="drop">
       		        <div>
       		        <li>中心简介</li>
       		        <li>中心领导</li>
       		        <li>中心环境</li>
       		        </div>
       		      </ul>
       		    </li>
              <li class="large">组织机构
       		        <ul class="drop">
       		        <div>
       		        <li>网络攻防技术研究室</li>
       		        <li>虚拟化技术研究室</li>
       		        <li>域名体系安全技术研究室</li>
                  <li>云计算技术研究室</li>
       		        </div>
       		       </ul>
       		      </li>
       		    <li>师资队伍</li>
              <li>科学研究
                  <ul class="drop">
                  <div>
                  <li>科研项目</li>
                  <li>科研成果</li>
                  <li>联合实验室</li>
                  <li>合作伙伴</li>
                  </div>
                 </ul>
              </li>
             <li>中心活动</li>
           </ul-->

          <!--自带的导航功能显示效果不好-->
          <el-row style="background:#11344E;">
            <el-col :xs="24" :sm="24" :md="24" :lg=" {span:13, offset:6}" :xl= "{span: 11, offset: 6}" >
              <el-menu :default-active="activeIndex"  mode="horizontal" @select="handleSelect" :active-text-color="changecolor"text-color="#FFFFFF" background-color="#11344E">
                <el-menu-item style="height:125%" index="1">首页</el-menu-item>
                <el-submenu  index="2">
                  <template slot="title">中心简介</template>
                  <el-menu-item index="2-1">中心简介</el-menu-item>
                  <el-menu-item index="2-2">中心领导</el-menu-item>
                  <el-menu-item index="2-3">中心环境</el-menu-item>
                </el-submenu>
                <el-submenu index="3">
                  <template slot="title">组织机构</template>
                  <el-menu-item index="3-1">网络攻防技术研究室</el-menu-item>
                  <el-menu-item index="3-2">虚拟化技术研究室</el-menu-item>
                  <el-menu-item index="3-3">域名体系安全研究室</el-menu-item>
                  <el-menu-item index="3-4">云计算技术研究室</el-menu-item>
                </el-submenu>
                <el-menu-item index="4">师资队伍</el-menu-item>
                <el-submenu index="5">
                  <template slot="title">科学研究</template>
                  <el-menu-item index="5-1">科研项目</el-menu-item>
                  <el-menu-item index="5-2">科研成果</el-menu-item>
                  <el-menu-item index="5-3">联合实验室</el-menu-item>
                  <el-menu-item index="5-4">合作伙伴</el-menu-item>
                </el-submenu>
                <el-menu-item index="6">中心活动</el-menu-item>
              </el-menu>
            </el-col>
          </el-row>
 </header>
</div>
</template>

<script>
export default {
  data () {
    return {
        activeIndex:'1',
        changecolor:"#0EBEFF"
    }
  },
  methods: {
    handleSelect(key, keyPath){
        switch(key){
            case '1':
             //首页
              this.$router.push('/');
              this.changecolor="#0EBEFF"
              break;
            case '2-1':
                //中心简介
                this.$store.state.First_Active="intro";
                this.$store.state.Second_Acitive="/intro";
                this.$router.push('/intro');
                this.changecolor="#ffd04b"
                break;
            case '2-2':
                //中心领导
                this.$store.state.First_Active="intro";
                this.$store.state.Second_Acitive="/leaders";
                this.$store.state.ifstate="leaders";
                this.$router.push('/intro/leaders');
                this.changecolor="#ffd04b"
                break;
            case '2-3':
                //中心环境
                this.$store.state.First_Active="intro";
                this.$store.state.Second_Acitive="/environment";
                this.$router.push('/intro/environment');
                this.changecolor="#ffd04b"
                break;
            case '3-1':
                //网络攻防
                this.$store.state.First_Active="labs";
                this.$store.state.Second_Acitive="/attack"
                this.$router.push('/labs');
                this.changecolor="#47CF73";
                break;
           case '3-2':
                //虚拟化
                this.$store.state.First_Active="labs";
                this.$store.state.Second_Acitive="/virtual"
                this.$router.push('/labs/virtual');
                this.changecolor="#47CF73";
                break;
          case '3-3':
              //域名
              this.$store.state.First_Active="labs";
              this.$store.state.Second_Acitive="/domains";
              this.$router.push('/labs/domains');
              this.changecolor="#47CF73";
              break;
          case '3-4':
                //云计算
                this.$store.state.First_Active="labs";
                this.$store.state.Second_Acitive="/yun";
                this.$router.push('/labs/yun');
                this.changecolor="#47CF73";
                break;
          case '4':
                //师资队伍
                this.$store.state.First_Active="teachers";
                this.$store.state.Second_Acitive="/teachers";
                this.$store.state.ifstate="teachers";
                this.$router.push('/teachers');
                this.changecolor="pink";
                break;
          case '5-1':
                //科研项目,这个得单独写一个可以有下拉的
                this.$store.state.Second_Acitive="1";
                this.$router.push('/projects');
                this.changecolor="#AE63E4";
                break;
          case '5-2':
                //科研成果
                this.$store.state.Second_Acitive="2-1"
                this.$router.push('/projects/gains');
                this.changecolor="#AE63E4";
                break;
          case '5-3':
               //联合实验室
                this.$store.state.Second_Acitive="3";
                this.$router.push('/projects/UnionLabs');
                this.changecolor="#AE63E4";
                break;
          case '5-4':
               //合作伙伴
                  this.$store.state.Second_Acitive="4"
                  this.$router.push('/projects/Cooperate');
                  this.changecolor="#AE63E4";
                  break;
            case '6':
                //中心记实
                this.$store.state.First_Active="activities";
                this.$store.state.Second_Acitive="/activities";
                  this.$store.state.ifstate="jishi";
                this.$router.push('/activities');
                this.changecolor="#FF6666";
                break;
        }},
        /*FirstRouter(){
           alert("hi");
        }*/
  }
}
</script>


<style scoped>
@import 'HEADER.css'
</style>
