<template>
    <el-table :data="processedMatches" >
        <el-table-column prop="Date" label="日期"></el-table-column>
        <el-table-column prop="HomeTeam" label="主队"></el-table-column>
        <el-table-column label="比分" width="180">
            <template #default="{ row }">
                <el-tag :type="getTagType(row.Result)" effect="dark">
                    {{ row.Score }}
                </el-tag>
            </template>
        </el-table-column>
        <el-table-column prop="AwayTeam" label="客队"></el-table-column>
    </el-table>
</template>

<script setup>
import { useEPLstateStore } from '../../stores/eplstate';
import { storeToRefs } from 'pinia';
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'

const store = useEPLstateStore();



const ArsMatches = ref([])
const getARSMatches = async () => {
    const path = 'http://localhost:5000/api/matchesdata/Arsenal';
    try {
        const res = await axios.get(path);
        ArsMatches.value = res.data;
        console.log('阿森纳',ArsMatches.value);
    } catch (error) {
        console.error(error);
    }
}

onMounted(getARSMatches);



const processedMatches = computed(() => {
    return ArsMatches.value.map(match => {
        if (match.Venue === 'Home') {
            return {
                Date: match.Date,
                HomeTeam: match.Team,
                Score: `${match.GF} - ${match.GA}`,
                AwayTeam: match.Opponent,
                Result: match.Result
            };
        } else {
            return {
                Date: match.Date,
                HomeTeam: match.Opponent,
                Score: `${match.GA} - ${match.GF}`,
                AwayTeam: match.Team,
                Result: match.Result
            };
        }
    });
});



const getTagType = (result) => {
    if (result === 'W') {
        return 'danger';
    } else if (result === 'L') {
        return 'info';
    } else {
        return 'success';
    }
};

</script>

<style scoped>
.el-table {
    width: 100%;
    height: auto;
}


</style>