def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == 'local':
                print('via local certification')
                func(*args,**kwargs)
            elif auth_type == 'ldap':
                print('via ldap certfication')
                func(*args, **kwargs)
        return wrapper
    return out_wrapper
@auth(auth_type='local')
#1.全部不带参数，相当于index=deco(index)
#2.被装饰函数带参数，相当于index=deco(index)=wrapper ->index(args)=wrapper(args)
#3.语法糖带参数，就需要多嵌套一层外层函数，将语法糖的参数传递给这一外层函数
def index(username,password):
    print('welcome to index page <local>',username)
index('yzw','secret')
@auth(auth_type='ldap')
def home(username,**kw):
    print('welcome to home page <ldap>',kw)
home('alex',a=2,b=3)