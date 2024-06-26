<template>
  <div class="layout">
    <el-container>
      <el-header height="8vh">
        <Menu />
      </el-header>
      <el-container class="upper-container">
        <el-aside width="45vw" class="map-aside">
          <Mapbox />
        </el-aside>
        <el-main>
          <ClubList />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import Mapbox from './components/Mapbox.vue'
import Menu from './components/Menu.vue'
import ClubList from './components/ClubList.vue'
import axios from 'axios'
import { ref, onMounted } from 'vue'

</script>

<style scoped>
.el-container {
  height: 100vh;
}

.el-aside,
.el-main {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.el-header {
  padding: 0;
}

.upper-container {
  height: 92vh;
}



</style>
