import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Recipes from '@/views/Recipes.vue'
import RecipeDetail from '@/views/RecipeDetail.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/recipes', component: Recipes },
  {
  path: '/recipes/:id',
  name: 'RecipeDetail',
  component: RecipeDetail,
  props: true
}

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
