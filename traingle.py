rows = int(input("Enter number of rows:"))
for i in range(rows):
    number = 0
    for j in range(i+1):
        print(number ,end=" ")
        number+1
    print("\r")
 
    