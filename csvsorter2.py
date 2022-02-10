import csv

lu1, lu2, lu2, lu3, lu4, lu5, lu6, lu7, lu8, lu9, lu10, lu11, lut = 0,0,0,0,0,0,0,0,0,0,0,0,0
plu1, plu2, plu3, plu4, plu5, plu6, plu7, plu8, plu9, plu10, plu11 = 0,0,0,0,0,0,0,0,0,0,0
zipcode = input('Input your zipcode:')

with open('pluto_21v4.csv', 'r') as data:
    csvreader = csv.reader(data)
    for row in csvreader:
        if row[10] == zipcode:
            if row[31] == '01':
                lu1 = lu1 + 1
                lut = lut + 1
            elif row[31] == '02':
                lu2 = lu2 + 1
                lut = lut + 1
            elif row[31] == '03':
                lu3 = lu3 + 1
                lut = lut + 1
            elif row[31] == '04':
                lu4 = lu4 + 1
                lut = lut + 1
            elif row[31] == '05':
                lu5 = lu5 + 1
                lut = lut + 1
            elif row[31] == '06':
                lu6 = lu6 + 1
                lut = lut + 1
            elif row[31] == '07':
                lu7 = lu7 + 1
                lut = lut + 1
            elif row[31] == '08':
                lu8 = lu8 + 1
                lut = lut + 1
            elif row[31] == '09':
                lu9 = lu9 + 1
                lut = lut + 1
            elif row[31] == '10':
                lu10 = lu10 + 1
                lut = lut + 1
            elif row[31] == '11':
                lu11 = lu11 + 1
                lut = lut + 1

plu1 = (lu1/lut) * 100
plu2 = (lu2/lut) * 100
plu3 = (lu3/lut) * 100
plu4 = (lu4/lut) * 100
plu5 = (lu5/lut) * 100
plu6 = (lu6/lut) * 100
plu7 = (lu7/lut) * 100
plu8 = (lu8/lut) * 100
plu9 = (lu9/lut) * 100
plu10 = (lu10/lut) * 100
plu11 = (lu11/lut) * 100

print(f'lu1 is {lu1,plu1}')
print(f'lu2 is {lu2,plu2}')
print(f'lu3 is {lu3,plu3}')
print(f'lu4 is {lu4,plu4}')
print(f'lu5 is {lu5,plu5}')
print(f'lu6 is {lu6,plu6}')
print(f'lu7 is {lu7,plu7}')
print(f'lu8 is {lu8,plu8}')
print(f'lu9 is {lu9,plu9}')
print(f'lu10 is {lu10,plu10}')
print(f'lu11 is {lu11,plu11}')
print(f'total is {lut}')

#Note: this can and should be simpler, but it's not.
