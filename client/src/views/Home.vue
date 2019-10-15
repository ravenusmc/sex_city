<template>
  <div>
    <Header />
    <Background />
    <Main />
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/home/Header.vue';
import Background from '@/components/home/Background.vue';
import Main from '@/components/home/Main.vue';
import Footer from '@/components/home/Footer.vue';

export default {
  name: 'home',
  components: {
    Header,
    Background,
    Main,
    Footer,
  },
};
</script>
