#The diagonal entries have a difference of 2*n when they are n steps 
#away from 1 on the diagonal

indices <- seq(from = 2, to = 1000, by = 2)

df <- matrix(rep(indices, times = 4), ncol = 4)
steps <- c(1, as.vector(t(df)))
diagonal_entries <- cumsum(steps)

print(sum(diagonal_entries))
