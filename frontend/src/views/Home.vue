<template lang="pug">
#home
  h1 Add a Recipe by URL

  form(@submit.prevent="extractRecipe")
    input(
      v-model="url"
      type="text"
      placeholder="Paste a recipe URL here..."
      required
    )
    button(type="submit") Extract Recipe

  p(v-if="loading") Extracting recipe...
  p(v-if="message") {{ message }}
  p(v-if="error" style="color: red") {{ error }}
  router-link(to="/recipes") View Saved Recipes
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const url = ref('')
const loading = ref(false)
const message = ref('')
const error = ref('')

const extractRecipe = async () => {
  loading.value = true
  message.value = ''
  error.value = ''
  try {
    const res = await axios.post('http://localhost:5005/extract-recipe', { url: url.value })
    message.value = `Recipe saved! ID: ${res.data.recipe_id}`
    url.value = ''
  } catch (err) {
    error.value = err.response?.data?.error || 'Something went wrong.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.home {
  padding: 2rem;
}
</style>
