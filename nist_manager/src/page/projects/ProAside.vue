<template>
        <div>
            <el-row :gutter="10">
                <el-col :xs="4" :sm="4" :md="4" :lg="4">
                    <div>
                      <el-menu :default-active="this.$store.state.Second_Acitive" class="el-menu-demo"  @select="handleSelect">
                        <el-menu-item index="1"><i class="el-icon-location"></i>科研项目</el-menu-item>
                        <el-submenu index="2">
                            <template slot="title"><i class="el-icon-message"></i>科研成果</template>
                            <el-menu-item index="2-1">系统类证书</el-menu-item>
                            <el-menu-item index="2-2">专利</el-menu-item>
                            <el-menu-item index="2-3">论文</el-menu-item>
                            <el-menu-item index="2-4">软著</el-menu-item>
                      </el-submenu>
                      <el-menu-item index="3"><i class="el-icon-setting"></i>联合实验室</a></el-menu-item>
                      <el-menu-item index="4"><i class="el-icon-loading"></i>合作伙伴</a></el-menu-item>
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
            activeIndex:"1",
            icon:["el-icon-setting","el-icon-message","el-icon-menu","el-icon-loading"]
          }
        },
        methods:{
            handleSelect(key, keyPath){
                  switch (key) {
                    case '1':
                      this.$router.push('/projects');
                      break;
                    case '2-1':
                       this.$router.push('/projects/gains');
                       break;
                    case '2-2':
                       this.$router.push('/projects/patent');
                       break;
                    case '2-3':
                       this.$router.push('/projects/article');
                       break;
                    case '2-4':
                       this.$router.push('/projects/soft');
                       break;
                    case '3':
                       this.$router.push('/projects/UnionLabs');
                       break;
                   case '4':
                      this.$router.push('/projects/Cooperate');
                      break;
                  }
              }
            },
        }
</script>
<style>

</style>
