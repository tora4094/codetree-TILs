class WeatherData:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather
    def info(self):
        print(self.date,self.day,self.weather)

n = int(input())
arr = []
for _ in range(n):
    date, day, weather = tuple(input().split())
    arr.append(WeatherData(date,day,weather))

arr.sort(key=lambda wd : wd.date)

for wd in arr:
    if wd.weather == "Rain":
        wd.info()
        break