import Vue from 'vue'
import Router from 'vue-router'

import Index1 from '@/page/index.vue'

import Intro from '@/page/intro/intro.vue'
import IntroAside from '@/page/intro/IntroAside.vue'
import Leaders from '@/page/intro/Leaders.vue'
import Environ from '@/page/intro/enviro.vue'

import Editor from '@/page/editor/editor.vue'

import AllNotice from '@/page/news/notice.vue'
import TitleDetails from '@/page/news/titledetails.vue'
import AllNews from '@/page/news/news.vue'
import TitleAside from '@/page/news/TitleAside.vue'

import LabsAside from '@/page/labs/Labs_Aside.vue'
import Attack from '@/page/labs/attack.vue'
import Virtual from '@/page/labs/virtual.vue'
import Cloud from '@/page/labs/cloud.vue'
import Domains from'@/page/labs/domains.vue'

import TeachersAside from '@/page/teachers/TeachersAside.vue'
import Teachers from '@/page/teachers/Teachers.vue'

import ProAside from '@/page/projects/ProAside.vue'
import Projects from '@/page/projects/projects.vue'
import Gains from '@/page/projects/gains.vue'
import Soft from '@/page/projects/soft.vue'
import Patent from  '@/page/projects/patent.vue'
import Article from '@/page/projects/article.vue'
import Union from '@/page/projects/unions.vue'
import Cooperate from '@/page/projects/cooprea.vue'

import ActAside from '@/page/activities/ActAside'
import Activities from '@/page/activities/Activities.vue'
import Happy from '@/page/activities/Happytime.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component:Index1
    },
    {
      path:'/editor',
      component:Editor
    },
    {
      path:'/notice',
      component:TitleAside,
      children:[{path:'',component:AllNotice },
              ]
    },
    {
        path:'/news',
        component: TitleAside,
        children:[{path:'',component:AllNews}]
    },
    {
      path: '/intro',
      component:IntroAside,
      children:[{path:'',component:Intro},
                {path:'leaders',component:Leaders},
                {path:'environment',component:Environ}]
    },
    {
    path:'/labs',
    component:LabsAside,
    children:[{path:'',component:Attack},
              {path:'domains',component:Domains},
              {path:'virtual',component:Virtual},
              {path:'yun',component:Cloud}]
   },
  {  path:'/teachers',
     component:TeachersAside,
     children:[{path:'',component:Teachers},
               {path:'details',component:TitleDetails}]
  },
  {
    path:'/projects',
    component:ProAside,
    children:[{path:'',component:Projects},
              {path:'gains',component:Gains},
              {path:'soft',component:Soft},
              {path:'patent',component:Patent},
              {path:'article',component:Article},
              {path:'UnionLabs',component:Union},
              {path:'Cooperate',component:Cooperate}
            ]
  },
  {  path:'/activities',
    component:ActAside,
    children:[{path:'',component:Activities},
               {path:'happytime',component:Happy}]
  },
  ]
})
