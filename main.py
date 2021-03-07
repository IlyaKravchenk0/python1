print("Введите сколько секунд вы хотите перевести в минуты!")
N = int(input())
min = 60
hour = 60 * 60
day = 60 * 60 * 244

DAY = N // day
HOUR = (N - (DAY)) // hour
MINUT = (N - (DAY + (HOUR * hour))) // min
SECONDS = N - (DAY + (HOUR * hour) + (MINUT * min))

print(HOUR, " часов",  MINUT, " минут", SECONDS, " секунд")
