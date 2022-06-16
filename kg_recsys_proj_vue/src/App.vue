<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>RecSys</strong></router-link>
      </div>

      <div class="navbar-menu">
        <div class="navbar-start"></div>
        <div class = "navbar-center">
          <div class="navbar-item" style="flex-grow:1">
            <form class="search-form" style="flex-grow:1" @submit="submit()">
              <input class="input" type="text" placeholder="Card Name" name="name" v-model="name">
            </form>
          </div>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <UserDrop/>
          </div>
           

          
          

  
        </div>

      </div>

    </nav>
    <section class="section">
      <router-view/>
    </section>

    <footer class ="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer> 

  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
@media screen and (min-width: 1088px){
 .navbar-center {
    display:flex;
    justify-content: stretch;
    align-items: stretch;
    flex-grow: 1;
    flex-shrink: 0;
    flex-direction: row;
 }
}
</style>

<script>
// @ is an alias to /src
import axios from 'axios'
import UserDrop from './components/UserDrop.vue'

export default {
  name: 'App',
  data() {
    return {
      name: null
      }
  },
  components: {
    UserDrop
  },

  methods:{
    submit(){
      this.$router.push("/cardSearch?"+this.name);
    
    },
  }

}
</script>

