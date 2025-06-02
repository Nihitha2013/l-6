class overload:
    def __init__(self,v):
     self.v=v

    def __lt__(self,other):
       if self.v < other.v:
             return "ob1 is less than ob2"
       else:
           return "ob1 is greater than ob2"
       
    def __eq__(self,other):
       if self.v == other.v:
             return "ob1 is equal t0 ob2"
       else:
           return "ob1 is not equal to ob2"
       
    
ob1=overload(40)
ob2=overload(20)
print("Passed values", ob1.v,ob2.v)
print(ob1==ob2)