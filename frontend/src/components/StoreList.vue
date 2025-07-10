
<template lang="pug">
div
  h2 Stores
  ul(v-if="stores.length")
    li(v-for="store in stores" :key="store.id") {{ store.name }}
  p(v-else) Loading stores...

</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api'

const stores = ref([])

onMounted(async () => {
  try {
    const res = await api.get('/store')
    stores.value = res.data
  } catch (err) {
    console.error('Error fetching stores:', err)
  }
})
</script>
