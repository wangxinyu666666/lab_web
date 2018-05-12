<template>
  <div>
    <AllNotice ref="notice" :AllN="AllN" :TitleInOnepage="TitleInOnepage" :length="length" :onepage="onepage"></AllNotice>
  </div>
</template>

<script>
import AllNotice from '../../components/title.vue'
import {AllNoticeURL} from '../../api/httpapi.js'
export default{
  components: {AllNotice},
  data(){
    return{
      AllN:[],  //记录所有的新闻内容/通知内容
      TitleInOnepage:[],//处理每一页的显示情况
      length:0,   //总的要显示的标题条数
      onepage:3, //计算得到的需要显示每页的数量，剩下需要的分页操作由自己进行
    }
  },
  mounted() {
  //根据不同的先判断是通知还是新闻,然后确定渲染的内容
this.$refs.notice.Init_page(AllNoticeURL);
this.$store.state.News_All="notice";
  },
}
</script>

<style>
</style>
