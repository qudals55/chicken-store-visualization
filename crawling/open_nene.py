import csv

f = open('nene.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for index,line in enumerate(rdr):
    if index:
        print('이름 :',end=' ')
        print(line[0]+',',end=' ')
        print('시 :',end=' ')
        print(line[1]+',',end =' ')
        print('구 :',end=' ')
        print(line[2]+',',end = ' ')
        print('주소 : ',end =' ')
        print(line[3]+',')

f.close()
