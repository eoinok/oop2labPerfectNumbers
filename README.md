# oop2labPerfectNumbers
This lab exercise has four objectives:
- To get you started using git and github
- To get you started using the Command Line Interface
- To guide you through a Top Down Design solution to a problem
- To get you to correctly translate pseudo-code

The challenge is to find the first four "perfect Numbers" - 
A perfect Number is one for which the sum of all it's divisors adds up to the number itself.
These numbers are rare. The first three are 6, 28, 496

Using a "Top down design" approach we imagine a function that when passed a number,
will return true if the number is perfect and false if it is not

The solution is then to keep a count (in an accumulator varialbe) of the total number of perfect numbers found and
keep trying to find another perfect number until four are found. Each time around the loop we must also increment the testNumber by 1
```
set the totalPFs variable to 0
set the testNumber variable to 1
while the totalPFs variable is less than or equal to 3
    if the testNumber is a perfect
        print the testNumber is a perfect number
        increment the totalPFs variable by 1
    increment the testNumber variable
```
        
Having imagined a function (perfectNumber) that tells us whether a number is perfect or not, the high-level solution is simple.
Now we tackle the problem at a lower level and try to figure out how to create the perfectNumber function. If only we had a function that
gave us back a list of all the divisors of the function - the solution would be easier - so we imagine a function like that.

In the exercise:
# Step 1
Open the file divisors.py and translate the pseudo code to create a function which will return a list of divisors. Before moving on to Step 2, make sure print(divisors(30)) works correctly

# Step 2
Open the file perfectNumber.py and translate the psuedo code to create a function which will return True or False based on whether the number passed is perfect or not. Before moving on to step 3, make sure to uncomment the last line to test if 8128 is a perfect number

# Step 3
Create a program in findFirstFourPNs.py to find the first four perfect numbers, use the high-level pseudo-cod solution outlined at the beginning of this README
