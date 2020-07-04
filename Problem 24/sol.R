library(combinat)
#Slow af
perms <- lapply(permn(0:9), function(x) paste(x, collapse = ""))

print(sort(unlist(perms))[1e6])
