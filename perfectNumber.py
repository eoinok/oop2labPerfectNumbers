#A perfect number is one for which all the divisors of the number add up to the
#number itself. For example the divisors of 28 are 1,2,4,7,14 which added together gives 28
#write a function below called perfectNumber(x) which checks to see if x is a perfect number
from divisors import divisors
#define the function header called perfectNumber expecting one argument
def perfectNumber(number):
    #set a result variable to False by default
    result = False
    #if the sum of all the divisors of the number is equal to the test number
    if (sum(divisors(number))==number):
        #set the result variable to be True
        result = True
    #return the result variable
    return result
