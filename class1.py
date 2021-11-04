
class Flight:
    def __init__(self, capacity):
        self.capacity=capacity
        self.passengers=[]
    
    def add_passengers(self, name):
        if self.capacity-len(self.passengers):
            self.passengers.append(name)
            return True
        else:
            return False
f=Flight(4)
passenger_list=["Derrick", "Joseph", "Collins", 'Sarah']

for i in passenger_list:
    if f.add_passengers(i) == True:
        print(f"{i} has been added")
    else:
        print("Flight fully booked")

print(f.passengers)






        
