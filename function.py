
# Q function to find the even no in a range
# def evenno():
#     noare = []
#     a = int (input("entre st range:"))
#     b = int (input("entre ending range:"))

#     for i in range(a,b+1):
#         if(i%2==0):
#             print(i)
#             noare.append(i)

        
#         else:
#             pass
#     print(noare)
    

# evenno()

# def time_seconds_to_hour_minutes():
#     n = int(input("entre total seconds:"))
#     hours = n//3600
#     minutes=n//60 
#     seconds=n//1
#     print(hours,minutes,seconds)


# def time_calculate():
#     h = int(input("entre hours"))
#     m = int(input("minutes"))
#     s = int(input("seconds"))
#     m = int(input("entre time in seconds"))
#     hours = m//3600
#     print(hours)
#     minute =m%3600
#     print(minute)
#     minutes = minute//60
#     print(minutes)
#     seconds = minute%60
   
#     print(seconds)
#     print(hours,"hour",minutes,"minutes",seconds,"seconds")

# time_calculate()


            
def input_time():
    try:
        h = int(input("entre hours"))
        m = int(input("minutes"))
        s = int(input("seconds"))
        return h,m,s
    except ValueError:
        print("please entre only intigers")
        input_time()
    

def calculation():
            print("which operation you want to perform \n convert to second\n to minutes \n hours")

            
            n = str(input("entre your operation"))
            if(n=="seconds"):
                input_time()
                hour = h*3600
                minute = m*60
                second =s*1
                seconds =hour+minute+second
                print(second,"seconds")
            elif(n=="minutes"):
                input_time()
                hour= h*60
                minute =m*1
                second = s%60
                minutes= hour+minute+second
                print(minutes)
            elif(n=="hours"):
                input_time()
                hour = h*1
                minute = m%60
                second = s%3600
                hours = hour+minute+second
                print(hours)
            else:
                calculation()



def time_cal2():

    try:
        type= str(input("entre time or specific"))
        return type

        if(type=="specific"):
            calculation()
    
        elif(type=='time'):
            calculation2()
        else:
            print("try to entre time or specific")
            time_cal2()

    except ValueError:
        print("maybe you entred something wrong try to entre:\n time or specific ")
        time_cal2()


def calculation2():
            print("entre your type of input")
            n = str(input("entre your input type:second, minutes or hours"))
            if(n=="second"):
                s=int(input('entre seconds'))
                hour= s//3600
                minute= s%3600
                minutes= minute//60
                second = minute%1
                seconds = second//1
                print(hour,"hours",minutes,"minutes",seconds,"seconds")
            elif(n=="minutes"):
                m = int(input("entre minutes"))
                hour=m//60
                minute=m%60
                minutes=minute//1
                second= minutes%1
                seconds= second*60
                print(hour,"hours",minutes,"minutes",seconds,"seconds")
            elif(n=="hour"):
                h = float(input("entre your hours"))
                if(h%1<=0.6):

                    hour =h//1
                    minute = h%1
                    minutes = h%1*10
                    second = minutes%1
                    seconds = second//1
                    print(hour,"hours",minutes,"minutes",seconds,"seconds")


time_cal2()

def time_cal2():

    try:
        type= str(input("entre time or specific"))
        return type

        if(type=="specific"):
            calculation()
    
        elif(type=='time'):
            calculation2()
        else:
            print("try to entre time or specific")
            time_cal2()

    except ValueError:
        print("maybe you entred something wrong try to entre:\n time or specific ")
        time_cal2()



              
         

       

            
                       

                
        

    
    

