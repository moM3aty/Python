class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers =[]

    def add_passenger(self,name):

        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Momen","M3aty","Be3o","Mohab","Elmogy"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to the Flight successfully")
    else:
        print(f"Sorry, No avilable seats for {person}")
    
