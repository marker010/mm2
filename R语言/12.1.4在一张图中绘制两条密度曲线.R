library(readxl)

testscore <- read_excel("C:\\Users\\13708\\OneDrive\\桌面\\R语言\\data\\testscore.xlsx")

d1 = density(testscore$Exam1,from=0,to=100)
d2 = density(testscore$Exam2,from=0,to=100)
plot(d1,main="",xlab="")
lines(d2)

