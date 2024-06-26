<template>
    <div id="goal-pie" class="chart"></div>
</template>

<script setup>
import { onMounted } from 'vue';
import * as echarts from 'echarts';

const goalData = [
    { value: 91, name: 'Arsenal' },
    { value: 76, name: 'Aston Villa' },
    { value: 54, name: 'Bournemouth' },
    { value: 56, name: 'Brentford' },
    { value: 55, name: 'Brighton' },
    { value: 41, name: 'Burnley' },
    { value: 77, name: 'Chelsea' },
    { value: 57, name: 'Crystal Palace' },
    { value: 40, name: 'Everton' },
    { value: 55, name: 'Fulham' },
    { value: 86, name: 'Liverpool' },
    { value: 52, name: 'Luton Town' },
    { value: 96, name: 'Manchester City' },
    { value: 67, name: 'Manchester United' },
    { value: 85, name: 'Newcastle United' },
    { value: 49, name: 'Nottingham Forest' },
    { value: 35, name: 'Sheffield United' },
    { value: 74, name: 'Tottenham Hotspur' },
    { value: 60, name: 'West Ham United' },
    { value: 50, name: 'Wolverhampton Wanderers' }
];

onMounted(() => {
    var chartDom = document.getElementById('goal-pie');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
        tooltip: {
            trigger: 'item'
        },
        series: [
            {
                name: '进球统计',
                type: 'pie',
                radius: ['20%', '70%'],
                roseType: 'radius',
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: 40,
                        fontWeight: 'bold'
                    }
                },
                data: goalData
            }
        ]
    };

    myChart.setOption(option);
});
</script>

<style scoped>
.chart {
    width: 1850px;
    height: 650px;
}
</style>
