def myfun():
    x = 300
    print(x)

myfun()


def myfunc():
    x = 400
    return x
    def myinnerfunc():
        print(x)
    myinnerfunc()

print(myfunc())


x = 500

def myfunc():
    x=200
    print(x)

myfunc()
print(x)

#####################
print("############################")

x = 300
 
def myfunc():
    global x
    x = 200

myfunc()

print(x)