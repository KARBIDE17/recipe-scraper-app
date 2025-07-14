<template lang="pug">
section
  h1.text-2xl.font-bold.mb-2 {{ recipe.name }}

  h2.text-xl.mt-4 Ingredients
  ul.list-disc.pl-5
    li(v-for="ing in recipe.ingredients" :key="ing") {{ ing }}

  h2.text-xl.mt-4 Instructions
  ol.list-decimal.pl-5
    li(v-for="step in recipe.instructions" :key="step") {{ step }}
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/api'

const route = useRoute()
const recipe = ref({
  name: '',
  ingredients: [],
  instructions: []
})

onMounted(async () => {
  try {
    const response = await api.get(`http://localhost:5005/recipes/${route.params.id}`)
    recipe.value = response.data
  } catch (error) {
    console.error('Error fetching recipe:', error)
  }
})
</script>

<style scoped>
section {
  padding: 2rem;
}
</style>