<template lang="pug">
  form.form(@submit.prevent="submitItem")
    input(v-model="part_name" placeholder="Part Name" required)
    input(v-model="part_number" placeholder="Part Number" required)
    input(v-model.number="quantity" type="number" placeholder="Quantity" required)
    select(v-model.number="store_id" required)
      option(disabled value="") Select Store
      option(v-for="store in stores" :key="store.id" :value="store.id") {{ store.name }}
    button(type="submit") Add Item
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'

const part_name = ref('')
const part_number = ref('')
const quantity = ref(0)
const store_id = ref('')
const stores = ref([])

const emit = defineEmits(['item-added'])

onMounted(async () => {
  const res = await api.get('/store')
  stores.value = res.data
})

const submitItem = async () => {
  try {
    const response = await api.post('/item', {
      part_name: part_name.value,
      part_number: part_number.value,
      quantity: quantity.value,
      store_id: store_id.value
    })

    emit('item-added', response.data) // ← send new item to parent

    // Reset form fields
    part_name.value = ''
    part_number.value = ''
    quantity.value = 0
    store_id.value = ''
  } catch (err) {
    console.error('Error adding item:', err)
  }
}

</script>

<style scoped>
.form {
  margin: 1rem 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
</style>
