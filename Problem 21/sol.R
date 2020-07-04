library(numbers)

sum_divs <- function(x){
  return(sum(divisors(x)) - x)
}

nums <- 2:9999
sdiv <- sapply(nums, sum_divs)
sdiv2 <- sapply(sdiv, sum_divs)

df <- data.frame(nums = nums, 
                 sdiv = sdiv,
                 sdiv2 = sdiv2)
sel <- (df$nums != df$sdiv) & (df$nums == df$sdiv2)

sum(df$nums[sel])
