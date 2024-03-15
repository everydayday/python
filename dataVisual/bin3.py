import datetime
from datetime import datetime as dt

today = dt.strptime('2024-03-15', '%Y-%m-%d')

print(today, type(today), type('2024-03-15'))

print(today + datetime.timedelta(days=3)) ## 날짜 더하기 편함




try:    
    with open('c.csv') as f:
        for line in f:
            print(line)
except Exception as e:
    pass
    print(e)

    