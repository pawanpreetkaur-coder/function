def exappend(n):
    print("------------append()--------------------")
    n.append('the road')
    n.append('a little life')
    print(n)
exappend(['water margin','dream of the red chambe','a tale of two cities'])  

print("=======================================================")

def exinsert(n):
    print("---------------insert()-------------------")  
    n.insert(3,"orange")
    print(n)
exinsert(['apple','mango','grapes','pineapple'])  

print("=======================================================")  

def exadd():
    print("----------------------+------------------------")
    movies=['qismat','war','zombie land','jurassic world']
    add='sitaare zameen par'
    movies=movies+[add]
    print("after adding one more movie:",movies)
exadd()    

print("=======================================================")

def cextend():
    print("-----------------extend()-------------------------")
    print("movie1=['qismat','war','zombie land','jurassic world']")
    print("movie2=['sitaare zameen par','mr&mrs420']")
    movie1=['qismat','war','zombie land','jurassic world']
    movie2=['sitaare zameen par','mr&mrs420']
    movie1.extend(movie2)
    print("after extending both movies:",movie1)
cextend()

print("=======================================================")


def exdel():
    print("-------------del()---------------------")
    furniture=['bed','sofa','table','chair','dining table']
    del furniture[3]
    print("after deleting chair:",furniture)
exdel()

print("=======================================================")

def exremove():
    print("---------------remove()----------------")   
    fruits=['apple','mango','pineapple','orange','guava']
    fruits.remove("pineapple")
    print("after removing pineapple:",fruits) 
exremove()

print("=======================================================")

def expop():
    print("----------------pop()-----------------")
    colors=['red','green','blue','yellow','black']
    print(colors.pop(2))
    print("after pop method:",colors)
expop()    

print("=======================================================")

def exlen(n):
    print("---------------len()----------------")
    print("['apple','mango','grapes','orange','guava']")
    len(n)
    print("total fruits:",len(n))
exlen(['apple','mango','grapes','orange','guava'])  

print("=======================================================")

def excount(n):
    print("-------------count()-------------------")
    print("[10,20,30,60,20,20,40]")
    n.count(20) 
    print("20 repeats ",n.count(20),"times") 
excount([10,20,30,60,20,20,40])

print("=======================================================")

def exindex(n):
    print("---------------index()--------------")
    print("['yellow','blue','green','orange']")
    n.index('green')
    print("the position of green is at",n.index('green'))
    
exindex(['yellow','blue','green','orange'])

print("=======================================================")

def exsorted(n):
    print("-----------------sorted()------------------")
    print("[15,78,45,39,75,40,10]")
    sorted(n)
    print("after sorting n:",sorted(n))
exsorted([15,78,45,39,75,40,10])    

print("=======================================================")

def exmin(n):
    print("---------------------exmin()---------------------")
    print("[57,89,46,90,74,105,54]")
    min(n)
    print("minimum value is:",min(n))
exmin([57,89,46,90,74,105,54])    

print("=======================================================")

def exmax(n):
    print("--------------------max()----------------")
    print("[63,72,65,90,926,110,999]")
    max(n)
    print("maximum value is:",max(n))
exmax([63,72,65,90,926,110,999])   

print("=======================================================")

def exreverse(n):
    print("--------------reverse---------------")
    print("['sofa','table','chair','dining table','cupboard']")
    n.reverse()
    print("after reversing:",n)
exreverse(['sofa','table','chair','dining table','cupboard'])    