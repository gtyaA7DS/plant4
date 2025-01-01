<script setup>
import { ref } from 'vue';

import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: '家',
        items: [{ label: '首页', icon: 'pi pi-fw pi-home', to: '/' }]
    },
    {
        label: '细节',
        items: [

            { label: '控制', icon: 'pi pi-fw pi-clone', to: '/detail/control' },

            { label: '环境数据趋势', icon: 'pi pi-fw pi-chart-bar', to: '/detail/charts' },

        ]
    },




]);
</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>

    </ul>
</template>

<style lang="scss" scoped></style>
