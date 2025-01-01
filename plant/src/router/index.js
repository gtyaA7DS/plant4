import { createRouter, createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: AppLayout,
            children: [
                {
                    path: '/',
                    name: 'dashboard',
                    component: () => import('@/views/Dashboard.vue')
                },

                {
                    path: '/detail/control',
                    name: 'control',
                    component: () => import('@/views/detail/Control.vue')
                },


                {
                    path: '/detail/charts',
                    name: 'charts',
                    component: () => import('@/views/detail/Chart.vue')
                },

            ]
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('@/views/login/Login.vue')
        },


        {
            path: '/404',
            name: '/404',
            component:  import('@/views/404/NotFound.vue')
        },
        {
            path: '/:pathMatch(.*)',
            //访问主页的时候 重定向到index页面
            redirect: '/404',
        },




    ]
});

export default router;
