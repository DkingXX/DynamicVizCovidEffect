<template>

  <div class="container px-lg-5">
    <div class="row mx-lg-n5">
      <div class="col py-3 px-lg-5 border bg-light">
        {{ projectText }}
      </div>
      <div class="col py-3 px-lg-5 border bg-active">
        <h1>Credits:</h1><br>

        <h2>Authors:</h2>
        <div v-for="(author,index) in authors" :key="index"> {{ author }}</div>

        <br>
        <h3>More info:</h3>
        <img :src="image" width="350" height="200"/>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  props: {
    projectText: String,
    authors: Array
  },
  data(){
    return {
      image : require(`@/assets/logo/logo_sim.png`)
    }
  }

}
</script>
