class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    
    dic = {}
    lst = [] 

    obj1 = MyClass("Jeff", 10)
    obj2 = MyClass("Jam", 12)
    dic[1] = obj1
    dic[2] = obj2 
    lst.append(obj1)
    lst.append(obj2) 

    #obj3.age = 11
    obj3 = dic[1]
    xx = MyClass(dic[1])
    print(obj3.age)
    obj3.age = 14
    print(obj1.age)
    print(xx.age)
    print(dic[1].age)
    print(lst[0].age)
    print(lst[1].age)

    