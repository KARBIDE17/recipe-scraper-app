<template lang="pug">
section
  h1.text-2xl.font-bold.mb-4 All Recipes

  ul
    li(v-for="recipe in recipes" :key="recipe.id")
      router-link(:to="`/recipes/${recipe.id}`") {{ recipe.name }}
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const recipes = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:5005/recipes')
    recipes.value = response.data
  } catch (error) {
    console.error('Error fetching recipes:', error)
  }
})
</script>
