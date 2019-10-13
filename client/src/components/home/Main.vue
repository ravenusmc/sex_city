<template>
  <div>

    <main>
      <h1 class='font center'>Study Area</h1>

      <section id='firstStudyArea'>

        <div>
        </div>

        <div>
          <form>
          </form>
        </div>

      </section>

    </main>

  </div>
</template>

<script>
export default {
  name: 'Main'
}
</script>

<style scoped>

.center {
  text-align: center;
}

.font {
  font-family: 'Indie Flower', cursive;
}

main {
  margin-top: 50px;
}

#firstStudyArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
  border: 2px solid black;
}

</style>
