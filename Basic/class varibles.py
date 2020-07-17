class person:
    #class variable
    count=0
    
    def __init__(self,name,age):
        #instance variables
        self.name=name
        self.age=age
        person.count+=1 #call by class name

    #instance method        
    def print_objects_count(self):
        print("number of objects created",self.count)#reference

p1=person("vijay",2)
p1.print_objects_count()
p2= person("pankaj",22)
person.print_objects_count(p2)
