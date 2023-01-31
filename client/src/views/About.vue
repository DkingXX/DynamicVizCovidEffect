<template>
  <div class="about-page-container">
    <AboutInfoAndCredits :project-text="projectText" :authors="authors"/>
  </div>
</template>

<script>
import AboutInfoAndCredits from "@/components/generalUseComponents/AboutInfoAndCredits";
export default {
  components: {AboutInfoAndCredits},
  data() {
    return {
      projectText: "At the end of 2019, a new viral pneumonia started to spread" +
          "amongst people generating a pandemic that affects\n" +
          "every part of the world. Given the current situation of the Corona Virus, there is no doubt our society is" +
          "facing a threat which has never been faced until this current moment. While there have been pandemics in the" +
          "past," +
          "we are now more globally connected than before. Using fast trains and planes you can get from one part of" +
          "the world to another in a matter of hours. Moreover, our population density has been the highest in the past" +
          "decades, now having reached a point where many people live in urban and suburban areas. Due to these\n" +
          "technological and engineering developments, plus the population rise, viruses can now spread much more easily" +
          "and way faster. Big metropolitan areas are also at the highest risk of having a high viral infection rate of" +
          "the population." + "\n" +
          "People in our society have started to get used to having more freedom in speech, travel and ways of living," +
          "so when measures regarding social distancing and lockdowns have appeared, some people were outraged and" +
          "did not follow the safety guidelines given by the WHO. Because of multiple political decisions and" +
          "speeches, disinformation campaigns on social media and not only, some part of the population started to doubt" +
          "the" +
          "efficiency of the countermeasures against the Covid-19 infection." + "" +
          "This project aims to provide a user-friendly interface that will provide both visually and numerically" +
          "          interpretation of a time-evolving human contact network in which certain (contact) mitigation scenarios are" +
          "applied." +
          "The web application we are going to develop should be able to show both sceptical and non-sceptical people" +
          "the effectiveness of contact mitigation measures, using temporal networks, thus informing people how certain" +
          "measures help in flattening the line of infection rate.",

      authors: ["Andrei Ionescu",
        "Ina Lupu",
        "Xiangyu Du",
        "Zenan Guan",
        "Ziang Qiu",]


    }
  }
}
</script>
