// src/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5000', // Your Flask API base URL
})

// ITEMS
export const getItems = () => api.get('/item')
export const createItem = (item) => api.post('/item', item)
export const deleteItem = (id) => api.delete(`/item/${id}`)

// STORES
export const getStores = () => api.get('/store')
export const createStore = (store) => api.post('/store', store)

export default api
