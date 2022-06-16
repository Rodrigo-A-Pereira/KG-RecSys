<template>
     <div :class="dropdownClasses">
              <div class="dropdown-trigger">
                <button @click="toggleDropdown" class="button is-dark" aria-haspopup="true" aria-controls="dropdown-menu">
                    <i class="fas fa-user"></i>
                </button>
              </div>

              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content" >
                  <a @click="setUser($event, user.uid)" class="dropdown-item" v-for="user in users" v-bind:key="user.uid">
                    {{user.name}}
                  </a>
                </div>
              </div>
            </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'user-drop',
    data () {
    return {
        isActive: false,
        users:[],
        selectedUser: ""
        }
    },
    computed: {
        dropdownClasses: function() {
            if (this.isActive) {
                return "dropdown is-active is-right";
            } else {
                return "dropdown is-right";
            }
            console.log("dropdownClasses = " + this.dropdownClasses);
        }

    },
    mounted() {
        this.getUserList()
    },
    methods: {
        toggleDropdown: function() {
            this.isActive = !this.isActive;
        },
        getUserList(){
            axios
                .get('/user/')
                .then(response => {
                    console.log(response.data)
                    this.users = response.data
                    this.selectedUser = this.users[0];
                    console.log("user obtained")
                })
                .catch(error => {
                    console.log(error)
                })
            
        },

        setUser(event,uid) {
            var elements = document.getElementsByClassName('dropdown-item');
            for (var i = 0; i < elements.length; i++) {
                console.log(elements[i].classList.remove('is-active'));
            }
            console.log(event.target.text)
            console.log(uid)
            event.target.classList.add('is-active')
            this.selectedUser = uid;
            
        }

        
    }
}
</script>

<style scoped>
.dropdown-content {
  max-height: 13em;
  overflow: auto;
}
</style>