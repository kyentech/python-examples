with open('log_snippet.log') as f:
    x=f.read()
    y=x.split()
    dic={}
    for i in y:
        if i not in dic:
              dic[i]=1
              print(dic[i])
        else:
              print(dic[i])
              dic[i]+=1
    for key in dic:
          if dic[key]>1:
                print(key,dic[key])
     
            