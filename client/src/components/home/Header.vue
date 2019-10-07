<template>
  <div>

    <header>
      <div class='homeHeader'>
        <h1 class='font headerTitle'>Sex and the City Study</h1>
      </div>
    </header>

  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>

.font {
  font-family: 'Indie Flower', cursive;
}

header {
  background-image: url('../../assets/img/header_image.jpg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  height: 600px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

}

.homeHeader {
  border-radius: 10px;
  padding: 25px;
  background-color: rgba(0, 0, 0, 0.7);
  border: 2px solid black;
}

.headerTitle {
  text-transform: uppercase;
  color: white;
}
</style>
