collatz_length <- function(x){
  n <- 1
  while(x != 1){
    if((x %% 2) == 0){
      x <- x/2
    }
    else{
      x <- 3*x + 1
    }
    n <- n + 1
  }
  return(n)
}

vals <- sapply(1:1e6, collatz_length)

print(which.max(vals))
