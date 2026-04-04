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

