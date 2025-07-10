<template lang="pug">
div
  h2 Items by Store
  div(v-for="(storeItems, storeName) in groupedItems" :key="storeName")
    h3 {{ storeName }}
    table
      thead
        tr
          th Part Name
          th Part Number
          th Quantity
          th Actions
      tbody
        tr(v-for="item in storeItems" :key="item.id")
          td {{ item.part_name }}
          td {{ item.part_number }}
          td {{ item.quantity }}
          td
            button(@click="$emit('delete-item', item.id)") Delete
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  items: {
    type: Array,
    required: true
  }
})

defineEmits(['delete-item'])

const groupedItems = computed(() => {
  const grouped = {}
  for (const item of props.items) {
    const storeName = item.store_name || 'Unknown Store'
    if (!grouped[storeName]) grouped[storeName] = []
    grouped[storeName].push(item)
  }
  return grouped
})
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 2rem;
}
th, td {
  padding: 0.5rem;
  border: 1px solid #ccc;
}
h3 {
  margin-top: 1.5rem;
}
</style>
