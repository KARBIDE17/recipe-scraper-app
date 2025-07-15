<template lang="pug">
section
  // Title
  .editable-block
    h1(v-if="!editing.title") {{ form.title }}
    input(v-else v-model="form.title")
    button(@click="toggleEdit('title')") {{ editing.title ? '✅' : 'Edit' }}

  // Ingredients
  .editable-block
    h2 Ingredients
    button(@click="toggleEdit('ingredients')") {{ editing.ingredients ? '✅' : 'Edit' }}
    ul(v-if="!editing.ingredients")
      li(v-for="(ing, i) in form.ingredients" :key="i") {{ ing }}
    textarea(
      v-else
      v-model="form.ingredientsText"
      rows="6"
    )

  // Instructions
  .editable-block
    h2 Instructions
    button(@click="toggleEdit('instructions')") {{ editing.instructions ? '✅' : 'Edit' }}
    ol(v-if="!editing.instructions")
      li(v-for="(step, i) in form.instructions" :key="i") {{ step }}
    textarea(
      v-else
      v-model="form.instructionsText"
      rows="8"
    )

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api'
import '@/assets/styles/fonts.scss'

const route = useRoute()
const router = useRouter()
const recipe = ref(null)

const editing = ref({
  title: false,
  ingredients: false,
  instructions: false,
})

const form = ref({
  title: '',
  ingredients: [],
  instructions: [],
  ingredientsText: '',
  instructionsText: ''
})

const fetchRecipe = async () => {
  const res = await api.get(`/recipes/${route.params.id}`)
  recipe.value = res.data
  form.value.title = res.data.name
  form.value.ingredients = res.data.ingredients
  form.value.instructions = res.data.instructions
  form.value.ingredientsText = res.data.ingredients.join('\n')
  form.value.instructionsText = res.data.instructions.join('\n')
}

const updateRecipe = async () => {
  await api.put(`/recipes/${route.params.id}`, {
    title: form.value.title,
    ingredients: form.value.ingredientsText.split('\n').map(s => s.trim()).filter(Boolean),
    instructions: form.value.instructionsText.split('\n').map(s => s.trim()).filter(Boolean)
  })
  await fetchRecipe()
}

const toggleEdit = async (field) => {
  if (editing.value[field]) {
    await updateRecipe()
  }
  editing.value[field] = !editing.value[field]
}
onMounted(fetchRecipe)
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

.editable-block {
  display: flex;
  flex-direction: row;
}
 button {
  height: 1.5rem;
  background-color: transparent;
  border: none;
  font-size: 1rem;
  margin-top: 1rem;
  text-decoration: underline;
 }

</style>