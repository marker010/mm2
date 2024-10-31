exams <- read.table("C:/Users/13708/OneDrive/桌面/R语言/data/ExamsQuiz.txt", header = FALSE)
exams
lma <- lm(exams[,2] ~ exams[,1]+exams[,3])
lma$coef
