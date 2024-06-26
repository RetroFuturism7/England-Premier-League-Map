<template>
    <el-menu class="header-menu" mode="horizontal" :ellipsis="false" @select="handleSelect">
        <el-menu-item index="0" @click="BackHome">
            <img style="width: 50px" src="../assets/ClubLogo/pl-main-logo.png" alt="Element logo" />
            英超联赛俱乐部地图
        </el-menu-item>
        <div class="flex-grow" />
        <el-menu-item index="1" @click="TableDrawer = true">积分榜</el-menu-item>
        <el-menu-item index="2" @click="ChartDrawer = true">数据图表</el-menu-item>

    </el-menu>

    <el-drawer v-model="TableDrawer" :with-header="false" direction="ltr" size="45%">
        <el-scrollbar>
            <div id="tour_standings" v-html="PointTable" height="100%"></div>
        </el-scrollbar>
    </el-drawer>

    <el-drawer v-model="ChartDrawer" :with-header="false" direction="btt" size="80%">
        <el-tabs v-model="activeName" class="chart-tabs" @tab-click="handleClick">
            <el-tab-pane label="排名变化图" name="first">
                <div class="chart-container">
                    <RatingChange />
                </div>
            </el-tab-pane>
            <el-tab-pane label="进球统计" name="second">
                <div>
                    <GoalPie />
                </div>
            </el-tab-pane>
            <el-tab-pane label="更多.." name="third">
                <el-empty description="待开发" />
            </el-tab-pane>
        </el-tabs>
    </el-drawer>
</template>

<script setup>
import { ref } from 'vue'
import { useEPLstateStore } from '../stores/eplstate';
import { storeToRefs } from 'pinia';
import { useMapStore } from '../stores/mapStore';


import RatingChange from './chart/RatingChange.vue'
import GoalPie from './chart/GoalPie.vue'

//导航栏
const activeIndex = ref('1')
function handleSelect(key, keyPath) {
    console.log(key, keyPath);
}


//积分榜（drawer)
const TableDrawer = ref(false)
const PointTable = ref("<iframe src='https://www.aiscore.com/zht/tournament-english-premier-league/mo07dni2vfxknxy/standings/4ndqmliezotlkve?isplugin=true'  height='1176' width='100%' scrolling='auto' border='0' frameborder='0'></iframe>");


//控制俱乐部信息页面相关
const store = useEPLstateStore();
const { selectedClub } = storeToRefs(store)
const mapStore = useMapStore();
const BackHome = () => {
    selectedClub.value = null
    mapStore.flyToOverview()
}

//控制图表页面相关
const ChartDrawer = ref(false)
const activeName = ref('first')

const handleClick = (tab, event) => {
    console.log(tab, event)
}
</script>

<style scoped>
.header-menu {
    width: 100%;
}

.flex-grow {
    flex-grow: 1;
}

.el-tabs__content {
    height: 100%;
}

.el-tab-pane {
    height: 100%;
}

.chart-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}
</style>
