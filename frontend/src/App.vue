<template lang="pug">
#app
  NavBar
  .appWrapper
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
  background-image: url('@/assets/bg.jpg');
  background-size: cover;
  overflow: hidden;
  z-index: -1;
}
#app {
  background-color: rgba(92, 92, 92, 0.379);
  border-radius: 1rem;
  z-index: 0;
}
h1 {
  margin-bottom: 1rem;
}
</style>
