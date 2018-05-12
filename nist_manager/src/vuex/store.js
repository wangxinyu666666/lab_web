import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'

Vue.use(Vuex)

// 应用初始状态
const state ={
  News_All:"news",
  news_key:"",           //新闻或者通知的渲染值
  ifstate:"",          //记录当前是在中心领导还是师资队伍
  card_key:"",
  Second_Acitive:'/',     //用来管理新闻的二级导航栏的正确选择
  InitSecodRouter:[],
  Editor_key:""    //启用编辑选，备选值add_news/add_notide/change_title
}

// 定义所需的 mutations
const mutations = {
     HandleSecondRouter(state, payload) {
       //alert(payload.firstAct);
       switch (payload.firstAct) {
          case "news":
          state.InitSecodRouter=[{index:"/",name:"中心新闻"},{index:"/notice",name:"通知公告"}];
          break;
        case "labs":
           state.InitSecodRouter=[{index:"/attack",name:"网络攻防技术研究室"},{index:"/virtual",name:"虚拟化技术研究室"},{index:"/domains",name:"域名体系安全技术研究室"},{index:"/yun",name:"云计算技术研究室"}];
        //   alert(payload.firstAct);
           break;
        case "intro":
           state.InitSecodRouter=[{index:"/intro",name:"中心简介"},{index:"/leaders",name:"中心领导"},{index:"/environment",name:"中心环境"}];
           break;
        case "teachers":
            state.InitSecodRouter=[{index:"/teachers",name:"师资队伍"}];
            break;
       case "activities":
            state.InitSecodRouter=[{index:'/activities',name:"中心纪实"},{index:"/happytime",name:"欢乐时光"}]
             break;
       }
      // alert(state.InitSecodRouter);
    },
    showUserName(state){
        alert(state.username);
    },
    DECREMENT(state) {
        state.count--
    },
  /*  setTaskId: (state, name) => {
        state.taskid = name
    }*/
}

// 创建 store 实例
export default new Vuex.Store({
    actions,
    getters,
    state,
    mutations
})
