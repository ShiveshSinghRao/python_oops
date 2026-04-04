class A:
    @staticmethod
    def add(a,b):
        return a+ b
    
# option A:  Call on teh calss directly ( no obj)
result = A.add(3,4)
print(result)

# Option B: call on a instance also works but self is not passed 
res2= A()
ans = A.(39,1)
print(ans)




# What is it?
# A staticmethod is a method that belongs to a class but doesn't have access to the instance (self)
#  or the class (cls). It's essentially a regular function that just happens
#  to live inside a class's namespace.