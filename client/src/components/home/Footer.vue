<template>
  <div>

    <footer>
       <p class='center font'>Copyright © 2019 Double Sun Productions</p>
    </footer>

  </div>
</template>

<script>
export default {
  name: 'Footer',
}
</script>

<style scoped>
.center {
  text-align: center;
}

.font {
  font-family: 'Indie Flower', cursive;
  text-transform: uppercase;
  font-size: 30px;
}

footer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 100px;
  background-color: #d62a5e;
  height: 400px;
}

</style>
