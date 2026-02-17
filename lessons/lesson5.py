def class_decorator(cls):
    class NewClass(cls):
        def method(self):
            print("New method")
    return NewClass

@class_decorator
class OldClass:
    def method(self):
        print("Old method")

obj_1 = Oldlass()
obj_1.method()
