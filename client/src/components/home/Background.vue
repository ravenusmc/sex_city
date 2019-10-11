<template>
  <div>

    <h1 class='center font'>Background</h1>

    <section>

      <div class='textDiv'>
        <p>
          Yes, this may seem to be a joke but this project I felt would be a good practice
          in doing some stuff in Natural Language Processing. I found a dataset on Kaggle
          where someone broke down every line from Sex and the City and turned it into one
          massive dataset. I picture a project that will allow a user to see who had the
          most positive/negative lines per episode. It will also show which characters had
          the most lines for each season and episode.
        </p>
      </div>

      <div class='pictureDiv'>
      </div>

    </section>

  </div>
</template>

<script>
export default {
  name: 'Background',
}
</script>

<style scoped>

.center {
  text-align: center;
}

.font {
  font-family: 'Indie Flower', cursive;
  text-transform: uppercase;
}

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
  margin-top: 50px;
  margin-bottom: 50px;
  margin-left: 5%;
  margin-right: 5%;
  height: 300px;
}

section div {
  padding: 10px;
}

.textDiv {
  font-size: 20px;
}

.pictureDiv {
  background-image: url('../../assets/img/cityScene1.jpg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

</style>
