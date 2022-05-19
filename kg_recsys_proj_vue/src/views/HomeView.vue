<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6" style="background-image: url('https://d3go.com/wp-content/themes/d3go/img/mtgpq_ogw_main_banner.jpg')">
      <div class="hero-body has-text-centered">
        <p class="title mb-6 has-text-black">
          Magic The Gathering Cards
        </p>
        <p class="subtitle has-text-black">
          Powered by KG-RecSys
        </p>
      </div>
    </section>
    
    
    <h2 class="is-size-2 has-text-centered">Recomended for you</h2>
     <carousel :items-to-show="5">
      <slide v-for="card in recomendedCards" 
          v-bind:key="card.id">
          <router-link v-bind:to="'/card/'+card.code"> <figure class="image mb-4">
            <img :src="card.image_url">
          </figure></router-link>
      </slide>

      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
      
      
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default {
  name: 'HomeView',
  data() {
    return {
      recomendedCards:[]
      }
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  mounted() {
    this.getrecomendedCards()
  },

  methods:{
    getrecomendedCards(){
      axios
        .get('/recomendedCards/1?max_len=20')
        .then(response => {
          console.log(response.data)
          this.recomendedCards = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }

}
</script>
