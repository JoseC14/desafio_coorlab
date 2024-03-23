<template>
    <div> 
        <div class="modal-background"></div>
        <div class="modal">
            <h1 class="erro" >Erro!</h1>
            <h3>Campos obrigatórios não preenchidos</h3>

            <button class="ok" @click="closeModal">Ok</button>
        </div>
    </div>
</template>
<script>
export default {
    name:'ModalError',
    methods:{
        closeModal()
        {
            this.$emit('destroyModal',false)
        }
    }


}
</script>

<style scoped>
.modal{
    text-align: center;
    position:relative;
    display: flex;
    flex-direction: column;
    bottom:50vh;
    margin: 0 auto;
    right: 10vw;
    padding: 50px;
    width: 20vw;
    background-color: white;
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;

}

.modal-background{
    position:fixed;
    top:0;
    width: 100vw;
    height: 100vh;
    background-color:rgba(0,0,0,0.2);
}

.ok{
    padding: 5px;
    cursor:pointer;
    background-color: rgb(92, 132, 158);
    color:white;
    border:none
}
</style>