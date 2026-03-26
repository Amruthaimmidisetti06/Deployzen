data("HairEyeColor") 
HairEyeColor 
hair_eye_df <- as.data.frame(HairEyeColor) 
mosaicplot(HairEyeColor, 
           main = "Mosaic Plot of Hair Color vs Eye Color", 
           xlab = "Hair Color", 
           ylab = "Eye Color", 
           color = TRUE)
