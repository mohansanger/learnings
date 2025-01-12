my_list=[1,2,3,4,5]

itrator=iter(my_list)
print(next(itrator))
print(next(itrator))


class PowTwo:

    def __init__(self,max=0):
        self.max=max

    def __iter__(self):
        self.n=0
        return self
    def __next__(self):

        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            return StopIteration

numbers=PowTwo(3)
i=iter(numbers)
print("Iter:",next(i))
print("Iter:",next(i))
print("Iter:",next(i))
print("Iter:",next(i))
print("Iter:",next(i))

        
