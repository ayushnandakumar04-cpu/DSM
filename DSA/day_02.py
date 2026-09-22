#Best Time to Buy and Sell Stock
price=[7,8,3,4,5,2]
min_price=price[1]
max_price=0

for p in price:
   if p<min_price:
      min_price=p

   profit = p - min_price

   if p>max_price:
      max_pric=p
print(p)

#Contains Duplicate

num=[3,4,5]
if len(num)!=len(set(num)):
   print(True)
else:
   print(False)
