<template>
  <div class="navigation_bar">
    <video-background
        :src="require(`@/assets/background/nav.mp4`)"
        :poster="require(`@/assets/background/poster.jpg`)"
        style="max-height: 50px; height: 100vh;"
        overlay="linear-gradient(45deg,#2a4ae430,#fb949e6b)">

      <nav class="navbar navbar-expand-md navbar-dark">
        <b-link :to="{path: '/'}" class="navbar-brand ">
          <div><font color="white">T</font><font color="#00A6D6">U</font><font color="white"> Delft</font></div>
        </b-link>

        <div class="collapse navbar-collapse" id="navbarCollapse">
          <div class="navbar-nav">
            <b-link :to="{path: '/'}" class="nav-item nav-link">Home</b-link>
            <b-link :to="{path: '/about'}" class="nav-item nav-link">About</b-link>
          </div>

        </div>
      </nav>
    </video-background>


  </div>
</template>

<script>
export default {
  data() {
    return {
      // see if the logo is available, if it is load it.
      // the logo variable can be changed dynamically and can be used
      // to the user the status of the simulation in the future
      logo: require(`@/assets/logo/logo.png`)
    }
  }
}
</script>
