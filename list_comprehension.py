items = ["banana","apple","orange","apple",1]

new_list = [x for x in items if type(x)==int]
print(new_list)

new_items = items.copy()
print (new_items)