import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    seasonSelected: {},
    seasonData: {},
  },

  getters: {
    seasonSelected: state => state.seasonSelected,
    seasonData: state => state.seasonData,
  },

  actions: {

    fetchSeasonData: ({commit}, {payload}) => {
      const path = 'http://localhost:5000/seasonSpeachCount';
      axios.post(path, payload)
      .then((res) => {
        commit('setSeasonData', res.data);
      })
    }

  },

  mutations: {

    setSeasonData(state, data){
      state.seasonData = data
    }
    
  },

});
