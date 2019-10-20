<template>
  <div>

    <main>
      <h1 class='font center'>First Study Area</h1>

      <!-- First study area -->
      <section id='firstStudyArea'>

        <div>
          <GraphCard
            :typeOne='typeOne'
            :data='seasonData'
            :options='chartOptionsSeasonLinesChart'>
          </GraphCard>
        </div>

        <div class='form_div'>

          <form @submit="submitSelection">
            <h3 class='font'>Select Season:</h3>
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
      <!-- End of first study area -->

      <h1 class='font center'>Second Study Area</h1>

      <!-- Second study area -->
      <section id='secondStudyArea'>

        <div>
          <img :src="image" alt='Word Cloud'>
        </div>

        <div class='form_div'>

          <form @submit="changeWordCloud">
            <h3 class='font'>Select Season:</h3>
            <select v-model="season" name="season">
              <option v-for="season in seasons" :value="season">{{ season }}</option>
            </select>&nbsp;
            <button type="submit">Submit</button>
          </form>

          <div>
            <p class='form_paragraph'>
              This area will allow the user to select a season and then see a
              word cloud that will show the most common words from that season. The
              word cloud comes from every line that was spoken in the season.
            </p>
          </div>

        </div>

      </section>
      <!-- End of second study area -->

      <h1 class='font center'>Third Study Area</h1>

      <!-- Third study area -->
      <section id='thirdStudyArea'>

        <div>
        </div>

        <div class='form_div'>

        </div>

      </section>

    </main>
    <!-- End of third study area -->

  </div>
</template>

<script>
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';
import GraphCard from '@/components/graphs/Graphcard.vue';
import Image1 from '@/assets/img/season1.png';
import Image2 from '@/assets/img/season2.png';
import Image3 from '@/assets/img/season3.png';
import Image4 from '@/assets/img/season4.png';
import Image5 from '@/assets/img/season5.png';
import Image6 from '@/assets/img/season6.png';

export default {
  name: 'Main',
  components: {
    GraphCard,
  },
  data(){
    return {
      season: '1',
      seasons: ['1', '2', '3', '4', '5', '6'],
      typeOne: "BarChart",
      image: Image1,
      image2: Image2,
      chartOptionsSeasonLinesChart: {
        title: 'Lines By Season By Character',
        legend: { position: 'bottom' },
        'height':300,
        vAxis: { viewWindow: {
          min:0
        }}
      },
    }
  },
  computed: {
    ...mapGetters([
      'seasonData',
    ]),
  },
  methods: {
    ...mapActions([
      'fetchSeasonData',
      'fetchInitialGraph'
    ]),
    submitSelection(evt){
      evt.preventDefault();
      const payload = {
        season: this.season,
      }
      this.fetchSeasonData({payload})
    },
    changeWordCloud(evt) {
      evt.preventDefault();
      if (this.season === '1'){
        this.image = Image1
      }else if (this.season === '2'){
        this.image = Image2
      }else if (this.season === '3'){
        this.image = Image3
      }else if (this.season === '4'){
        this.image = Image4
      }else if (this.season === '5'){
        this.image = Image5
      }else if (this.season === '6'){
        this.image = Image6
      }
    }
  },
  mounted() {
    const payload = {
      season: 1
    }
    this.fetchInitialGraph({payload})
  },
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

main {
  margin-top: 50px;
}

#firstStudyArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
}

.form_div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form_paragraph {
  font-size: 20px;
  margin-left: 3%;
  margin-right: 3%;
}

button {
  background-color: #d62a5e;
  color: white;
  border: #d62a5e;
  padding: 8px;
  border-radius: 10px;
}

button:hover {
  background-color: #de547d;
  border: #de547d;
}

#secondStudyArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
  margin-left: 5%;
  margin-right: 5%;
}

img {
  height: 300px;
}

#thirdStudyArea {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
  margin-left: 5%;
  margin-right: 5%;
}

@media only all and (max-width: 975px) {

  #firstStudyArea {
    grid-template-columns: 1fr;
  }

  #secondStudyArea {
    grid-template-columns: 1fr;
  }

}

</style>
