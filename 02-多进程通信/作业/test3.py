a = 1

def func1():
    global a
    a = 2

def func2():
    # global a
    print(a)

func1()
func2()