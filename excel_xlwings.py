import xlwings as xw
import random

wb = xw.Book("unacknowledged words.xlsx")
sht = wb.sheets["Sheet1"]

rng = sht.range('a1').expand('table')
nrows = rng.rows.count
n = random.randint(0,nrows)
print(n+1)

cell = sht[n,0].value
print(cell)

t = input('认识请按1: ') 
print(t)

i = int(sht[n,1].value)
print(i)

if t == 1:
  pass
else:
 	i = i+1
 	sht[n,1].value = i
