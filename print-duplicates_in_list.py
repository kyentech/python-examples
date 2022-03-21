l = ["Kumar","Sound","Devi","Sid","Kumar"]

def check_duplicates():
    global l
    print(set([x for x in l if l.count(x)>1]))
check_duplicates()