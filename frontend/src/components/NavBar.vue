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
}

.nav-link {
  color: white;
  text-decoration: none;
  font-family: Gin;
  font-weight: bold;
  font-size: 2rem;
  margin-right: 1rem;
}

.nav-link.router-link-exact-active {
  text-decoration: underline;
  text-underline-position: above;
}
</style>
