class Person():
    def __init__ (self,name,address,phone):  
        self.name = name
        self.address = address
        self.phone = phone
    def introduce(self):
        return "Hi my name is "+self.name


class Teacher(Person):
    def __init__ (self,name,address,phone,subject):
        Person.__init__ (self,name,address,phone)
        self.subject = subject
    def introduce(self):
        return "Hi my name is "+self.name+". I am a teacher."
class Student(Person):
    def __init__ (self,name,address,phone,group):
        Person.__init__(self,name,address,phone)  
        self.group = group
p = Person("Prajwal","Urlabari",9348394)
print(p.name)
t = Teacher("Anish","Donaa",121,"Python")
print(t.name,t.subject) 
s = Student("Ashim","Asthanagar",212,"CS101")
print(s.name,s.address,s.group)
print(s.introduce())
print(t.introduce())