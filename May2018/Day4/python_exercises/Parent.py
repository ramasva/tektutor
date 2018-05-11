class Parent:

  def __init__(self):
    print("Inside construtor")
    self.__privateData = 100
    self._protectedData = 200
    self.publicData=300


  def setValues(self,val1,val2,val3):
    self.__privateData = val1
    self._protectedData = val2
    self.publicData=val3

  def printValues(self):
    print ("private = "+ str(self.__privateData))  
    print ("protected = "+ str(self._protectedData))  
    print ("public = "+ str(self.publicData))  


class Child(Parent):
  def __init__(self):
    Parent.__init__(self)
    self.data=2000

def main():
  obj1 = Child()
  print("values before set function")
  obj1.printValues()
  obj1.setValues(500,600,700)
  print("values after set function")
  obj1.printValues()

  print("Read public ", obj1.publicData)
  print("Read protected ", obj1._protectedData)
  print("Read child data  ", obj1.data)
  #print("Read private ", obj1.__privateData)



main()
