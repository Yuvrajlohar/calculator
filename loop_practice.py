#number = int(input("enter a number"))
#for a in range(1,11):
    #print(number*a)

#q2 

#for i in range(1,22):
    #if(i%2==0):
        #print(i)


##q3
#for a in range(2,22,2):
    #print(a)

##q4
#b=0
#for a in range(0,6):
    #b=a+b
    #print(b)
#print(b)
#
##q5
#string = "yuvraj"
#for a in string:
    #print(a)

#q6
#i =10
#while (i>0):
    #print(i)
    #i=i-1

##q7
#num= int(input("enter a number"))
#check=True
#for a in range(2,num):
    #if(num%a==0):
        #check=False
#if(check==False):
    #print(num,"is not a prime")
#else:
    #print(num,"is a prime")

##q8
#num = int(input("entre a number"))
#b=0
#for a in range(1,11,1):
    #print(a*num)
    #b=a*num+b
#print(b)

##q9
#num = int(input("enter a no"))
#b=1
#for a in range(1,num+1,1):
    #print(a)
    #b = a*b
#print("factorial of",num,"is",b)   

##q10
#string =str(input("entre your string" ))
#r=''
#for a in string:
    #r = a+r
#print(r)

#q11
#no = int(input("entre a number:"))
#
#for a in range(1,no+1):
#
    #print("*"*no)

##q12
#no = int(input("entre a number:"))
#for a in range(no+1):
    #print("*"*a)

#13
#no = int(input("entre a number:"))

#for i in range(1,no+1):
    #for j in range(1,i+1):
        #print(j,end=" ")
    ##print()

##14
#n = int (input("entere a no "))
#for i in range(n,0,-1):
    #print(" "*(n-i)+"*"*(i*2-1))

#for a in range(0,11):
    #print(a)


#b = 0
#for a in range(1,11):
    #b = b+a
    #print(a)
#print(b)

#n = int(input("entre a number"))
#
#for a in range(2,n-1):
    #if(n%a==0):
        #print("no is not prime")
        #break
#else:
     #print("prime")

#n = 3 #int(input("entre a number"))
#b=1
#for a in range(1,4):
    #b=b*a
#print(b)

#n =int(input("enter a no"))
#
#for a in range(0,n+1):
    #print("*"*n)

# n =int(input("enter a no"))

# for a in range(0,5,1):
#     for a in range (0,4):
#         if(a<4):
#             print("*"*a)
#         else:
#             print(a)    


# a=10
# # b=a+=1
# print(b)

#i = 1
## ab = int(input("Enter a Number?"))
#while (i <= 100):
    #if(i%5==0 and i%7==0) :
        #print(i)
    #i +=1
#else:
    #print("Loop finished!")

#n= int(input("entre a no:"))
#for a in range(n,0,-1):
    #for j in range(1,a+1):
        #print(j,end=" ")
    #print()

#n = int(input("entre a no "))
#for a in range(1,n+1):
    #print(" "*(n-a)+"*"*(a))

#Q
#total = 0
#stops = int(input("enter no of stops"))
#
#for i in range(1,stops+1):
    #get = int(input("pessenger get"))
    #off = int(input("pessenge"))
    #total=(total-off)+get
    #print(total)
#print(total)

#q
#a = 0
#for i in range(1,8):
    #temp=float(input("temperature"))
    #a=a+temp
#
#print(a/7,"is the average temperature of this week")

##Q to book a single seat 
#total_seats = int(input('entre total no of seats'))
#people = int(input("enter no of people you ask"))
#booked=0
#remaining=total_seats
#for a in range(0,people):
#
    #ans =str(input("yes or no ")).lower()
    #if(ans=='yes'):
        #print("seat booked")
        #booked = booked+1
        #remaining=remaining-1;
        #if(remaining==0):
            #break
    #elif(ans=='no'):
        #print("thank you")
#    
    #else:
        #print("you should write yes or no")
        #print("seats remaining:",remaining)
#        
#print(booked)
#print(remaining)

#Q to book seats as much you want 
# total_seats = int(input('entre total no of seats'))
# people = int(input("enter no of people you ask"))
# booked=0
# remaining=total_seats
# for a in range(0,people):
#     print("seats remaining:",remaining)
#     ans =str(input("do you want to book a seat: ")).lower()
#     if(ans=='yes'):
#         n=int(input("entre no of sets you want to book"))
#         if(n<=remaining):
#             print("seat booked",n)
#             booked = booked+n
#             remaining=remaining-n;
#             print(remaining,"seats remaining")
#             if(remaining==0):
#                 print("all booked")
#                 break
#         else:
#             print("Opps! \n maybe the no seats you want to book is more than seats available! \n try again")
        
#     elif(ans=='no'):
#         print("thank you")
    
#     else:
#         print("you should write yes or no")
#         print("seats remaining:",remaining)
#        
#print("seats booked",booked)
#print("no of seats remaining",remaining)

##Q
#n = int(input("entre a no "))
#
#for a in range(1,11):
    #c =a*n
    #print(f"{n}X{a}={c}")

##Q
#for a in range (1,6):
    #for i in range(0,a):
        #print(i+1,end="")
    #print()

##Q
#for a in range (1,6):
    #print("*"*a)

##Q
#for a in range(5,0,-1):
    #for i in range(1,a+1):
        #print(i,end="")
    #print()

#for a in range(1,5):
    #for i in range(1,5):
        #print(a,end="")
    #print()

#for a in range(1,5):
#        
    ##for i in range(1,a+1):
        #print(" "*(5-a)+"*"*a,end="")
        #print()


# x = int(input("entre st of your range"))
# y = int(input("entre end no of your range"))
# #sir
# for i in range(1,11):
#     print()
#     for a in range(1,12):
#             if (i==1 or i== 6  or (a==11 and i<=6) or a==1 or (i==7 and a==2)):
#                 print("*", end="")
#             elif( a<=10 and i<=6 ):
#                 print(" " ,end="")
             
            

# for a in range (1,12):
    
#     for b in range(1,12):
#         if(b==1 or (b==10 and a<=6)):
#             print("*")
#         elif(a ==1 or a==6):
#             print("*",end="")

# for i in range(1,11):
#     print("")
#     for j in range(1,11):
#         if (i<=11 and j==11):
#             print("1")
#         elif (i == 6 or j==6 or (j==1 and i<6) or (j==11 and i>6) or (i==1 and j>6) or (i==11 and j<6 )):
#             print("*" ,end="")


# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     print()
#     for j in range(1,i):
#         print(j,end="")



# 54321
# 4321
# 321
# 21
# 1

# for i in range(5,0,-1):
#     print()
#     for j in range(1,i+1):
#         print(j,end="")

# 55555
# 4444
# 333
# 22
# 1

# for i in range(5,0,-1):
#      print()
#      for j in range(1,i+1):
#          print(i,end="")

# 6   
# 34 
# 345
# 3456


# for i in range(3,8):
#     print()
#     for j in range(3,i):

#         if(i==4):
#             print(j*2)
#         else:    
#             print(j, end="")



# 6
# 16
# 126
# 1236
# 12346
# 123456

# for i in range(0,6):
#     print()
#     for j in range(1,i+2):
#         if(j==i+1 or i==0):
#             print("6",end="")
#         else:

#             print(j,end="")

# 654321
# 64321
# 6321
# 621
# 61
# 6

# for i in range(6,0,-1):
#     print()
#     for j in range(i,0,-1):
#         if(j==i):
#             print("6",end="")
#         else:
#             print(j,end="")
        
#     *    
#    ***   
#   *****  
#    ***   
#     *    


# n= int(input("entre a odd no "))
# for i in range(1,n+1,2):
#     print(" "*(n-i//2)+"*"*i)
# for i in range(n-2,0,-2):
#     print(" "*(n-i//2)+"*"*i)

# ****
# *  *
# *  *
# ****

# for i in range(1,5):
#     print()
#     for j in range(1,5):

#         if((i==2 and j==2) or(i==3 and j==2)or(i==2 and j==3)or(i==3 and j==3)):
#             print(" ",end="")
#         else:
#             print("*",end="")

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# n = int(input("Enter number of rows: "))
# for i in range(n):
#     num = 1
#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()
# n = int(input("entre a odd no:"))
# for i in range(1,n+1):
#     if(i==1):
#             print("*")
#     elif(i>1 and i<5):
#           print("")
#     elif(i==n):
#           for j in range(1,n+1):
#                 print("*",end="")

# a=int(input("eenter Number"))

# for i in range(1,a,a):

#     i=i*i
#     print(i)




# a = [2,2,4,5,7,8,3,2,2]
# a.reverse()
# print(a)




# y= int(input("enter emp id"))

# for i in range(0,len(a)):

#     if i==y:
#         continue
#     else:
#         b= int(a[i])
#         print(type(b))

# import array as r
# my_array = r.array('u',["e","d"])

# print(my_array[0])
    
a='hello yavraj'

print(a[9])
    
        
           
        

        
            
    
        
        

           
