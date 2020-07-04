path <- "C:/Users/d91913/Documents/R/Privat/Project Euler/Problem11/grid.txt"

prodn <- function(x, k = 4){
  n <- length(x)
  res <- c()
  if(n < k){
    return(0)
  }
  else{
    for(i in 1:(n-k+1) ){
      res <- c(res, prod(x[i:(i+k-1)]))
    }
    return(res)
  }
}

rotate_matrix <- function(x){
  return(apply(x, 2, rev))
}

grid <- as.matrix(read.delim(path, sep = " ", header = F))
colnames(grid) <- NULL
flipped_grid <- t(apply(grid, 1, rev))

diags_lower_leftright <- lapply(1:17, function(x) diag(grid[x:20,]))
diags_upper_leftright <- lapply(2:17, function(x) diag(t(grid)[x:20,]))

diags_lower_rightleft <- lapply(1:17, function(x) diag(flipped_grid[x:20,]))
diags_upper_rightleft <- lapply(2:17, function(x) diag(t(flipped_grid)[x:20,]))

rows <- lapply(1:20, function(x) grid[x,])
cols <- lapply(1:20, function(x) grid[,x])

directions <- c(diags_lower_leftright, diags_upper_leftright,
                diags_lower_rightleft, diags_upper_rightleft,
                rows, cols)

prods <- unlist(lapply(directions, prodn))
max(prods)
