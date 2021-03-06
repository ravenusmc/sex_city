import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jsonp from 'jsonp';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    seasonSelected: {},
    seasonData: {},
    sentimentData: {},
  },

  getters: {
    seasonSelected: state => state.seasonSelected,
    seasonData: state => state.seasonData,
    sentimentData: state => state.sentimentData,
  },

  actions: {

    fetchInitialGraph: ({commit}, {payload}) => {
      const path = 'http://localhost:5000/seasonSpeachCount';
      axios.post(path, payload)
      .then((res) => {
        commit('setSeasonData', res.data);
      })
    },

    fetchSeasonData: ({commit}, {payload}) => {
      const path = 'http://localhost:5000/seasonSpeachCount';
      axios.post(path, payload)
      .then((res) => {
        commit('setSeasonData', res.data);
      })
    },

    fetchInitialSentimentGraph: ({commit}, {payload}) => {
      const path = 'http://localhost:5000/seasonSentimentData';
      axios.post(path, payload)
      .then((res) => {
        commit('setSentimentData', res.data);
      })
    },

    fetchSentimentData: ({commit}, {payload}) => {
      const path = 'http://localhost:5000/seasonSentimentData';
      axios.post(path, payload)
      .then((res) => {
        commit('setSentimentData', res.data);
      })
    }

  },

  mutations: {

    setSeasonData(state, data){
      state.seasonData = data
    },

    setSentimentData(state, data){
      state.sentimentData = data
    }

  },

});
