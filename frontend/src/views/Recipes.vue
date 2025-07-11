<template lang="pug">
section
  h1.text-2xl.font-bold.mb-4 All Recipes

  ul
    li(v-for="recipe in recipes" :key="recipe.id")
      router-link(:to="`/recipes/${recipe.id}`") {{ recipe.name }}
      button.text-red-600.ml-4(@click="handleDelete(recipe.id)") ✕

</template>

<script setup>
import { ref, onMounted } from 'vue'
import api, { deleteRecipe } from '@/api'

const recipes = ref([])

const fetchRecipes = async () => {
  try {
    const response = await api.get('/recipes')
    recipes.value = response.data
  } catch (error) {
    console.error('Error fetching recipes:', error)
  }
}

const handleDelete = async (id) => {
  const confirmed = confirm("Are you sure you want to delete this recipe?")
  if (!confirmed) return

  try {
    await deleteRecipe(id)
    recipes.value = recipes.value.filter(r => r.id !== id)
  } catch (error) {
    console.error('Error deleting recipe:', error)
  }
}


onMounted(fetchRecipes)
</script>