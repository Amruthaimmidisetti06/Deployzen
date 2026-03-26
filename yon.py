data("iris")
summary(iris)
boxplot(Sepal.Length ~ Species,
        data = iris,
        main = "Sepal Length by Species",
        xlab = "Species",
        ylab = "Sepal Length (cm)",
        col = c("lightblue", "salmon", "lightgreen"),
        border = "darkblue")

boxplot(Petal.Width ~ Species,
        data = iris,
        main = "Petal Width by Species",
        xlab = "Species",
        ylab = "Petal Width (cm)",
        col = c("skyblue", "orange", "lightpink"),
        border = "black")

palette <- rainbow(3)

boxplot(Sepal.Width ~ Species,
        data = iris,
        main = "Sepal Width by Species",
        col = palette,
        xlab = "Species",
        ylab = "Sepal Width (cm)")





data("airquality")
summary(airquality)
par(mfrow = c(2, 2))
boxplot(airquality$Ozone,
        main = "Ozone Concentration",
        ylab = "Ozone (ppb)",
        col = "lightblue")

boxplot(airquality$Solar.R,
        main = "Solar Radiation",
        ylab = "Solar.R (lang)",
        col = "lightgreen")

boxplot(airquality$Wind,
        main = "Wind Speed",
        ylab = "Wind (mph)",
        col = "lightyellow")

boxplot(airquality$Temp,
        main = "Temperature",
        ylab = "Temperature (°F)",
        col = "lightpink")

par(mfrow = c(1, 1))
