#question
Given a number N, find the factorial of the gien number and repeatedly add the digits of the factorial till you are left with one digit.

Input Format

One integer input

Constraints

1<=N<=20

Output Format

One digit integer output

Sample Input 0

0

Sample Output 0

1

**************************************************************************
#answer
from math import factorial as f
a=int(input())
b=f(a)
print(b%9)
