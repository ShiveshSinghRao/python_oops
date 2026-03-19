class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Cannot fly")  #  breaks LSP
    



"""

Child should behave like parent
    
    
"""