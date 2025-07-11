<template lang="pug">
#app
  NavBar
  h1 Recipe Scraper
  router-view
</template>

<script setup>
import { ref, onMounted } from 'vue'
import AddItemForm from './components/AddItemForm.vue'
import ItemList from './components/ItemList.vue'
import NavBar from './components/NavBar.vue'
import { getItems, deleteRecipe } from '@/api'

const items = ref([])

const fetchItems = async () => {
  try {
    const response = await getItems()
    items.value = response.data
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}

const handleDelete = async (id) => {
  try {
    await deleteRecipe(id)
    await fetchItems()
  } catch (error) {
    console.error('Error deleting item:', error)
  }
}

onMounted(fetchItems)
</script>

<style>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 2rem;
}
h1 {
  margin-bottom: 1rem;
}
</style>
