# function can return another function
def fun1(asd):
    def inner(dsf):
        return asd+dsf

    return inner
add=fun1("hello  ")
print(add("rassu"))