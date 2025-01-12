def MyGenerators(n):
    value=0
    while value<n:
        yield value
        value+=1


for c in MyGenerators(3):
  print(c)