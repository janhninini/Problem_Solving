from itertools import permutations
for i in range(int(input())):
    s = input()
    p = input()
    for i in permutations(s):
        print ["".join(i)]
