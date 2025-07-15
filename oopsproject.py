option=int(input(("enter 1 for admin ,enter 2 for user:")))

# class Airline():
#     def airline_info(self,airlinename1,airlinename2,airlinename3,airlinename4):
#         self.airline_name1=airlinename1
#         self.airline_name2=airlinename2
#         self.airline_name3=airlinename3
#         self.airline_name4=airlinename4

#     def print_info(self):
#         print("airline 1 is:",self.airline_name1) 
#         print("airline 2 is:",self.airline_name2) 
#         print("airline 3 is:",self.airline_name3) 
#         print("airline 4 is:",self.airline_name4)
        
    
class Employee():
    
    def passenger_info(self):
        print("-------------passengers information:---------------")
        name=['seerat','harshit','rakesh kumar','deepika','karan','harman']
        print(name[0])
        print(name[1])
        print(name[2])
        print(name[3])
        print(name[4])
        print(name[5])
        
        print("------------flights information-----------")
        flights=['indigo','air india','qatar airaways','singapore airlines']
        print("['indigo','air india','qatar airaways','singapore airlines']")
        
        print('delhi to canada--',flights[1],'--')
        print('amritsar to delhi--',flights[1],'--')
        print('delhi to singapore--',flights[0],'--')
        print('amritsar to dubai--',flights[3],'--')
        
        
        print("--------------------timings----------------------")
        print("take off                  stay                                         land")
        print(" 9pm(monday)             london (3hours)                 11pm(tuesday)     ")
        print(" 2am(monday)               no stay                         5am(tuesday)    ")
        print(" 6ampm(monday)             no stay                       12pm(tuesday)     ")
        print(" 12pm(monday)              no stay                        11pm(tuesday)    ")
        
        
        
        
    def change_details(self):
        print("-------------passengers information:---------------")
        name=['seerat','harshit','rakesh kumar','deepika','karan','harman']
        print(name[0])
        print(name[1])
        print(name[2])
        print(name[3])
        print(name[4])
        print(name[5])
        
        print("------------flights information-----------")
        flights=['indigo','air india','qatar airaways','singapore airlines']
        print("['indigo','air india','qatar airaways','singapore airlines']")
        
        print('delhi to canada--',flights[1],'--')
        print('amritsar to delhi--',flights[1],'--')
        print('delhi to singapore--',flights[0],'--')
        print('amritsar to dubai--',flights[3],'--')
        
        
        print("--------------------timings----------------------")
        print("take off                  stay                                         land")
        print(" 9pm(monday)             london (3hours)                 11pm(tuesday)     ")
        print(" 2am(monday)               no stay                         5am(tuesday)    ")
        print(" 6ampm(monday)             no stay                       12pm(tuesday)     ")
        print(" 12pm(monday)              no stay                        11pm(tuesday)    ")
        
        print("----------------------after some change in information----------------------------") 
           
        del name[3]  
        print('after removing name[3] the list is',name)
        
        del flights[0]
        print("available flights are:",flights)
        
        
          
    
    def food_provision(self):
        
        print("------------veg platter--------------------")
        veg=['dal chapati','rajma rice','poha','fried rice']
        print(veg)
    
    
        print("--------------------non-veg paltter----------------------")
        Non_Veg=['butter chicken','omellette','chicken nuggets','biryani']
        print(Non_Veg)
        
        
        print("---------------------beverages----------------------")
        print("beverages             price           discount      ")
        print("soft drink             250                         ")
        print("cold coffee            350                          ")
        print("milkshakes             300                          ")
        print(" tea                   450                          ")
        
        print("---------------------snacks----------------------")
        print("snacks            price         discount          ")
        print("cookies             150                           ")
        print("potato chips        200                           ")
        print("chocolates          250                           ")
        print("french fries        100                           ")
        
        
            
class Passengers():
    
    def ticket_booking(self):
        
        flight=['indigo','air india','Qatar airways','singapore airlines']
        print(flight)
        print("-------------------ECONOMY CLASS-----------------------")
        print(" flight                           flight name                  ticket price  ")
        print(f" amritsar to dubai               {flight[2]}                   15,000                  ")
        print(f" delhi to singapore              {flight[3]}                   20,000                  ")
        print(f" delhi to kerela                 {flight[0]}                   16,000                  ")
        print(f" amritsar to chandigarh          {flight[1]}                   10,000                  ")
        print(f" delhi to canada                 {flight[1]}                   30,000                  ")
        print(f" chandigarh to mumbai            {flight[0]}                   12,000                  ")
        
        
        print("-----------------------BUSINESS CLASS-------------------")
        print("flights                           flight name                  ticket price             ")
        print(f" amritsar to dubai               {flight[2]}                   30,000                  ")
        print(f" delhi to singapore              {flight[3]}                   45,000                  ")
        print(f" delhi to kerela                 {flight[0]}                   20,000                  ")
        print(f" amritsar to chandigarh          {flight[1]}                   15,000                  ")
        print(f" delhi to canada                 {flight[1]}                   50,000                  ")
        print(f" chandigarh to mumbai            {flight[0]}                   18,000                  ")
        

    def available_flights(self):
        
        print("----available flights------")
        flight=['indigo','air india','Qatar airways','singapore airlines']
        print(flight)
        print("----------from amritsar to delhi---------")
        print("flight                      timings")
        print(f"{flight[1] }                1hour20min" )
        
        print("-----------from delhi to mumbai----------")
        print(f" {flight[0]}                2hours      ")
        
        print("-----------from delhi to singapore-----------")
        print(f"{flight[3]}                  7hours         ")
        
        print("------------amritsar to dubai-----------------")
        print(f"{flight[2]}                  5hours          ")
    
        
        
    def cancel_ticket(self):
        print("----SELECT THE FLIGHT TO CANCEL TICKET----")
        
        flight=['indigo','air india','Qatar airways','singapore airlines']
        print(flight)
        print("-------------------ECONOMY CLASS-----------------------")
        print(" flight                           flight name                  ticket price  ")
        print(f" amritsar to dubai               {flight[2]}                   15,000                  ")
        print(f" delhi to singapore              {flight[3]}                   20,000                  ")
        print(f" delhi to kerela                 {flight[0]}                   16,000                  ")
        print(f" amritsar to chandigarh          {flight[1]}                   10,000                  ")
        print(f" delhi to canada                 {flight[1]}                   30,000                  ")
        print(f" chandigarh to mumbai            {flight[0]}                   12,000                  ")
        
        
        print("-----------------------BUSINESS CLASS-------------------")
        print("flights                           flight name                  ticket price             ")
        print(f" amritsar to dubai               {flight[2]}                   30,000                  ")
        print(f" delhi to singapore              {flight[3]}                   45,000                  ")
        print(f" delhi to kerela                 {flight[0]}                   20,000                  ")
        print(f" amritsar to chandigarh          {flight[1]}                   15,000                  ")
        print(f" delhi to canada                 {flight[1]}                   50,000                  ")
        print(f" chandigarh to mumbai            {flight[0]}                   18,000                  ")
        
        

if option==1:
    password=input("enter password:")
    cpass="airline321"
    if password==cpass:
        Employee()
        emp1=Employee()
        emp1.passenger_info()
        emp1.change_details()
        emp1.food_provision()
        
    else:
        print("please enter the correct password")
    

else:
    if option==2:
        Passengers()
        attendents=Passengers()
        
        attendents.ticket_booking()
        attendents.available_flights()
        attendents.cancel_ticket()
       
    else:
        print("please enter a valid number")    
    
       
# flight=Airline()
# flight.airline_info('indigo','Air india','Qatar airways','singapore airlines')
# flight.print_info()






    

