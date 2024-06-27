// src/stores/mapStore.js
import { defineStore } from 'pinia';
import mapboxgl from 'mapbox-gl';
import { ref } from 'vue';

export const useMapStore = defineStore('mapStore', () => {
  const map = ref(null);

  const initializeMap = (container, center = [-1.1743, 52.9], zoom = 6) => {
    map.value = new mapboxgl.Map({
      container: container,
      style: "mapbox://styles/mapbox/streets-v12",
      center: center,
      zoom: zoom,
    });
  };

  const addMarkers = (stadiums) => {
    stadiums.forEach(stadium => {
      const el = document.createElement('div');
      el.className = 'marker';
      el.style.backgroundImage = `url(${stadium.logo})`;
      el.style.width = '50px';
      el.style.height = '50px';
      el.style.backgroundSize = 'cover';
      el.style.borderRadius = '50%';

      new mapboxgl.Marker(el)
        .setLngLat(stadium.coords)
        .setPopup(new mapboxgl.Popup({ offset: 25 }).setText(stadium.name))
        .addTo(map.value);
    });
  };

  const flyToStadium = (coords) => {
    if (map.value) {
      map.value.flyTo({
        center: coords,
        zoom: 16,
        essential: true
      });
    }
  };

  const flyToOverview = () => {
    if (map.value) {
      map.value.flyTo({
        center: [-1.1743, 52.9],
        zoom: 6,
        essential: true
      });
    }
  }

  return {
    map,
    initializeMap,
    addMarkers,
    flyToStadium,
    flyToOverview
  };
});
