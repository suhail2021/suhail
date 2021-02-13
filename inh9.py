class Foo(object):
    @classmethod
    def hello(cls):
        print("hello from %s" % cls.__name__)
Foo.hello()