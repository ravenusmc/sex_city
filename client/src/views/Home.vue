<template>
  <div>
    <Header />
    <Background />
  </div>
</template>

<script>
import Header from '@/components/home/Header.vue';
import Background from '@/components/home/Background.vue';

export default {
  name: 'home',
  components: {
    Header,
    Background
  },
};
</script>
