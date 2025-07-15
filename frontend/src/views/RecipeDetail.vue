<template lang="pug">
section
  h1 {{ recipe.name }}

  h2 Ingredients
  ul
    li(v-for="ing in recipe.ingredients" :key="ing") {{ ing }}

  h2 Instructions
  ol
    li(v-for="step in recipe.instructions" :key="step") {{ step }}
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/api'
import '@/assets/styles/fonts.scss'

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

h1 {
  font-size: 2.5rem;
  font-family: Bungee;
  box-sizing: border-box;
  margin: 0 0 1rem 0;
  color: #1d1d1d;
  line-height: 2.5rem;
}

h2 {
  font-size: 2rem;
  font-family: Gin;
  margin: 1rem 0;
  color:#1d1d1d;
}

li {
  font-size: 1.2rem;
  margin: 0.5rem 0;
  font-family: Gin;
}
</style>