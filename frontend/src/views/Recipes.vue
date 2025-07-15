<template lang="pug">
section
  h1 All Recipes
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
  padding: 2rem 2rem 2rem 2rem;
}

h1 {
  font-size: 2.5rem;
  font-family: Bungee;
  box-sizing: border-box;
  margin: 0 0 1rem 0;
  color: #1d1d1d;
  line-height: 2.5rem;
}

li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  /* padding: 0.5rem 0; */
  font-size: 2rem;
  border-bottom: grey 1px solid;
  margin-bottom: 2rem;
  font-family: 'Gin';
  color: #1d1d1d;
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
  background-color: #5a5c5d;
  border: solid 1px #000000;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 1);
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-size: 1.2rem;
}

.edit-button {
  color: #363839;
  margin-right: 2rem;
}

.delete-button {
  color: #e3342f;
}

a {
  text-decoration: none;
  color: #1d1d1d;
  text-decoration: underline;
}


</style>