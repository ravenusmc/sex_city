import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    seasonSelected: {},
  },

  getters: {
    seasonSelected: state => state.seasonSelected,
  },

  actions: {

    fetchSeasonData: ({commit}, {payload}) => {
      const path = 'http://localhost:5000/seasonSpeachCount';
      axios.post(path, payload)
      .then((res) => {
        console.log(res.data)
        //commit('setDeathData', res.data);
      })
    }

  },

  mutations: {

  },

});
