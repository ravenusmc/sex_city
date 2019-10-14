<template>
  <div>

    <main>
      <h1 class='font center'>Study Area</h1>

      <section id='firstStudyArea'>

        <div>
        </div>

        <div class='form_div'>

          <form @submit="submitSelection">
            <h5 class='font'>Select Season:</h5>
            <select v-model="season" name="season">
              <option v-for="season in seasons" :value="season">{{ season }}</option>
            </select>&nbsp;
            <button type="submit">Submit</button>
          </form>

          <div>
            <p class='form_paragraph'>
              This area will show the user the number of times each character speaks
              on each season of Sex and the City. To use, select a season from the
              drop down above and hit submit. The graph will show the four
              main characters and how much each one spoke on the show / season that's
              been selected.
            </p>
          </div>

        </div>

      </section>

    </main>

  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Main',
  data(){
    return {
      season: 'Season 1',
      seasons: ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5', 'Season 6']
    }
  },
  methods: {
    ...mapActions([
      'fetchSeasonData',
    ]),
    submitSelection(evt){
      evt.preventDefault();
      const payload = {
        season: this.season,
      }
      this.fetchSeasonData({payload})
    }
  }
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

.form_div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* display: grid;
  grid-template-rows: 1fr 1fr;
  grid-gap: 1em;
  border: 2px solid red;  */
}

.form_paragraph {
  font-size: 20px;
}

</style>
