def func (*args):
    print(args)
    print(type(args))
func(1,2,3,4,5,6,7,8)
func('hello','world','helloworld',1,2,3,4)
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))

func2('')