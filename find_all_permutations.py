from itertools import permutations

int_str="abcd"
print ("Actual string:",int_str)

permute = [''.join(p) for p in permutations(int_str)]

print("Result", str(permute))