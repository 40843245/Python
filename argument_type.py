#ex6-3-3.py
#argument_type

#postional arguments and keyword arguments
#positional arguments:
#def f(*args):
# function of * is that args will be converted to tuple type

#keyword arguments:
#def f(**kwargs):
# function of ** is that kwargs will be converted to dict type

def f_pa(*args):
    print("args is",args)
    print("Is args a tuple type?",type(args)==type(tuple()))
def f_kwa(**kwargs):
    print("args is",kwargs)
    print("Is args a tuple type?",type(kwargs)==type(dict()))
def f_pa_mixed(start=1,*args):
    print("starter is",start)
    print("kwargs is",args)
    print("Is kwargs a tuple type?",type(args)==type(tuple()))
def f_all_mixed(start=100,*args,**kwargs):
    print("starter is",start)
    print("args is",args)
    print("Is kwargs a tuple type?",type(args)==type(tuple()))
    print("kwargs is",kwargs)
    print("Is kwargs a dict type?",type(kwargs)==type(dict()))
    
f_pa(1,2,3)
f_pa(1,2,3,4)
# f_kwa(1,2,3)      #TypeError: f_kwa() takes 0 positional arguments but 3 were given
#f_kwa(1,2,3,4)     #TypeError: f_kwa() takes 0 positional arguments but 3 were given
f_kwa(a=1,b=2,c=3)
f_kwa(a=1,b=2,c=3,d=4)

f_pa_mixed(1,2,3)
#f_pa_mixed(1,start=2,3)#SyntaxError: positional argument follows keyword argument
f_pa_mixed()
f_pa_mixed(start=5)
#f_pa_mixed(start=5,12)  #SyntaxError: positional argument follows keyword argument
#f_pa_mixed(1,2,start=5)#SyntaxError: positional argument follows keyword argument
f_all_mixed(100,200,500,a=5,b=2)
f_all_mixed(100,200,500,a=5,b=2)
#SyntaxError: positional argument follows keyword argument
#f_all_mixed(start=20,200,500,a=5,b=2)
#TypeError: f_all_mixed() got multiple values for argument 'start'
#            start           start
#f_all_mixed(200,500,a=5,b=2,start=50)