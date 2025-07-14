option=int(input(("enter 1 for admin ,enter 2 for user:")))


class Airline():
    def airline_info(self,airlinename1,airlinename2):
        self.airline_name1=airlinename1
        self.airline_name2=airlinename2
    
    def print_info(self):
        print("airline 1 is:",self.airline_name1)   
        print("airline 2 is:",self.airline_name2) 
    
        
class Employee(Airline):
    
    def info_check():
        pass
    
    def change_details():
        pass
    
    def food_provision():
        pass
    
    
class Passengers(Airline):
    
    def ticket_booking():
        pass
    def available_flights():
        pass
    def cancel_ticket():
        pass
    
    

if option==1:
    password=input("enter password:")
    cpass="airline321"
    if password==cpass:
        Employee(Airline)
    else:
        print("please enter the correct password")
    
else:
    if option==2:
        Passengers(Airline)
        
    else:
        print("please enter a valid number")    
        



