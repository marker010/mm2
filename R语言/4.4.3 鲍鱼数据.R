g <- c("M","F","F","I","M","M","F")

lapply(c("M","F","I"),function(gender) which(g==gender))
