# passing function as arguments
def function1(text):
    return text.upper()
def fucntion2(asd):
    return asd

def greet(fun):
    greeting=fun("hi this is Rasagnya")
    print(greeting)
greet(function1)
greet(fucntion2)


