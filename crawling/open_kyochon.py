import csv

f = open('goup.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for index,line in enumerate(rdr):
    if index:
        print(line[0]+',',end=' ')
        print('이름 :',end=' ')
        print(line[1]+',',end =' ')
        print('시 :',end=' ')
        print(line[2]+',',end = ' ')
        print('구 : ',end =' ')
        print(line[3]+',',end =' ')
        print('주소 :',end=' ')
        print(line[4])
f.close()
