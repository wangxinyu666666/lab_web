<template>
        <div>
            <el-row :gutter="10">
                <el-col :xs="4" :sm="4" :md="4" :lg="4">
                    <div>
                        <el-menu :default-active="this.$store.state.Second_Acitive" class="el-menu-vertical-demo"  @select="handleSelect">
                            <el-menu-item v-for="(item,index) in SecondRouter" :key="index" :index="item.index"><i :class="icon[index]"></i>{{item.name}}</el-menu-item>
                        </el-menu>
                    </div>
                </el-col>
                <el-col :xs="20" :sm="20" :md="20" :lg="20">
                    <div style="margin-top:10px">
                        <router-view></router-view>
                    </div>
                </el-col>
            </el-row>
        </div>
</template>

<script>
export default {
        data(){
          return{
          //  SecondRouter:[{"index":"/","name":"中心领导"},{"index":"/virtual","name":"中心领导"},{"index":"/domains","name":"中心领导"}],
            icon:["el-icon-setting","el-icon-message","el-icon-menu","el-icon-loading"]
          }
        },
        props:{
          SecondRouter:{}
        },
        methods:{
          //处理单击二级导航
            handleSelect(key, keyPath){
                  switch (key) {
                    //新闻二级标题
                    case '/':
                      this.$router.push('/news');
                      break;
                    case '/notice':
                       this.$router.push('/notice');
                       break;
                    //组织机构哦二级标题
                    case '/attack':
                      // alert("hi");
                       this.$router.push('/labs');
                       break;
                    case '/domains':
                       this.$router.push('/labs/domains');
                       break;
                    case '/virtual':
                       this.$router.push('/labs/virtual');
                       break;
                    case '/yun':
                        this.$router.push('/labs/yun');
                        break;
                        //中心简介二级比标题
                    case '/intro':
                        this.$router.push('/intro');
                        break;
                    case '/leaders':
                        this.$store.state.ifstate="leaders";
                        this.$router.push('/intro/leaders');
                        break;
                   case '/environment':
                        this.$router.push('/intro/environment');
                        break;
                        //欢乐时光
                  case '/activities':
                        this.$store.state.ifstate="jishi";
                        this.$router.push('/activities');
                        break;
                  case '/happytime':
                        this.$store.state.ifstate="happy";
                        this.$router.push('activities/happytime');
                        break;
                  }
              }
            },
        }
</script>
<style>

</style>
