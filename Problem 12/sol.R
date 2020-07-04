library(numbers)

v <- 1:2e4

df <- data.frame(values = v, sums = v*(v+1)/2)

df$ndiv <- sapply(df$sums, function(x) length(divisors(x)))

df[df$ndiv > 500,][1,2]
