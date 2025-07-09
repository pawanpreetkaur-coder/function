def exlen():
    print("---------len()-------------------")
    furniture=('table','chair','sofa','bed')
    print("the list is ('table','chair','sofa','bed') ")
    print("total stock:",len(furniture))
exlen()    

print("-------------------------------")
 
def excount():
    print("----------count()-----------------")
    fruits=('guava','apple','apple','mango')
    print("the list is ('guava','apple','apple','mango')")
    print("apple repeat",fruits.count('apple'),"times")  
    
excount()  

print("----------------------------------------")
   
def exindex():
    print("---------index()--------------------")
    cars=('bmw','venue','ford','scorpio')
    print("the list is ('bmw','venue','ford','scorpio')")
    print("the position of venue is at:",cars.index('venue'))
exindex()  

print("-------------------------------")

def exsorted():
    print("--------sorted()-----------------")
    totalcards=(4,7,3,1,2,5,9,6,8)
    aftersorting=sorted(totalcards)
    print("the cards are (4,7,3,1,2,5,9,6,8)")
    print("after sorting",aftersorting)
exsorted()

print("-------------------------------")

def exmin():
    print("----------min()----------------")
    marks=(98,20,67,43,57)
    minimummarks=min(marks)
    print("marks list is (98,20,67,43,57)")
    print("minimum marks is ",minimummarks)
exmin()     

print("-------------------------------")
     
def exmax():
    print("-----------max()-----------------")
    marks=(78,84,36,90,95)     
    maxmarks=max(marks)
    print("marks list is (78,84,36,90,95)")
    print("maxmarks is:",maxmarks)
exmax()    
    
    
    
    
    
    
    
    
    
    
