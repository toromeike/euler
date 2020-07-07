# Set c = 1000 - a - b
# Then the solution has to have the form 1000(a+b) = ab+500*1000

df <- expand.grid(a = 1:999, b = 1:998)
df$solves <- (1000*(df$a + df$b)) == (df$a * df$b + 500*1000)
sol <- df[df$solves,][1,]
print(sol$a * sol$b * (1000 - sol$a - sol$b))
