def search(lt,x):
    for i in range(len(lt)):
        if lt[i]==x:
            print("Found at", i)

l=[1,2,3,4,5,5,2,34,55]
search(l,55)