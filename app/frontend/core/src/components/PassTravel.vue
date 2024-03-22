<template>
    <div class="content">
        
        <div class="travel-content">
            <div class="space-content">
                    <img class="airplane" src="../assets/airplane.png"> 
            </div>
            <div class="pass-info">  
               
                <h3>{{fast_transport}}</h3>
                <p>{{bed}}</p>
                <p>Tempo estimado: {{time_fast}}</p>
            </div>

            <div class="pass-price">
                <h3>
                    {{price_fast}}
                </h3>
            </div>
            
        </div>    

        <div class="travel-content">
            <div class="space-content">
                    <span><img class="airplane" src="../assets/snail.png"> </span>
            </div>
            <div class="pass-info">  
                <h3>{{transport_slow}}</h3>
                <p>{{seat}}</p>
                <p>Tempo estimado: {{time_slow}}</p>
            </div>

            <div class="pass-price">
                <h3>{{price_slow}}$</h3>
            </div>
            
        </div>    
    </div>
</template>

<script>
export default {
    name:'PassTravel',
    props:[
        'fast_transport',
        'bed',
        'time_fast',
        'price_fast',
        'transport_slow',
        'seat',
        'time_slow',
        'price_slow'
    ]

}
</script>

<style scoped>
    .content{
        background-color: rgb(62, 62, 62);
        color:white;
        padding: 50px;
        width:30vw;
        border-radius: 50px;
        position: relative;
        bottom:165px;
        margin-right: 100px;
        float: right;
        display: flex;
        flex-direction: column;
    }

    .travel-content{
        background-color:rgb(92, 132, 158);  
        display: flex;
        flex-direction: row;
        margin-top: 30px;
    }

    .space-content{
        background-color: white; 
        padding-right: 40px;
    }

    .airplane{
        margin-top: 50px;
        margin-left:30px
        
    }
    .pass-info{
        margin-left:40px
    }

    .pass-price{
        margin-right: 30px;
    }
</style>