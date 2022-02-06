#Add a function below called divisors(num) which takes one argument of type integer
#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder
#define the funciton header called divisors expecting one argument
#the 
def divisors(number):
    #set up an empty list to hold your result
    divisorList = []
    #loop i from 1 to the number you are checking
    for i in range(1,number):
        #if the remainder when dividing the number by i is equal to zero - i is a divisor so...
        if (number%i==0):
            #apend i to the list you set up
            divisorList.append(i)
       
 
    #return the list
    return divisorList
    


