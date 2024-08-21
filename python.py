# Decorators with ags
def decorator(f):
    def wrapper(a,b):
        print("i")
        f(a,b)
    return wrapper
    
@decorator
def function(a,b):
    print(a+b)
    
    
#Overloading += operator 
class A:
    
    def __init__(self, x) -> None:
        self.x = x
    def __iadd__(self,b):
        print(b)
        return self.x*b

a = A(10)
a += 2
print(a)
