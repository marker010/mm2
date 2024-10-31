mind <- function(d){
  n <- nrow(d)
  dd <- cbind(d,1:n)
  wmins <- apply(dd[-n,],1,imin)
  i <- which.min(wmins[2,])
  j <- wmins[1,i]
  return(c(d[i,j],i,j))
}

imin <- function(x){
  lx <- length(x)
  i <- x[lx]
  j <- which.min(x[(i+1):(lx-1)])
  k <- i+j
  return(c(k,x[k]))
}

x <- c(0,12,13,8,20,12,0,15,28,88,13,15,0,6,9,8,28,6,0,33,20,88,9,33,0)

q <- matrix(x,nrow=5,ncol=5)
q

mind(q)
