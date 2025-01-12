d = {2: 56, 1: 2, 5: 12, 4: 24}
print(sorted(d))

for i in sorted(d.keys()):
    print(i,end=" ")

from collections import OrderedDict

d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, "Ajay":2, "Boy":20}

d1=OrderedDict(sorted(d.items()))

print(d1)