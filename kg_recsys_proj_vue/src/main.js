import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000' //process.env.VUE_APP_DJANGO_ENDPOINT || 

createApp(App).use(store).use(router, axios).mount('#app')

