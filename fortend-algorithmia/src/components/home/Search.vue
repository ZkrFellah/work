<template>
        <div class="col-md-12 mb-32" >
                <div class="input-group"><input  v-model="value" placeholder="Search..." autocomplete="off" 
                    class="form-control input-lg">
                  <div class="input-group-btn">
                      <button type="submit" @click="searchAlgo()"  class="btn btn-default btn-lg">
                      <i aria-hidden="true" class="fa fa-search"></i>
                      </button>
                  </div>
                </div>
            <hr>
          </div>
</template>
<script>
export default {
  name: 'Search',
  data(){
    return {
      value: this.route.query.q
    }
  },
  methods:{
    searchAlgo(){
       this.$router.push({ path: '/search/?q='+this.value})
    }
  }


}
</script>


<style scoped>

</style>