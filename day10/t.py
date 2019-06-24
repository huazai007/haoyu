def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print("oo")
            func(*args,**kwargs)
        return wrapper
    return outer_wrapper