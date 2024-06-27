<template>
    <div ref="mapContainer" class="map-container"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import mapboxgl from 'mapbox-gl';
import '../../node_modules/mapbox-gl/dist/mapbox-gl.css';
mapboxgl.accessToken = 'pk.eyJ1IjoiamltaW5qaSIsImEiOiJjbHhscXI1N2IwMHFkMmhzZHdxMTg4ODQyIn0.aLsuiW6bBO37JH-ZYtZHwg';

// 使用 import 确保路径正确
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

const mapContainer = ref(null);


const stadiums = [
    { name: 'Emirates Stadium', coords: [-0.108611, 51.555], logo: arsenalImage },
    { name: 'Villa Park', coords: [-1.884722, 52.509167], logo: astonvillaImage },
    { name: 'Vitality Stadium', coords: [-1.8386, 50.7353], logo: bournemouthImage },
    { name: 'Brentford Community Stadium', coords: [-0.289048, 51.490715], logo: brentfordImage },
    { name: 'American Express Community Stadium', coords: [-0.083278, 50.861822], logo: brightonImage },
    { name: 'Turf Moor', coords: [-2.230278, 53.789167], logo: burnleyImage },
    { name: 'Stamford Bridge', coords: [-0.191111, 51.481667], logo: chelseaImage },
    { name: 'Selhurst Park', coords: [-0.085556, 51.398333], logo: crystalpalaceImage },
    { name: 'Goodison Park', coords: [-2.966389, 53.438889], logo: evertonImage },
    { name: 'Craven Cottage', coords: [-0.221667, 51.475], logo: fulhamImage },
    { name: 'Anfield', coords: [-2.96, 53.430819], logo: liverpoolImage },
    { name: 'Kenilworth Road', coords: [-0.430573, 51.883479], logo: lutonImage },
    { name: 'Etihad Stadium', coords: [-2.200292, 53.482989], logo: mancityImage },
    { name: 'Old Trafford', coords: [-2.291389, 53.463056], logo: manunitedImage },
    { name: 'St James Park', coords: [-1.621667, 54.975], logo: newcastleImage },
    { name: 'City Ground', coords: [-1.132778, 52.94], logo: nottinghamImage },
    { name: 'Bramall Lane', coords: [-1.469697, 53.370348], logo: sheffieldImage },
    { name: 'Tottenham Hotspur Stadium', coords: [-0.067007, 51.604252], logo: hotspurImage },
    { name: 'London Stadium', coords: [-0.017136, 51.538811], logo: westhamImage },
    { name: 'Molineux Stadium', coords: [-2.130278, 52.590278], logo: wolveImage }
];


import { useMapStore } from '../stores/mapStore';
const mapStore = useMapStore();
onMounted(() => {
    mapStore.initializeMap(mapContainer.value);
    mapStore.addMarkers(stadiums);
});

onUnmounted(() => {
    if (mapStore.map) {
        mapStore.map.remove();
    }
});


</script>

<style scoped>
.map-container {
    width: 90%;
    height: 80%;
    margin: auto;
    border: 5px solid #37003C;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);

}

.marker {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
