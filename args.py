#正常寫法
#def add(a,b):
#    return a+b
#print(add(1,2)) #會跳出3
#--------------------------------------------------args(tuple)-----------------
def add(*args):
    total = 0
    for arg in args:
        print(f"args:{arg}")
        total += arg
    return total
print(add(1,2,3,4,5)) #會跳出15
#--------------------------------------------------kwargs(字典)-----------------
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"key:{key} value:{value}")
        
print_info(name="jerome", age="10") #會跳出key:name value:jerome key:age value:10