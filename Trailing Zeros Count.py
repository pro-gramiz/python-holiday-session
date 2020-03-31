#question
Given a number N, find out the number of trailing zeros in the factorial of the given number N

Input Format

One integer input

Constraints

!<=N<=10^18

Output Format

One integer output denoting the number of zeros in the factorial of the given number N
****************************************************************************************************************
#answer
def find_trailing_zeros(num):
    sum = 0
    i = 1
    while(True) :
        quotient = num // (5 ** i)
        if(quotient == 0) :
            break
        sum += quotient
        i += 1

    return(sum)

n =int(input())
print(find_trailing_zeros(n))
