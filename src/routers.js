import login from './components/login.vue'
import view from './components/view.vue'
import del from './components/del.vue'
import {createRouter,createWebHistory} from 'vue-router'

const routes=[
{
    name:'login',
    component:login,
    path:'/login'
},
{
    name:'view',
    component:view,
    path:'/view'
},
{
    name:'delete',
    component:del,
    path:'/delete'
}

];
const router=createRouter(
    {
        history:createWebHistory(),
        routes,
    }
);
export default router;