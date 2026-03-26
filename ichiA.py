data("VADeaths")

print("VADeaths Dataset:")
print(VADeaths)

va_df <- as.data.frame(VADeaths)

str(va_df)

dev.off()

par(mfrow = c(2, 2), mar = c(4, 4, 2, 1))

hist(va_df$`Rural Male`,
     main = "Rural Male Death Rate",
     xlab = "Death Rate",
     col = "skyblue",
     border = "black")

hist(va_df$`Rural Female`,
     main = "Rural Female Death Rate",
     xlab = "Death Rate",
     col = "lightgreen",
     border = "black")

hist(va_df$`Urban Male`,
     main = "Urban Male Death Rate",
     xlab = "Death Rate",
     col = "salmon",
     border = "black")

hist(va_df$`Urban Female`,
     main = "Urban Female Death Rate",
     xlab = "Death Rate",
     col = "orchid",
     border = "black")

par(mfrow = c(1, 1))


data("airquality")

head(airquality)

str(airquality)

hist(airquality$Temp,
     main = "La Guardia Airport Daily Max Temperature",
     xlab = "Temperature (°F)",
     col = "orange",
     border = "black")
