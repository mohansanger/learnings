def make_multilpier(n):
    def multiplier(x):
        return x*n
    return multiplier

times3=make_multilpier(3)
print(f"Clousers can call inner function post outer:",times3(9))

times5=make_multilpier(5)
print(times5(3))