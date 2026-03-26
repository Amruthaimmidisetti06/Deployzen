data("mtcars")  
summary(mtcars) 
mtcars_scaled <- scale(mtcars)
heatmap(mtcars_scaled,  
        main = "Heatmap of mtcars Dataset",  
        col = heat.colors(256),  
        scale = "none") 
