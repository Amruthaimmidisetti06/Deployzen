data("AirPassengers")

print("Summary of AirPassengers dataset:")
summary(AirPassengers)

print(paste("Class of dataset:", class(AirPassengers)))

plot(AirPassengers,
     main = "Monthly International Air Passengers (1949–1960)",
     xlab = "Year",
     ylab = "Number of Passengers (in Thousands)",
     col = "blue",
     type = "l",
     lwd = 2)
