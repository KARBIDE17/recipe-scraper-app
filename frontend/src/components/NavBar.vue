<template lang="pug">
nav.navbar
  router-link.nav-link(to="/" exact) Home
  router-link.nav-link(to="/recipes") Recipes
</template>

<style scoped>
.navbar {
  background-color: #333;
  padding: 1rem;
  display: flex;
  gap: 1rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-link.router-link-exact-active {
  text-decoration: underline;
}
</style>
