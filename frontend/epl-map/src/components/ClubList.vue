<template>
    <div v-if="selectedClub === null">
        <el-row :gutter="30">
            <el-col :span="6">
                <el-button class="grid-button button-arsenal" @click="selectClub('Arsenal', [-0.108611, 51.555])">
                    <div class=" button-content">
                        <img :src="arsenalImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">阿森纳</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-astonvilla"
                    @click="selectClub('Aston Villa', [-1.884722, 52.509167])">
                    <div class="button-content">
                        <img :src="astonvillaImage" alt="astonvilla" class="button-image">
                        <h1 class="button-text">阿斯顿维拉</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-bournemouth"
                    @click="selectClub('Bournemouth', [-1.8386, 50.7353])">
                    <div class="button-content">
                        <img :src="bournemouthImage" alt="bournemouth" class="button-image">
                        <h1 class="button-text">伯恩茅斯</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-brentford"
                    @click="selectClub('Brentford', [-0.289048, 51.490715])">
                    <div class="button-content">
                        <img :src="brentfordImage" alt="brentford" class="button-image">
                        <h1 class="button-text">布伦特福德</h1>
                    </div>
                </el-button>
            </el-col>
        </el-row>
        <el-row :gutter="30">
            <el-col :span="6">
                <el-button class="grid-button button-brighton"
                    @click="selectClub('Brighton & Hove Albion', [-0.083278, 50.861822])">
                    <div class="button-content">
                        <img :src="brightonImage" alt="brighton" class="button-image">
                        <h1 class="button-text">布莱顿</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-burnley" @click="selectClub('Burnley', [-2.230278, 53.789167])">
                    <div class="button-content">
                        <img :src="burnleyImage" alt="burnley" class="button-image">
                        <h1 class="button-text">伯恩利</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-chelsea" @click="selectClub('Chelsea', [-0.191111, 51.481667])">
                    <div class="button-content">
                        <img :src="chelseaImage" alt="chelsea" class="button-image">
                        <h1 class="button-text">切尔西</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-crystalpalace"
                    @click="selectClub('Crystal Palace', [-0.085556, 51.398333])">
                    <div class="button-content">
                        <img :src="crystalpalaceImage" alt="crystalpalace" class="button-image">
                        <h1 class="button-text">水晶宫</h1>
                    </div>
                </el-button>
            </el-col>
        </el-row>
        <el-row :gutter="30">
            <el-col :span="6">
                <el-button class="grid-button button-everton" @click="selectClub('Everton', [-2.966389, 53.438889])">
                    <div class="button-content">
                        <img :src="evertonImage" alt="everton" class="button-image">
                        <h1 class="button-text">埃弗顿</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-fulham" @click="selectClub('Fulham', [-0.221667, 51.475])">
                    <div class="button-content">
                        <img :src="fulhamImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">富勒姆</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-liverpool" @click="selectClub('Liverpool', [-2.96, 53.430819])">
                    <div class="button-content">
                        <img :src="liverpoolImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">利物浦</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-luton" @click="selectClub('Luton Town', [-0.430573, 51.883479])">
                    <div class="button-content">
                        <img :src="lutonImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">卢顿</h1>
                    </div>
                </el-button>
            </el-col>
        </el-row>
        <el-row :gutter="30">
            <el-col :span="6">
                <el-button class="grid-button button-mancity"
                    @click="selectClub('Manchester City', [-2.200292, 53.482989])">
                    <div class="button-content">
                        <img :src="mancityImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">曼城</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-manunited"
                    @click="selectClub('Manchester United', [-2.291389, 53.463056])">
                    <div class="button-content">
                        <img :src="manunitedImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">曼联</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-newcastle"
                    @click="selectClub('Newcastle United', [-1.621667, 54.975])">
                    <div class="button-content">
                        <img :src="newcastleImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">纽卡斯尔联</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-nottingham"
                    @click="selectClub('Nottingham Forest', [-1.132778, 52.94])">
                    <div class="button-content">
                        <img :src="nottinghamImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">诺丁汉森林</h1>
                    </div>
                </el-button>
            </el-col>
        </el-row>
        <el-row :gutter="30">
            <el-col :span="6">
                <el-button class="grid-button button-sheffield"
                    @click="selectClub('Sheffield United', [-1.469697, 53.370348])">
                    <div class="button-content">
                        <img :src="sheffieldImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">谢菲尔德联</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-hotspur"
                    @click="selectClub('Tottenham Hotspur', [-0.067007, 51.604252])">
                    <div class="button-content">
                        <img :src="hotspurImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">托特纳姆热刺</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-westham"
                    @click="selectClub('West Ham United', [-0.017136, 51.538811])">
                    <div class="button-content">
                        <img :src="westhamImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">西汉姆联</h1>
                    </div>
                </el-button>
            </el-col>
            <el-col :span="6">
                <el-button class="grid-button button-wolve"
                    @click="selectClub('Wolvehampton Wanderers', [-2.130278, 52.590278])">
                    <div class="button-content">
                        <img :src="wolveImage" alt="Arsenal" class="button-image">
                        <h1 class="button-text">狼队</h1>
                    </div>
                </el-button>
            </el-col>
        </el-row>
    </div>

    <el-scrollbar v-if="selectedClub === 'Arsenal'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Arsenal />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Aston Villa'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Astonvilla />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Bournemouth'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Bournemouth />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Brentford'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Brentford />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Brighton & Hove Albion'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Brighton />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Burnley'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Burnley />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Chelsea'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Chelsea />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Crystal Palace'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Crystal />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Everton'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Everton />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Fulham'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Fulham />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Liverpool'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Liverpool />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Luton Town'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Luton />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Manchester City'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Mancity />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Manchester United'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <ManUnited />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Newcastle United'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Newcastle />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Nottingham Forest'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Nottingham />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Sheffield United'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Sheffield />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Tottenham Hotspur'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Hotspur />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'West Ham United'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Westham />
        </div>
    </el-scrollbar>

    <el-scrollbar v-if="selectedClub === 'Wolvehampton Wanderers'" style="width: 100%; height: 90%;">
        <h1 style="font-size: 30px;">{{ selectedClub }}</h1>
        <div>
            <Wolve />
        </div>
    </el-scrollbar>
</template>

<script setup>
import arsenalImage from '../assets/ClubLogo/arsenal.png';
import astonvillaImage from '../assets/ClubLogo/astonvilla.png';
import bournemouthImage from '../assets/ClubLogo/bournemouth.png';
import brentfordImage from '../assets/ClubLogo/Brentford.png';
import brightonImage from '../assets/ClubLogo/Brighton.png';
import burnleyImage from '../assets/ClubLogo/burnley.png';
import chelseaImage from '../assets/ClubLogo/chelsea.png';
import crystalpalaceImage from '../assets/ClubLogo/crystalpalace.png';
import evertonImage from '../assets/ClubLogo/everton.png';
import fulhamImage from '../assets/ClubLogo/fulham.png';
import liverpoolImage from '../assets/ClubLogo/liverpool.png';
import lutonImage from '../assets/ClubLogo/luton.png';
import mancityImage from '../assets/ClubLogo/mancity.png';
import manunitedImage from '../assets/ClubLogo/manunited.png';
import newcastleImage from '../assets/ClubLogo/newcastle.png';
import nottinghamImage from '../assets/ClubLogo/nottingham.png';
import sheffieldImage from '../assets/ClubLogo/sheffield.png';
import hotspurImage from '../assets/ClubLogo/hotspur.png';
import westhamImage from '../assets/ClubLogo/westham.png';
import wolveImage from '../assets/ClubLogo/wolve.png';

import Arsenal from './ClubsInfo/Arsenal.vue';
import Astonvilla from './ClubsInfo/Astonvilla.vue';
import Bournemouth from './ClubsInfo/Bournemouth.vue';
import Brentford from './ClubsInfo/Brentford.vue';
import Brighton from './ClubsInfo/Brighton.vue';
import Burnley from './ClubsInfo/Burnley.vue';
import Chelsea from './ClubsInfo/Chelsea.vue';
import Crystal from './ClubsInfo/Crystal.vue';
import Everton from './ClubsInfo/Everton.vue';
import Fulham from './ClubsInfo/Fulham.vue';
import Liverpool from './ClubsInfo/Liverpool.vue';
import Luton from './ClubsInfo/Luton.vue';
import Mancity from './ClubsInfo/Mancity.vue';
import ManUnited from './ClubsInfo/ManUnited.vue';
import Newcastle from './ClubsInfo/Newcastle.vue';
import Nottingham from './ClubsInfo/Nottingham.vue';
import Sheffield from './ClubsInfo/Sheffield.vue';
import Hotspur from './ClubsInfo/Hotspur.vue';
import Westham from './ClubsInfo/Westham.vue';
import Wolve from './ClubsInfo/Wolve.vue';



import { ref } from 'vue'
import { useEPLstateStore } from '../stores/eplstate';
import { storeToRefs } from 'pinia';
import { useMapStore } from '../stores/mapStore';
const store = useEPLstateStore();
const { selectedClub } = storeToRefs(store)

const mapStore = useMapStore();
const selectClub = (club, coords) => {
    selectedClub.value = club;
    mapStore.flyToStadium(coords);
};


</script>

<style scoped>
@import '../assets/css/clublist.css';
</style>