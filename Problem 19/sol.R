library(lubridate)

start <- ymd("1901-01-01")
end <- ymd("2000-12-31")

l <- as.numeric(end - start)

days <- start + 1:l

sundays_on_first <- days[wday(days) == 1 & day(days) == 1]

print(length(sundays_on_first))