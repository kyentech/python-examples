s = [2113,42352,2312,665654,8798632]

def sort_acending_num():
    global s
    s.sort
    print(s)
def sort_decending_num():
    global s
    s.sort(reverse=True)
    print(s)
def sort_without_sort_function():
    global s
    new_list = []
    while s:
        min=s[0]
        for x in s:
            if x > min:
                min = x
                new_list.append(min)
                s.remove(min)
                print(new_list)
    
# sort_acending_num()
# sort_decending_num()
sort_without_sort_function()


    