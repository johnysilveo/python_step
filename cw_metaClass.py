class MyClass:
    pass

obj = MyClass()
print(type(type(obj)))

num = "123"
print(type(type(num)))

def method1(self):
    print(self.prop1)

MyClass2 = type("Fuck",(),{'prop1':'test1','method1':method1})
obj2 = MyClass2()
print(type(obj2))
obj2.method1()



class MyMetaClass1(type):
    def __new__(cls,name,bases,dict):
        print("Method new start")
        print("type of class created",cls)
        print("class's name ",name)
        print("bases",bases)
        print('atrs',dict)
        return super().__new__(cls,name,bases,dict)


class MyClass3(metaclass=MyMetaClass1):
    pass

print(type(MyMetaClass1))
print(type(MyClass3))

class MyMetaClass2(type):
    def __new__(cls, name,bases,dict):
        if 'id' not in dict.keys():
            print(f"no id attr in the class {name}")
        else:
            countMethods = {key: value for key, value in dict.items() if callable(value)}
            if len(countMethods) > 2:
                print(f'More than 2 mathods in the class!')
            else:
                print(f"class {name} is creating...")
                return super().__new__(cls,name,bases,dict)

class MyClass4(metaclass=MyMetaClass2):
    attr = 100

class MyClass5(metaclass=MyMetaClass2):
    attr = 200
    id = 1

    def func1(self):
        pass

    def func2(self):
        pass

obj5 = MyClass5()
print(obj5.attr)

class MyMetaClass3(type):
    def __new__(cls, name,bases,dict,**kwargs):
        resultCls = super().__new__(cls,name,bases,dict)
        if kwargs:
            for key,value, in kwargs.items():
                setattr(resultCls,key,value)

        # if 'id' not in dict.keys():
        #     print(f"No id attr")
        #     resultCls.id = 42
        return resultCls

class User(metaclass=MyMetaClass3,fname='John',age=12):
    attr = 100

class Book(metaclass=MyMetaClass3):
    attr = 100

obj6 = User()
print(obj6.attr)
print(obj6.fname)
print(obj6.age)
book1 = Book()
print(book1.attr)