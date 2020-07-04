ones <- c("one", "two", "three", "four", "five", 
          "six", "seven", "eight", "nine")
teens <- c("eleven", "twelve", "thirteen", "fourteen", "fivteen",
           "sixteen", "seventeen", "eighteen", "nineteen")
tens <- c("","twenty","thirty", "forty", "fifty", 
          "sixty", "seventy", "eighty", "ninety")

hundred <- "hundred"


spell_xy_digits <- function(digits){
  n <- length(digits)
  
  if(n == 1 | digits[1] == 0){
    return(ones[digits])
  }
  else if(n == 2 & digits[1] == 1){
    if(digits[2] == 0){
      return("ten")
    }
    else{
      return(teens[digits[2]])
    }
  }
  else if(n == 2 & digits[1] > 1){
    return(paste(tens[digits[1]], ones[digits[2]], sep = ""))
  }
  else if(n == 2 & sum(digits) == 0){
    return("")
  }
}

n_spelled <- function(x){
  digits <- as.numeric(strsplit(as.character(x), "")[[1]])
  n <- length(digits)
  if(n < 3){
    return(spell_xy_digits(digits))
  }
  else if(x %in% as.integer(100*(1:9))){
    return(paste(ones[digits[1]], 
                 hundred,
                 sep = ""))
  }
  else{
    return(paste(ones[digits[1]], 
                 hundred, 
                 "and", 
                 spell_xy_digits(digits[2:3]), sep = ""))
  }
}

nums <- 1:999 
spelled <- c(unlist(sapply(nums, n_spelled)), "onethousand")
sum(nchar(spelled))
