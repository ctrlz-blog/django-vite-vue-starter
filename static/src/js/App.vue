<script setup>
import Counter from "./Counter.vue"
</script>

<template>
    <h1>{{message}}</h1>
    <counter />
    <button>
        <a :href="url">Click me</a>
    </button>
    
</template>

<script>
export default {
  components: { Counter },
  data() {
    return {
      message: JSON.parse(document.getElementById("vue-message").textContent),
      url: JSON.parse(document.getElementById("url").textContent)
    };
  },
};
</script>