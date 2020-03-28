
def my_argument(*args):
    print args

my_argument(123, 234)

def other_fuc(arg1, arg2):
    print arg1
    print arg2

a = (123, 345)
other_fuc(*a)

def keyarg_func(**kwargs):
    for key in kwargs:
        print "Key: {} - Value: {}".format(key, str(kwargs[key]))

keyarg_func(argument1=123, othervar=3)
