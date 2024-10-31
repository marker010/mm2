aba <- read.csv("C:/Users/13708/OneDrive/桌面/R语言/data/Abalone.data", header = TRUE, as.is = TRUE)
aba
grps <- list()
for(gen in c("M","F")){
  grps[[gen]] <- which(aba[,1]==gen)
}
abam <- aba[grps$M,]
abaf <- aba[grps$F,]
plot(abam$Length, abam$Diameter)  
par(new=TRUE)                    
plot(abaf$Length, abaf$Diameter, pch="x", axes=FALSE, xlab="", ylab="")  


abafull <- read.csv("C:/Users/13708/OneDrive/桌面/R语言/data/Abalone_0.data", header = TRUE, as.is = TRUE)

pchvec <- ifelse(abafull$Gender == "M","o","x")

plot(abafull$Length,abafull$Diameter,pch=pchvec)
