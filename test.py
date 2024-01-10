conf = [ 1, 2]

def func(a, b,c):
    print(f"a: {a}, b: {b}, c: {c}")
    

func(*conf, c="selam")


print(type(func))