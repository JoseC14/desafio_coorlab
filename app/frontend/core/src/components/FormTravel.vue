<template>
    <div>
        <div class="search">   
            <form @submit.prevent="searchPass">
                <div class="container"> 
                    <div class="input-content">
                        <h3>Destino</h3> 
                        <select v-model="destiny" id="destiny">
                            <option v-for="city in cities" :key="city">{{ city }}</option>
                        </select>
                    </div>

                    <div class="input-content">
                        <h3>Data</h3>
                        <input type="date" name="date_wished" v-model="date_wished" id="date_wished">
                        <br>
                        <br>
                    </div>
                   
                    <div class="input-content">
                        <input id="buscar" type="submit" value="Buscar">
                    </div>
               
                </div>
            </form>
        </div>
        <div v-if="formSubmitted">
            <PassTravel :bed="apiData[0].bed"
                        :fast_transport="apiData[0].name"
                        :price_fast="apiData[0].price_confort"
                        :time_fast="apiData[0].duration"
                        :transport_slow="apiData[1].name"
                        :price_slow="apiData[1].price_econ"
                        :seat="apiData[1].seat"
                        :time_slow="apiData[1].duration"/>
        </div>

        <div v-if="formError">
            <ModalError @destroyModal="closeModal"/>
        </div>
    </div>
</template>

<script>

import PassTravel from './PassTravel.vue'
import ModalError from './ModalError.vue'
import axios from 'axios'



export default {
    name:'FormTravel',
    components:{
        PassTravel,
        ModalError
    },
    data(){
    return {
        destiny: '',
        date_wished: '',
      formSubmitted:false,
      formError:false,
      apiData: null,
      cities:[]
    };
  },
  mounted()
    {
        axios.get('http://127.0.0.1:8000/api/transports').then(response=>{
            this.cities=response.data.map(transport => transport.city);
        })
    },
  methods: {
    searchPass() {
        if(this.destiny == '' || this.date_wished == '')
        {
            this.formError = true
        }else{
            axios.get(`http://127.0.0.1:8000/api/transports/${this.destiny}`).then(response=>{
            this.apiData = response.data.transports
            this.formSubmitted=true
            })
        }
        
    },
    closeModal(data)
    {
        this.formError = data
    }
  }
}




</script>

<style scoped>
    input, select{
        border: none;
        border-radius:2px;
        padding:8px;
        border:1px solid #ccc;
    }

    h3{
        display:flex;
        justify-content:start;
    }
    .container{
        display: flex;
        flex-direction: column;
        width: 20vw;
        text-align: center;
        position: relative;
        left:70px;
        top: 100px;
    }
    #destiny{
        border: none;
        background-color:white;
    }

    #date_wished{
        position: relative;
        margin-bottom:20px;
    }

    #buscar{
        background-color: rgb(62, 62, 62);
        border: none;
        padding: 15px;
        cursor: pointer;
        color:white;
    }

    #buscar:hover{
       background-color:white;
       color: black; 
    }

    .input-content{
        margin-top: 20px;
        display: flex;
        flex-direction: column;
    }
</style>
