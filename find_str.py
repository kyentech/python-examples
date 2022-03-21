import re
s1 = "I am happy"
s2 = "I am old"
# output should be ["happy","old"]
s1_happy = re.findall("happy", s1)
s2_old = re.findall("old", s2)
s3 = s1_happy + s2_old
print (s3)
