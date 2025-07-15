<template lang="pug">
#app
  NavBar
  .appWrapper
    router-view
</template>

<script setup>
import { ref, onMounted } from 'vue'
import AddItemForm from './components/AddItemForm.vue'
import ItemList from './components/ItemList.vue'
import NavBar from './components/NavBar.vue'
import { getItems, deleteRecipe } from '@/api'
import '@/assets/styles/fonts.scss'

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
section {
 
}

#body {
  font-family: Helvetica, Arial, sans-serif;
  margin: 2rem;
  background-image: url('@/assets/bg.jpg');
  background-color: rgba(92, 92, 92, 0.479);
  background-size: cover;
  overflow: hidden;
  margin-top: 2rem;
  height: auto;
}
#app {
  background-color: rgba(92, 92, 92, 0.6);
  height: auto;
}
.app-wrapper {
  background-color: rgba(255, 255, 255, 0.85);
  min-height: 100vh;
  padding: 2rem;
}

</style>
