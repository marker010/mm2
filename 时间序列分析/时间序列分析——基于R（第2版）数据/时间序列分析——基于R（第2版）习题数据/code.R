setwd("C:\\Users\\13708\\OneDrive\\桌面\\时间序列分析\\时间序列分析——基于R（第2版）数据\\时间序列分析——基于R（第2版）习题数据")

data <- read.table('习题2.8.1数据.txt',header = FALSE)
data_1 <- data[[2]]

data_1 <- ts(data_1)
plot(data_1)

acf(data_1,lag = 24)

len <- length(data_1)

b<-NULL
for(i in 2:len){
  b <- c(b,data_1[i]-data_1[i-1])
}

b <- ts(b)

plot(b)

acf(b,lag.max = 24)
