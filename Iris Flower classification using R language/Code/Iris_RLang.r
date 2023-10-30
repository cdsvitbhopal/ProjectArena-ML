#BASIC DATA EXPLORATION
data(iris)
head(iris,4)
tail(iris)
dim(iris)
names(iris)
attributes(iris)
summary(iris)
sum(is.na(iris))
iris[1:5, ]         #Indexing the first 5 rows
iris[ , 1:4]       #Indexing the first 4 columns
Iris[1:10, Sepal Length]     #Exploring the first 10 rows of a particular column, in this case, Sepal length.
plot(iris)    #The plot () function is the generic function for plotting R objects.
pairs(iris[,1:4],col=iris[,5],oma=c(4,4,6,12)) # PLOT(IRIS),WITH COLORS AND LEGENDS
par(xpd=TRUE)            #CORRELATIONAL SCATTERPLOT
legend(0.85,0.6, as.vector(unique(iris$Species)),fill=c(1,2,3))
 
#HISTOGRAMS FOR EACH COLUMN OF DATASET
Sepal_Width <- iris$Sepal.Width
hist(Sepal_Width, main="Histogram of Sepal Width", xlab = "Sepal Width", xlim=c(2,5),col="darkorchid", freq= FALSE)
Sepal_Length <- iris$Sepal.Length
hist(Sepal_Width, main="Histogram of SepalLength", xlab = "Sepal Length", xlim=c(2,5),col="blue", freq= FALSE)
Petal_Width <- iris$Petal.Width
hist(Petal_Width, main="Histogram of Petal Width", xlab = "Petal Width", xlim=c(2,5),col= "green", freq= FALSE)
Petal_Length <- iris$Petal.Length
hist(Petall_Length, main="Histogram ofPetal Length", xlab = "petal Length", xlim=c(2,5),col="orange", freq= FALSE)
 
#BOXPLOTS IN DIFFERENT PALETTES 
irisVer <- subset(iris, Species == "versicolor")
irisSet <- subset(iris, Species == "setosa")
irisVir <- subset(iris, Species == "virginica")
par(mfrow=c(1,3),mar=c(6,3,2,1))  # more space to labels
boxplot(irisVer[,1:4], main="Versicolor, Rainbow Palette",ylim = c(0,8),las=2, col=rainbow(4))
boxplot(irisSet[,1:4], main="Setosa, Heat color Palette",ylim = c(0,8),las=2, col=heat.colors(4))
boxplot(irisVir[,1:4], main="Virginica, Topo colors Palette",ylim = c(0,8),las=2, col=topo.colors(4))
 
 
# PERCENTAGE, STANDARD DEVIATION, CORRELATION: +1 DIRECTLY RELATED, -1INVERSE.
cbind(freq=table(iris$Species), percentage = prop.table(table(iris$Species))*100)
sapply(iris[,1:4], sd)
cor(iris,[,1:4])
 
#SCATTER PLOTS
plot(iris$Sepal.Width, iris$Sepal.Length, col='steelblue', main='Scatterplot',xlab='Sepal Width',ylab='Sepal Length', pch=19)
plot(iris$Petal.Width, iris$Petal.Length,col='darkgreen',main='Scatterplot',xlab='Petal Width',ylab='Petal Length',pch=19)
 
# MACHINE LEARNING MODEL: DECISION TREE
install.packages("C50")
library(C50)
input <- iris[,1:4]
output <- iris[,5]
 
model1 <- C5.0(input, output, control = C5.0Control(noGlobalPruning = TRUE,minCases=1))
plot(model1, main="C5.0 Decision Tree - Unpruned, min=1")
 
# We can play with the parameters of the classifier to see better/simpler/more complete/more complex trees. Here's a simpler one:-
model2 <- C5.0(input, output, control = C5.0Control(noGlobalPruning = FALSE))
plot(model2, main="C5.0 Decision Tree - Pruned")
summary(model2)
 
C5imp(model2,metric='usage')   #"zoom into" the usage of features for creation of the model
newcases <- iris[c(1:3,51:53,101:103),]  #PREDICTING CLASS FROM NUMERICAL ATTRIBUTES
newcases
 
predicted <- predict(model2, newcases, type="class")
predicted
predicted <- predict(model2, iris, type="class")
predicted
 
#Let's see which rows have different classes (stated and predicted)
iris$predictedC501 <- predicted
iris[iris$Species != iris$predictedC501,]