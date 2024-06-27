<template>
    <div id="main"></div>
</template>

<script setup>
import { onMounted } from 'vue';
import * as echarts from 'echarts';

// 英超俱乐部名称
const names = [
    'Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton',
    'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham',
    'Liverpool', 'Luton Town', 'Man City', 'Man United',
    'Newcastle', 'Nottingham', 'Sheffield United', 'Hotspur',
    'West Ham', 'Wolve'
];



// 生成排名数据的函数
const generateRankingData = () => {
    const map = new Map();

    const rankingData = {
        'Arsenal': [4, 3, 5, 5, 4, 5, 3, 2, 3, 2, 4, 3, 1, 1, 1, 2, 1, 1, 2, 4, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2],
        'Man City': [3, 2, 1, 1, 1, 1, 1, 3, 2, 3, 1, 1, 2, 3, 4, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 1, 2, 2, 2, 1, 1, 1, 1],
        'Liverpool': [12, 5, 4, 3, 3, 2, 4, 4, 4, 4, 3, 2, 3, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3],
        'Aston Villa': [20, 9, 7, 10, 7, 6, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 3, 3, 3, 2, 4, 5, 4, 5, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4],
        'Bournemouth': [10, 14, 16, 16, 15, 17, 19, 19, 19, 17, 18, 17, 17, 17, 16, 15, 13, 13, 13, 13, 13, 13, 14, 14, 15, 14, 13, 13, 12, 12, 13, 10, 10, 10, 13, 13, 12, 12],
        'Hotspur': [9, 6, 3, 2, 2, 4, 2, 1, 1, 1, 2, 4, 5, 5, 5, 5, 5, 4, 5, 5, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5],
        'Chelsea': [11, 15, 10, 12, 14, 14,11, 11, 10, 11, 10, 10, 10, 10, 11, 13, 11, 11, 11, 10, 9, 10, 11, 10, 10, 11, 11, 11, 10, 9, 9, 9, 8, 8, 7, 7, 6, 6],
        'Newcastle': [1, 8, 13, 14, 12, 8, 8, 8, 6, 6, 6, 7, 7, 6, 7, 7, 6, 7, 9, 9, 10, 8, 9, 7, 8, 10, 8, 10, 8, 8, 8, 6, 7, 7, 6, 7, 7, 7],
        'Man United': [7, 12, 8, 11, 13, 9, 10, 10, 8, 8, 8, 6, 6, 7, 6, 6, 7, 8, 7, 8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 8, 8, 8, 8],
        'West Ham': [13, 7, 2, 4, 6, 7, 7, 7, 9, 9, 12, 9, 9, 9, 9, 9, 8, 6, 6, 6, 6, 6, 7, 8, 9, 8, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9, 9, 9],
        'Crystal Palace': [5, 11, 11, 7, 8, 9, 8, 8, 11, 13, 11, 13, 13, 13, 15, 16, 16, 16, 16, 15, 16, 15, 15, 16, 16, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 10],
        'Brighton': [2, 1, 6, 6, 5, 3, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 8, 7, 7, 9, 8, 9, 7, 7, 9, 8, 9, 9, 10, 10, 11, 12, 11, 10, 11, 11],
        'Fulham': [6, 13, 12, 13, 10, 11, 13, 12, 13, 14, 15, 16, 14, 15, 13, 11, 12, 14, 14, 14, 14, 14, 14, 12, 13, 12, 12, 12, 12, 12, 13, 13, 12, 13, 14, 14, 14, 13],
        'Wolve': [17, 19, 15, 15, 16, 16, 15, 14, 12, 12, 14, 12, 12, 14, 14, 14, 14, 12, 12, 11, 11, 11, 10, 11, 11, 9, 10, 9, 10, 11, 11, 11, 12, 11, 12, 14, 15, 14],
        'Everton': [15, 20, 20, 18, 18, 15, 16, 16, 16, 15, 16, 14, 18, 17, 17, 16, 15, 15, 15, 17, 17, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 16, 15, 15, 15, 15, 15],
        'Brentford': [8, 4, 9, 8, 11, 13, 14, 15, 14, 10, 9, 11, 11, 11, 12, 12, 13, 15, 17, 15, 16, 16, 15, 15, 16, 16, 16, 16, 16, 17, 16, 16, 16, 16, 16, 16, 16, 16],
        'Nottingham': [14, 10, 14, 9, 8, 12, 12, 13, 15, 16, 13, 15, 16, 16, 17, 17, 17, 17, 17, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17],
        'Luton Town': [18, 19, 19, 20, 18, 17, 17, 17, 18, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
        'Burnley': [19, 18, 20, 19, 19, 18, 18, 18, 19, 19, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19],
        'Sheffield': [16, 16, 17, 17, 17, 20, 20, 20, 20, 20, 20, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    };

    for (const [name, data] of Object.entries(rankingData)) {
        map.set(name, data);
    }

    return map;
};



// 生成系列列表的函数
const generateSeriesList = () => {
    const seriesList = [];
    const rankingMap = generateRankingData();
    const colors = [
        'red', 'rgb(25, 138, 179)', 'rgb(240, 37, 37)', 'rgb(93, 17, 93)', 'rgb(205, 7, 7)',
        'rgb(155, 155, 155)', 'blue', 'rgb(16, 12, 12)', 'rgb(240, 37, 37)', 'rgb(93, 45, 45)',
        'rgb(20, 39, 186)', 'rgb(8, 82, 241)', 'rgb(155, 155, 155)', 'rgb(222, 168, 4)', 'rgb(30, 6, 239)',
        'rgb(222, 4, 4)', 'rgb(191, 2, 94)', 'rgb(207, 93, 5)', 'rgb(63, 13, 63)', 'rgb(158, 59, 89)'
    ];

    let index = 0;
    rankingMap.forEach((data, name) => {
        const series = {
            name,
            symbolSize: 20,
            type: 'line',
            smooth: true,
            emphasis: {
                focus: 'series'
            },
            endLabel: {
                show: true,
                formatter: '{a}',
                distance: 20
            },
            lineStyle: {
                width: 4,
                color: colors[index % colors.length] // 设置颜色
            },
            itemStyle: {
                color: colors[index % colors.length] // 设置颜色
            },
            data
        };
        seriesList.push(series);
        index++;
    });
    return seriesList;
};





// 初始化图表的函数
const initChart = () => {
    const chartDom = document.getElementById('main');
    const myChart = echarts.init(chartDom);

    const option = {
        title: {
            text: 'Premier League Club Ranking Changes'
        },
        tooltip: {
            trigger: 'item'
        },
        grid: {
            left: 30,
            right: 110,
            bottom: 30,
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            splitLine: {
                show: true
            },
            axisLabel: {
                margin: 30,
                fontSize: 16
            },
            boundaryGap: false,
            data: Array.from({ length: 38 }, (_, i) => i + 1)  // 38 轮
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                margin: 30,
                fontSize: 16,
                formatter: '#{value}'
            },
            inverse: true,
            interval: 1,
            min: 1,
            max: names.length
        },
        series: generateSeriesList()
    };

    myChart.setOption(option);
};

// 在组件挂载时初始化图表
onMounted(() => {
    initChart();
});
</script>

<style scoped>
#main {
    width: 1850px;
    height: 650px;
}
</style>
