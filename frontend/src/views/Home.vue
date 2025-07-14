<template lang="pug">
#home
  h2 Add a Recipe by URL

  form.url-form(@submit.prevent="extractRecipe")
    input(
      v-model="url"
      type="text"
      placeholder="Paste a recipe URL here..."
      required
    )
    button(type="submit") Extract From URL

  p(v-if="loading") Extracting recipe...
  p(v-if="message") {{ message }}
  p(v-if="error" style="color: red") {{ error }}

  h2.mt-8 Add a Recipe Manually

  form.manual-form(@submit.prevent="extractFromSplitInputs")
    label.block.font-bold.mb-1 Title:
    input.mb-4.w-full.border(
      v-model="manualTitle"
      type="text"
      required
      placeholder="e.g. Grandma's Apple Pie"
    )

    label.block.font-bold.mb-1 Ingredients (one per line):
    textarea.mb-4.w-full.border(
      v-model="manualIngredients"
      rows="5"
      placeholder="1 cup sugar\n2 eggs\n..."
    )

    label.block.font-bold.mb-1 Instructions (one per line):
    textarea.mb-4.w-full.border(
      v-model="manualInstructions"
      rows="6"
      placeholder="1. Preheat oven to 350F\n2. Mix ingredients\n..."
    )

    button(type="submit") Extract from Form

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

const manualTitle = ref('')
const manualIngredients = ref('')
const manualInstructions = ref('')
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

const extractFromSplitInputs = async () => {
  loadingText.value = true
  textMessage.value = ''
  textError.value = ''

  const combinedText = `Title: ${manualTitle.value.trim()}\n\nIngredients:\n${manualIngredients.value.trim()}\n\nInstructions:\n${manualInstructions.value.trim()}`

  try {
    const res = await api.post('/extract-text-recipe', { text: combinedText })
    textMessage.value = res.data.message

    manualTitle.value = ''
    manualIngredients.value = ''
    manualInstructions.value = ''
  } catch (err) {
    textError.value = err.response?.data?.error || 'Failed to extract recipe.'
  } finally {
    loadingText.value = false
  }
}
</script>

<style scoped>
#home {
  padding: 2rem;
}

.manual-form {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  width: 60%;
}

button {
  background-color: #4a4a4a;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  margin: 0.5rem;
}

</style>
