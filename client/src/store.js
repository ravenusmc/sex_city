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
      console.log(payload)
      console.log('Mike')
    }

  },

  mutations: {

  },

});
