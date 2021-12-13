#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!
szám = int(input('Adj meg egy egész számo! '))
szám1 = int(input('Adj meg egy másik egész számot! '))
if szám > szám1:
  print (szám, 'a nagyobb!')
if szám < szám1:
  print (szám1, 'a nagyobb!')
