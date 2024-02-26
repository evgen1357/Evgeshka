import csv
import datetime
with open('songs.csv',encoding='utf8') as file:
    reader = csv.reader(file,delimiter=';')
    next(file)
    data = [x for x in reader]

    print(data)
    for el in data:
        if el[0]=='0':
            date = list(el[3].split('.'))
            arr = [int(y) for y in date]
            Dn = datetime.datetime(2023,5,12,0,0,0)
            Di = datetime.datetime(arr[2],arr[1],arr[0],0,0,0)
            time_diff = Dn-Di
            days = time_diff.days
            el[0] = abs(days/(len(el[1]) + len(el[2])))*10000
            print(el[0])

with open('songs_new.csv','w',encoding='utf8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for el in data:
        writer.writerow(el)