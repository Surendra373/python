# class and objects

class electronic :
    operating_system="windows"
    ram=None
    hard_disk=None
    
    def __init__ (self,ram,hard_disk):  # dunded method # construct # call
        print ("its me suren")
    # pass
    
    def get_ram(self):
     return self.ram

laptop = electronic(10,200)

laptop.get_ram()

# print (laptop.operating_system)
# print (laptop.ram)
# print (laptop.hard_disk)