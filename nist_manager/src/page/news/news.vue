<template>
  <div>
    <AllNews ref="news" :AllN="AllN" :TitleInOnepage="TitleInOnepage" :length="length" :onepage="onepage"></AllNews>
  </div>
</template>

<script>
import AllNews from '../../components/title.vue'
import {AllNewsURL} from '../../api/httpapi.js'

export default{
  components: {AllNews},
  data(){
    return{
      AllN:[],  //记录所有的新闻内容/通知内容
      TitleInOnepage:[],//处理每一页的显示情况
      length:0,   //总的要显示的标题条数
      onepage:3, //计算得到的需要显示每页的数量，剩下需要的分页操作由自己进行
    }
  },
  mounted() {
  this.$refs.news.Init_page(AllNewsURL);
  this.$store.state.News_All="news";
  },
}
</script>

<style>
</style>
