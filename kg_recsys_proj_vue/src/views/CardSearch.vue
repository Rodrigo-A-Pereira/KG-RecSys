<template>
    <div class="columns">
        <div class="column is-three-fifths is-offset-one-fifth">
            <h1 class="title">Search Results for "{{this.$route.query.name}}":</h1>
            <p class="">{{allCardResults.length}} results</p>

            <div 
                class="box cardWrpper columns"
                v-for="card in allCardResults"
                v-bind:key="card.code">
                <router-link to="/" class="column is-3"><img class="router-img" :src="card.image_url"></router-link>   
                
                <router-link v-bind:to="`/card/${card.code}`" class="column is-size-4">{{card.name}}</router-link>    
            </div>
        </div>
    </div>
    
</template>

<style lang="scss">
@import '../../node_modules/bulma';
@media screen and (min-width: 1088px){
 .router-img {
 }
}
</style>
<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'CardSearch',
  data() {
    return {
      allCardResults:[]
      }
  },
  components: {
  },
  mounted() {
    this.getCardsByName(this.$route.query.name)
  },

  methods:{
    getCardsByName(name){
      axios
        .get(`/card?name=${name}`)
        .then(response => {
          console.log(response.data)
          this.allCardResults = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }

}
</script>
