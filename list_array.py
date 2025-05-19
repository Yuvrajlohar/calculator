# list = [2,,4,"hello",.4,True]
# print(type(list))

# import array
# arr = array.array('l')


# a= [89,1156,876,86]


# c=a[0]

# for b in range(0,4,1):
        
# print(-len(a),-1,1)

    # if (c< a[b]):

        # c= a[b]
    # else:
    #         r = a[0]    

    # if (a[2]< a[]):

    #     q= a[]
    # else:
    #     q = a[2]    

     
    # if (r<q):


    #     w= q
    # else:
    #     w= r        

# print(c)       


# b = lambda a,b,c : a * b * c *8
# print(b(,4,5))


def entre():

    try:
        a = float(input("entre first no"))
        b = float(input("entre second no "))
        return a,b
        
      
    except ValueError:
        print("invalid input ! please enter a numeric value ,not string")
        return entre()

print("function you can perform is ","+","-","*","/","%","//","**")

a,b = entre()
print("your input is:","a=",a,"b=",b)



def plus(a,b):
    print(a+b)
def sub(a, b):
    print(a-b)
def multiplication(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)
def modulus(a,b):
    print(a%b)
def floordivision(a,b):
    print(a//b)
def exponent(a,b):
    print(a**b)

def xyz():
    print("please entre any one ","+","-","*","/","%","//","**")
    function = str(input("entre your function:"))
    
    if(function=="+"):

        
        plus(a,b)
    
    elif(function=="-"):
        
        sub(a,b)
    
    elif(function=="*"):
        
        multiplication(a,b)
    
    elif(function=="/"):
        
        divide(a,b)
    
    elif(function=="%"):
        
        modulus(a,b)
    
    elif(function=="//"):
        
        floordivision(a,b)
    
    elif(function=="**"):
        
        exponent(a,b)
    
    else:
        print("wrong operation entered")
        wrong()

def wrong():    
    xyz()
        
xyz()



    
# import array
# arr = array.array('i',[,4,5,5,6,6])
# arr2 = array.array('i',[])


# for b in range(-1,-len(arr)-1,-1):
#     arr2.append(arr[b])
# print(arr2)



# import array
# type = str(input("type of array-float,int:"))
# if(type=='float'):
#     arr=array.array('f',[])
# elif(type=='int'):
#     arr=array.array('i',[])

# size = int(input("entre size of the array"))
# for i in range (0,size,1):
#     num = float(input("entre your no"))
#     arr.append(num)
#     print(arr[i])
# print(arr)
