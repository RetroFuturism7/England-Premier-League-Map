import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import Papa from 'papaparse'


export const useEPLstateStore = defineStore('eplstate', () => {
  //选中状态
  const selectedClub = ref(null)

  

  return { selectedClub }
})
