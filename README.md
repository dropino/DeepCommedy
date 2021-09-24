# DeepCommedy

In this project we developed two models able to generate texts similar to Dante’s Divine Comedy, with particular attention given to making sure that verses are correctly syllabified.  
  
Two different architectures have been developed: the first is composed of a single Generator model trained on pre-syllabified data to directly generate syllabified verses. The second one is composed of a Generator trained with non syllabified data which generates verses and a Syllabifier trained with syllabified data to demonstrate that the generated verses are correct.  
