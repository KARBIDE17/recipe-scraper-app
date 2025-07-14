<template lang="pug">
section
  h1.text-2xl.font-bold.mb-4 All Recipes

  ul
    li(v-for="recipe in recipes" :key="recipe.id")
      .left
        router-link(:to="`/recipes/${recipe.id}`") {{ recipe.name }}
      .right
        button.edit-button(@click="editRecipe(`/recipes/${recipe.id}`)") EDIT
        button.delete-button(@click="handleDelete(recipe.id)") DELETE X

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

<style scoped>

section {
  padding: 2rem;
}

h1 {
  font-family: 'Bungee', sans-serif;
}

li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 0;
  font-size: 2rem;
  border-bottom: grey 1px solid;
  margin-bottom: 2rem;
  font-family: 'Gin';
}

.left {
  flex: 1;
}

.right {
  display: flex;
  margin-right: 1rem;
}

.edit-button,
.delete-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
}

.edit-button {
  color: #3490dc;
  margin-right: 2rem;
}

.delete-button {
  color: #e3342f;
}

a {
  text-decoration: none;
  color: #1a202c;
  text-decoration: underline;
}


</style>