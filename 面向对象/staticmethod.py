class A:
    bar =1
    def foo(self):
        print("foo")
    @staticmethod
    def static_foo(values):
        print("static_foo")
        print(A.bar+1)
        print(values)
    @classmethod
    def class_foo(cls,values):
        print("class foo")
        print(cls.bar-1)
        print(values)
A.static_foo("haha")
A.class_foo("hehe")


def aa(*args):
    print(args)
aa("putong_func,heihei")
