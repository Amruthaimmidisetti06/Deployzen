data("airquality")

head(airquality)

str(airquality)

hist(airquality$Temp,
     main = "La Guardia Airport Daily Max Temperature",
     xlab = "Temperature (°F)",
     col = "orange",
     border = "black")
