class person:
	def inputdetails(self):
		self.name=input("enter your name")
		self.age=int(input("enter your age"))
	def printdetails(self):
		print("name:",self.name)
		print("age:",self.age)

p1=person()
p2=person()
p1.inputdetails()
p2.inputdetails()
p1.printdetails()
p2.printdetails()
