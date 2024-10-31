library(pixmap)
mtrush1 <- read.pnm("C:/Users/13708/AppData/Local/R/win-library/4.3/pixmap/pictures/mtrush1.pgm")
mtrush1
plot(mtrush1)
mtrush2 <- mtrush1
mtrush2@grey[120:220,230:280] <- 1
plot(mtrush2)

blurpart <- function(img, rows, cols, q) {
  lrows <- length(rows)
  lcols <- length(cols)
  newimg <- img
  randomnoise <- matrix(runif(lrows * lcols), nrow = lrows, ncol = lcols)
  newimg@grey[rows, cols] <- (1 - q) * img@grey[rows, cols] + q * randomnoise
  return(newimg)
}
mtrush3 <- blurpart(mtrush1, 120:220, 230:280, 0.5)
plot(mtrush3)

