def outerFun():
    message="Local"
    def innerFun():
        nonlocal message
        message="Non Local"
        print("Inner: ",message)
    
    innerFun()
    print("OuterFun: ",message)

outerFun()

c=1
def addFun():
    global c
    c=c+2
    print(c)

addFun()