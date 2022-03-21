items = [("shirt",10),
         ("pant",10),
         ("glasses",20),
         ("ticket",5),
         ("ride",3)]
prices = []
for i in items:
    prices.append(i[1])

price_greater_than_10=list(filter(lambda item: item[1] > 10, items))
print(price_greater_than_10)

# map example
prices=[]
for item in items:
    prices.append(item[1])
print(prices)

x = list(map(lambda item:item[1],items))
print(x)
    

