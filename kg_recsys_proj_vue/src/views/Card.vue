<template>
    <div class="page-product">
        <div class="columns">
            <div class="column is-3">
                <figure class="image mb-3">
                    <img :src="card.image_url">
                </figure>
            </div>
            <div class="column is-4 is-offset-1">
                 <h1 class="title">{{ card.name }}</h1>

                 <div class="image">
                    <div class="field has-addons mt-6">
                        <div class="control">
                            <input type="number" class="input" min="1" v-model="quantity">
                        </div>

                        <div class="control" @click="buyCard()">
                            <a class="button is-dark"> Buy </a>
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Card',
    data() {
        return {
            card: {},
            quantity: 1
        }
    },
    mounted() {
        this.getCard()
    },
    methods: {
        getCard() {
            const card_slug = this.$route.params.card_slug
            
            axios
                .get(`/card/${card_slug}`)
                .then(response => {
                    this.card = response.data
                    console.log(this.card.image_url)
                })
                .catch(error=>{
                    console.log(error)
                })

        },

        buyCard() {
            const card_slug = this.$route.params.card_slug
            axios
                .post(
                    '/buy_card/',
                    {
                        'uid':'04375983ff3649dda695435ea2f4e095',
                        'card_code': card_slug
                    } 
                )
                .then(response =>{
                    console.log(response.data)
                })
                .catch(error=>{
                    console.log(error)
                })

        }
    }
    
}
</script>
