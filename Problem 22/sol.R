letters <- c("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
             "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z")

score <- function(x){
  splt <- unlist(strsplit(x, split = ""))
  return( sum(sapply(splt, function(x) which(x == letters))) )
  }


name <- readChar("p022_names.txt", file.info("p022_names.txt")$size)
name <- unlist(strsplit(name, split = ",", fixed = FALSE))
name <- substring(name, 2, nchar(name) - 1)

sorted_names <- sort(name)

df <- data.frame(id = 1:length(name), 
                 names = sorted_names, 
                 score = sapply(sorted_names, score))

print(sum(df$id * df$score))