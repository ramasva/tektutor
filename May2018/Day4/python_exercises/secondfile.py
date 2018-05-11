class  MyClass:

 def __init__(self):
  print("Myclass Constructor")
  self.x=10
  self.y=25

 def secondfunction(self):
  print("coming from secondfunction")
  print( __name__ )
  print("X is =", self.x )
  print(" Y is =" + str(self.y))
