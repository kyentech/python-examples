import re
import re
def sum_num_in_str(str):
    return sum(map(int, re.findall('\d+',str)))
    
print(sum_num_in_str("11gjhl1"))
            