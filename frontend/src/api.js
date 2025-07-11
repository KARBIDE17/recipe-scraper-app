// src/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5005', // Your Flask API base URL
})

// ITEMS
export const getItems = () => api.get('/item')
export const createItem = (item) => api.post('/item', item)
// RECIPES
export const deleteRecipe = (id) => api.delete(`/recipes/${id}`)


// STORES
export const getStores = () => api.get('/store')
export const createStore = (store) => api.post('/store', store)

export default api
