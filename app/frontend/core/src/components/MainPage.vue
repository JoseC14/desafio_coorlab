<template>
    <div>
        <SideBar/>
        <FormTravel/>
    </div>
</template>

<script>
import SideBar from './SideBar.vue';
import FormTravel from './FormTravel.vue';


export default {
    name:'MainPage',
    components:{
        SideBar,
        FormTravel
    }

}
</script>

<style scoped>
    
</style>