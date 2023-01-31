<template>
  <div id="app">
    <!-- website background image & animation -->
    <video-background v-if="this.$route.name !== 'Advanced' && this.$route.name !== 'Comparison'"
                      :src="require(`@/assets/background/background.mp4`)"
                      :poster="require(`@/assets/background/poster.jpg`)"
                      style="max-height: 400px; height: 100vh;"
                      overlay="linear-gradient(45deg,#2a4ae430,#fb949e6b)">

      <!-- <div classs = "logo"></div>-->
      <h1 style="color: white;"><font color="#000000">T</font><font color="#00A6D6">U</font><font color="#000000">
        Delft</font> <br> Covid-19 Block Simulation
      </h1>
      <!--<img class="logo-image" :src="require(`@/assets/logo/logo.png`)" height="300" width="150"/>-->
    </video-background>
    <!-- route navigation buttons -->
    <div v-if="this.$route.name !== 'Advanced' && this.$route.name !== 'Comparison'"  id="nav">
      <router-link to="/">Home</router-link>
      |
      <router-link to="/about">About</router-link>
    </div>
    <!-- view container -->
    <b-container>
      <router-view/>
    </b-container>
  </div>

</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>


