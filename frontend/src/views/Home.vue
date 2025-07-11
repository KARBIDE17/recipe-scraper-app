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

  form(@submit.prevent="extractFromText")
    textarea(
      v-model="manualText"
      placeholder="Paste a recipe’s title, ingredients, and instructions here..."
      rows="10"
      required
    )
    button(type="submit") Extract from Text
  
  p(v-if="loadingText") Extracting recipe...
  p(v-if="textMessage") {{ textMessage }}
  p(v-if="textError" style="color: red") {{ textError }}
  
</template>

<script setup>
import { ref } from 'vue'
import api from '@/api'

const url = ref('')
const loading = ref(false)
const message = ref('')
const error = ref('')
const manualText = ref('')
const loadingText = ref(false)
const textMessage = ref('')
const textError = ref('')

const extractRecipe = async () => {
  loading.value = true
  message.value = ''
  error.value = ''
  try {
    const res = await api.post('http://localhost:5005/extract-recipe', { url: url.value })
    message.value = `Recipe saved! ID: ${res.data.recipe_id}`
    url.value = ''
  } catch (err) {
    error.value = err.response?.data?.error || 'Something went wrong.'
  } finally {
    loading.value = false
  }
}

const extractFromText = async () => {
  loadingText.value = true
  textMessage.value = ''
  textError.value = ''

  try {
    const res = await api.post('/extract-text-recipe', { text: manualText.value })
    textMessage.value = res.data.message
    manualText.value = ''
  } catch (err) {
    textError.value = err.response?.data?.error || 'Failed to extract recipe.'
  } finally {
    loadingText.value = false
  }
}
</script>


<style scoped>
.home {
  padding: 2rem;
}
</style>
