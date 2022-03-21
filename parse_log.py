import re

def parse(filename):
    file = open(filename).read().splitlines()
    for index, line in enumerate(file):
        if "SEVERE" in line:
            file[index+1]
            print(file[index:index+2])
      
if __name__ == '__main__':
   parse('log_snippet.log')


