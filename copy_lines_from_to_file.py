with open('source.txt','r') as source_file, open('write.log','w') as destination_file:
    x=source_file.read()
    y=x.split('\n')
    for i in range(0,10):
        destination_file.write(y[i])
        destination_file.write('\n')
    