import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'Beijing_2014.csv'
with open(filename,'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    highs,lows,dates = [],[],[]
    for row in reader:
        try:
            current_data = datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_data,'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_data)
    #print(highs)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='green',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
fig.autofmt_xdate()

plt.title('Daily high and low temperatures -2014')
plt.xlabel('Date',fontsize=16)
plt.ylabel('Temperature(F)',fontsize=16)
plt.show()
