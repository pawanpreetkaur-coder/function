name=input("enter name:")
Gamingname=input("enter gaming name:")
DOB=(input("enter date of birth:"))
gender=input("enter gender:")
phNo=int(input("enter phone number:"))
address=input("enter address:")
email=input("enter email id:")
age=int(input("enter age:"))

if age>=18:
    print("----you can proceed the game-----")
    
          
    
    password=input("enter password:")
    Cpass=input("enter Cpass:") 
    if Cpass==password:
        print("you can proceed ")
        print("---please read and agree the terms and conditions before entering the quiz---")
    
        print("1.once you leave the game you have to enter all the details again. ")
        print("2.each questions carry one point.")
        print("3.each questions has its time limit of 2 minutes.")
        print("4.There will total 7 questions.")
        print("5.You cannot skip any question.")
        print("6.all the question is based on informational technology.")
        print("7. you cannot share the data.")
        print("8.no cheating is allowed.")
        print("9.If any rule is breaked ,game is automattically stoped.")
        option=input("do you agree with these terms and conditions(yes/no)?:")
        if option=="yes"  or option=="Yes" or option=="YES":
            print("----you can enter the game----") 
            print("****WELCOME TO QIZ GAME****") 
           
            score=0
            
            print("1.Who developed python programming language?")  
            a=print("a.bjarne stroustrup") 
            b=print("b.rasmus lerdorf")
            c=print("c.guido van rossum")
            d=print("d.wick van rossum")
            correctAnswer="c"
            guess=input("answer is :")
            if guess==correctAnswer:
               print("correct answer")
               score+=1
        
            else:
                chances=3
                while chances>0:
                    print("wrong answer....try again")
                    guess=input("answer is:")
                    if guess==correctAnswer:
                       print("correct answer")
                       score+=1
                       break
                    else:
                     chances-=1
                    if chances==0:
                        print("no chance left")
                        print("correct answer is c ")
                    else:
                        print("chance left:",chances)
    
                        
            print("2.which of the following is correct extension for python?")
            a=print("a. .python")
            b=print("b.  .py")
            c=print("c.  .pl") 
            d=print("d. .p")
            correctAnswer="b"
            guess=input("answer is :") 
            if guess==correctAnswer:
               print("correct answer")
               score+=1
        
            else:
                chances=3
                while chances>0:
                    print("wrong answer....try again")
                    Guess=input("answer is:")
                    if Guess==correctAnswer:
                       print("correct answer")
                       score+=1
                       break
                    else:
                     chances-=1
                    if chances==0:
                        print("no chance left")
                        print("the correct answer is b")
                    else:
                        print("chance left:",chances)
                        
                        
            print("3. which of the following is not a valid datatype?")
            a=print("a. int")
            b=print("b. char")
            c=print("c. float")
            d=print("d. string")
            correctAnswer="b"
            guess=input("answer is :") 
            if guess==correctAnswer:
               print("correct answer")
               score+=1
        
            else:
                chances=3
                while chances>0:
                    print("wrong answer....try again")
                    Guess=input("answer is:")
                    if Guess==correctAnswer:
                       print("correct answer")
                       score+=1
                       break
                    else:
                     chances-=1
                    if chances==0:
                        print("no chance left")
                        print("the correct answer is b")
                    else:
                       print("chance left:",chances)
                        
            print("4. what does the break statement do in python?")
            a=print("a. it terminates the program easily")
            b=print("b.  it raises an exception")
            c=print("c. it continues to the next")
            d=print("d. it breaks out the current loop and resume execution at the next statement")
            correctAnswer="d"
            guess=input("answer is :") 
            if guess==correctAnswer:
               print("correct answer")
               score+=1
        
            else:
                chances=3
                while chances>0:
                    print("wrong answer....try again")
                    Guess=input("answer is:")
                    if Guess==correctAnswer:
                       print("correct answer")
                       score+=1
                       break
                    else:
                     chances-=1
                    if chances==0:
                        print("no chance left")
                        print("the correct answer is d")
                    else:
                        print("chance left:",chances)
                        
            print("5. what will be the output of: print(2**3)?")
            a=print("a. 5")
            b=print("b. 8")
            c=print("c. 9")
            d=print("d. 4")
            correctAnswer="b"
            guess=input("answer is :") 
            if guess==correctAnswer:
               print("correct answer")
               score+=1
        
            else:
                chances=3
                while chances>0:
                    print("wrong answer....try again")
                    Guess=input("answer is:")
                    if Guess==correctAnswer:
                       print("correct answer")
                       score+=1
                       break
                    else:
                     chances-=1
                    if chances==0:
                        print("no chance left")
                        print("the correct answer is b")
                    else:
                        print("chance left:",chances)
                        
                        
            print("6. what is the use of in operator?")
            a=print("a. checks membership")
            b=print("b. adds value")
            c=print("c. multiplies items")
            d=print("d. compares identity")
            correctAnswer="a"
            guess=input("answer is :") 
            if guess==correctAnswer:
               print("correct answer")
               score+=1
        
            else:
                chances=3
                while chances>0:
                    print("wrong answer....try again")
                    Guess=input("answer is:")
                    if Guess==correctAnswer:
                       print("correct answer")
                       score+=1
                       break
                    else:
                     chances-=1
                    if chances==0:
                        print("no chance left")
                        print("the correct answer is a")
                    else:
                       print("chance left:",chances)
                        
            print("7. what does range(5) return?")
            a=print("a. [1,2,3,4,5]")
            b=print("b. [0,1,2,3,4]")
            c=print("c. [0,1,2,3,4,5]")
            d=print("d. [1,2,3,4]")
            correctAnswer="b"
            guess=input("answer is :") 
            if guess==correctAnswer:
               print("correct answer")
               score+=1
        
            else:
                chances=3
                while chances>0:
                    print("wrong answer....try again")
                    Guess=input("answer is:")
                    if Guess==correctAnswer:
                       print("correct answer")
                       score+=1
                       break
                    else:
                     chances-=1
                    if chances==0:
                        print("no chance left")
                        print("the correct answer is b")
                    else:
                        print("chance left:",chances)
                        
                 
            print("total score:",score) 
            print("**********Congratlations**********")                                                                   
                                     
            print("~~~~~~~~~~~~~~~:::::::Certificate:::::::~~~~~~~~~~~~~~~~") 
            print("This certificate is awarded to ")
            print("Username:",name)
            print("Gamingname:",Gamingname)
            print("Score:",score)
            print("**************XXXXXXXXX********************")      
        else:
            print("-------------NO ENTRY----------")
                    
    else:
        print("try again")
        passWord=input("enter password:")
        cpass=input("enter cpass:")
        if cpass==passWord:
            print("you can proceed")
            print("---please read and agree the terms and conditions before entering the quiz---")
    
            print("1.once you leave the game you have to enter all the details again. ")
            print("2.each questions carry one point.")
            print("3.each questions has its time limit of 2 minutes.")
            print("4.There will total 7 questions.")
            print("5.You cannot skip any question.")
            print("6.all the question is based on informational technology.")
            print("7. you cannot share the data.")
            print("8.no cheating is allowed.")
            print("9.If any rule is breaked ,game is automattically stoped.")
            option=input("do you agree with these terms and conditions(yes/no)?:")
            if option=="yes"  or option=="Yes" or option=="YES":
                print("----you can enter the game----") 
                print("****WELCOME TO QIZ GAME****") 
                score=0
                print("1.Who developed python programming language?")  
                a=print("a.bjarne stroustrup") 
                b=print("b.rasmus lerdorf")
                c=print("c.guido van rossum")
                d=print("d.wick van rossum")
                correctAnswer="c"
                guess=input("answer is :") 
                if guess==correctAnswer:
                   print("correct answer")
                   score+=1
            
                else:
                    chances=3
                    while chances>0:
                        print("wrong answer....try again")
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                           print("correct answer")
                           score+=1
                           break
                        else:
                         chances-=1
                        if chances==0:
                            print("no chance left")
                            print("the correct answer is c")
                        else:
                            print("chance left:",chances)
                            
                print("2.which of the following is correct extension for python?")
                a=print("a. .python")
                b=print("b.  .py")
                c=print("c.  .pl") 
                d=print("d. .p")
                correctAnswer="b" 
                guess=input("answer is :") 
                if guess==correctAnswer:
                   print("correct answer")
                   score+=1
            
                else:
                    chances=3
                    while chances>0:
                        print("wrong answer....try again")
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                           print("correct answer")
                           score+=1
                           break
                        else:
                         chances-=1
                        if chances==0:
                            print("no chance left")
                            print("the correct answer is b")
                        else:
                            print("chance left:",chances)
                        
                print("3. which of the following is not a valid datatype?")
                a=print("a. int")
                b=print("b. char")
                c=print("c. float")
                d=print("d. string")
                correctAnswer="b"
                guess=input("answer is :") 
                if guess==correctAnswer:
                   print("correct answer")
                   score+=1
            
                else:
                    chances=3
                    while chances>0:
                        print("wrong answer....try again")
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                           print("correct answer")
                           score+=1
                           break
                        else:
                         chances-=1
                        if chances==0:
                            print("no chance left")
                            print("the correct answer is d")
                        else:
                            print("chance left:",chances)
                            
                            
                print("4. what does the break statement do in python?")
                a=print("a. it terminates the program easily")
                b=print("b.  it raises an exception")
                c=print("c. it continues to the next")
                d=print("d.  it breaks out the current loop and resume execution at the next statement")
                correctAnswer="d"
                guess=input("answer is :") 
                if guess==correctAnswer:
                   print("correct answer")
                   score+=1
            
                else:
                    chances=3
                    while chances>0:
                        print("wrong answer....try again")
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                           print("correct answer")
                           score+=1
                           break
                        else:
                         chances-=1
                        if chances==0:
                            print("no chance left")
                            print("the correct answer is d")
                        else:
                            print("chance left:",chances)
                
                print("5. what will be the output of: print(2**3)?")
                a=print("a. 5")
                b=print("b. 8")
                c=print("c. 9")
                d=print("d. 4")
                correctAnswer="b"
                guess=input("answer is :") 
                if guess==correctAnswer:
                   print("correct answer")
                   score+=1
            
                else:
                    chances=3
                    while chances>0:
                        print("wrong answer....try again")
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                           print("correct answer")
                           score+=1
                           break
                        else:
                         chances-=1
                        if chances==0:
                            print("no chance left")
                            print("the correct answer is b")
                        else:
                            print("chance left:",chances)
                        
                print("6. what is the use of in operator?")
                a=print("a. checks membership")
                b=print("b. adds value")
                c=print("c. multiplies items")
                d=print("d. compares identity")
                correctAnswer="a"
                guess=input("answer is :") 
                if guess==correctAnswer:
                   print("correct answer")
                   score+=1
            
                else:
                    chances=3
                    while chances>0:
                        print("wrong answer....try again")
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                           print("correct answer")
                           score+=1
                           break
                        else:
                         chances-=1
                        if chances==0:
                            print("no chance left")
                            print("the correct answer is a")
                        else:
                          print("chance left:",chances)
                        
                print("7. what does range(5) return?")
                a=print("a. [1,2,3,4,5]")
                b=print("b. [0,1,2,3,4]")
                c=print("c. [0,1,2,3,4,5]")
                d=print("d. [1,2,3,4]")
                correctAnswer="b"
                guess=input("answer is :") 
                if guess==correctAnswer:
                   print("correct answer")
                   score+=1
            
                else:
                    chances=3
                    while chances>0:
                        print("wrong answer....try again")
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                           print("correct answer")
                           score+=1
                           break
                        else:
                         chances-=1
                        if chances==0:
                            print("no chance left")
                            print("the correct answer is b")
                        else:
                            print("chance left:",chances)
                 
                print("total score:",score) 
                print("**********Congratlations**********")                                                                   
                                         
                print("~~~~~~~~~~~~~~~:::::::Certificate:::::::~~~~~~~~~~~~~~~~") 
                print("This certificate is awarded to ")
                print("Username:",name)
                print("Gamingname:",Gamingname)
                print("Score:",score)
                print("**************XXXXXXXXX********************")  
            else:
                print("-------------NO ENTRY----------")
                        
        else:
            maxAttempts =3
            for attempt in range(1,3):
                enterpass=input(f"attempt:{attempt} enter password:")
                if enterpass==password:
                    print("password matched")
                    print("---please read and agree the terms and conditions before entering the quiz---")
    
                    print("1.once you leave the game you have to enter all the details again. ")
                    print("2.each questions carry one point.")
                    print("3.each questions has its time limit of 2 minutes.")
                    print("4.There will total 7 questions.")
                    print("5.You cannot skip any question.")
                    print("6.all the question is based on informational technology.")
                    print("7. you cannot share the data.")
                    print("8.no cheating is allowed.")
                    print("9.If any rule is breaked ,game is automattically stoped.")
                    option=input("do you agree with these terms and conditions(yes/no)?:")
                    if option=="yes"  or option=="Yes" or option=="YES":
                        print("----you can enter the game----") 
                        print("****WELCOME TO QIZ GAME****") 
                        score=0
                        print("1.Who developed python programming language?")  
                        a=print("a.bjarne stroustrup") 
                        b=print("b.rasmus lerdorf")
                        c=print("c.guido van rossum")
                        d=print("d.wick van rossum")
                        correctAnswer="c"
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                             print("correct answer")
                             score+=1
            
                        else:
                         chances=3
                         while chances>0:
                             print("wrong answer....try again")
                             Guess=input("answer is:")
                             if Guess==correctAnswer:
                                print("correct answer")
                                score+=1
                                break
                             else:
                              chances-=1
                             if chances==0:
                                 print("no chance left")
                                 print("the correct answer is c")
                             else:
                                 print("chance left:",chances)
                                    
                        print("2.which of the following is correct extension for python?")
                        a=print("a. .python")
                        b=print("b.  .py")
                        c=print("c.  .pl") 
                        d=print("d. .p")
                        correctAnswer="b" 
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                             print("correct answer")
                             score+=1
            
                        else:
                         chances=3
                         while chances>0:
                             print("wrong answer....try again")
                             Guess=input("answer is:")
                             if Guess==correctAnswer:
                                print("correct answer")
                                score+=1
                                break
                             else:
                              chances-=1
                             if chances==0:
                                 print("no chance left")
                                 print("the correct answer is b")
                             else:
                                 print("chance left:",chances)
                                 
                        print("3. which of the following is not a valid datatype?")
                        a=print("a. int")
                        b=print("b. char")
                        c=print("c. float")
                        d=print("d. string")
                        correctAnswer="b"
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                             print("correct answer")
                             score+=1
            
                        else:
                         chances=3
                         while chances>0:
                             print("wrong answer....try again")
                             Guess=input("answer is:")
                             if Guess==correctAnswer:
                                print("correct answer")
                                score+=1
                                break
                             else:
                              chances-=1
                             if chances==0:
                                 print("no chance left")
                                 print("the correct answer is b")
                             else:
                                 print("chance left:",chances)
                                 
                        print("4. what does the break statement do in python?")
                        a=print("a. it terminates the program easily")
                        b=print("b.  it raises an exception")
                        c=print("c. it continues to the next")
                        d=print("d. it breaks out the current loop and resumes execution at the next statement")
                        correctAnswer="d"
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                             print("correct answer")
                             score+=1
            
                        else:
                         chances=3
                         while chances>0:
                             print("wrong answer....try again")
                             Guess=input("answer is:")
                             if Guess==correctAnswer:
                                print("correct answer")
                                score+=1
                                break
                             else:
                              chances-=1
                             if chances==0:
                                 print("no chance left")
                                 print("the correct answer is d")
                             else:
                                 print("chance left:",chances)   
                        
                        print("5. what will be the output of: print(2**3)?")
                        a=print("a. 5")
                        b=print("b. 8")
                        c=print("c. 9")
                        d=print("d. 4")
                        correctAnswer="b"
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                             print("correct answer")
                             score+=1
            
                        else:
                         chances=3
                         while chances>0:
                             print("wrong answer....try again")
                             Guess=input("answer is:")
                             if Guess==correctAnswer:
                                print("correct answer")
                                score+=1
                                break
                             else:
                              chances-=1
                             if chances==0:
                                 print("no chance left")
                                 print("the correct answer is b")
                             else:
                                 print("chance left:",chances)
                                 
                                 
                        print("6. what is the use of in operator?")
                        a=print("a. checks membership")
                        b=print("b. adds value")
                        c=print("c. multiplies items")
                        d=print("d. compares identity")
                        correctAnswer="a"
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                             print("correct answer")
                             score+=1
            
                        else:
                         chances=3
                         while chances>0:
                             print("wrong answer....try again")
                             Guess=input("answer is:")
                             if Guess==correctAnswer:
                                print("correct answer")
                                score+=1
                                break
                             else:
                              chances-=1
                             if chances==0:
                                 print("no chance left")
                                 print("the correct answer is a")
                             else:
                                 print("chance left:",chances)
                                 
                        print("7. what does range(5) return?")
                        a=print("a. [1,2,3,4,5]")
                        b=print("b. [0,1,2,3,4]")
                        c=print("c. [0,1,2,3,4,5]")
                        d=print("d. [1,2,3,4]")
                        correctAnswer="b"
                        Guess=input("answer is:")
                        if Guess==correctAnswer:
                             print("correct answer")
                             score+=1
            
                        else:
                         chances=3
                         while chances>0:
                             print("wrong answer....try again")
                             Guess=input("answer is:")
                             if Guess==correctAnswer:
                                print("correct answer")
                                score+=1
                                break
                             else:
                              chances-=1
                             if chances==0:
                                 print("no chance left")
                                 print("the correct answer is b")
                             else:
                                 print("chance left:",chances)
                                 
                        print("total score:",score) 
                        print("**********Congratlations**********")                                                                   
                                                 
                        print("~~~~~~~~~~~~~~~:::::::Certificate:::::::~~~~~~~~~~~~~~~~") 
                        print("This certificate is awarded to ")
                        print("Username:",name)
                        print("Gamingname:",Gamingname)
                        print("Score:",score)
                        print("**************XXXXXXXXX********************")  
                    break         
                if maxAttempts==attempt:
                    print("you have used your two attempts")
                else:
                    print("password is not matched")
            else:
                print("-------------NO ENTRY----------")
                
                 

else:
    print("age is not valid")       
        
            
    
    
     
        
    
        
            
           
            
        
    
    

        
    
    
