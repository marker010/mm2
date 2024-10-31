values <- sample(c(0, 1), size = 500, replace = TRUE, prob = c(0.6, 0.4))
predA <- function(x,k){
  n <- length(x)
  half <-k/2
  prd <- vector(length = n-k)
  for(i in 1:(n-k)){
    if(sum(x[i:(i+(k-1))])>=half){
      prd[i]<-1
    }
    else{
      prd[i]<-0
    }
  }
  return(mean(abs(prd-x[(k+1):n])))
}
point <- vector(length = 18)
for(i in 3:20){
  point[i-2] <- 1-predA(values,i)
}
point
plot(c(1:18),point,xlim = c(1, 18))
axis(1, at = seq(1, 18, by = 1))

