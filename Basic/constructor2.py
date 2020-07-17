class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def printdetails(self):
		return "name:" + self.name + "\n age:" + str(self.age)
p1=person(input("enter name:"),input("enter age"))
p2=person(input("enter name:"),input("enter age"))
print(p1.printdetails())
print(p2.printdetails())
