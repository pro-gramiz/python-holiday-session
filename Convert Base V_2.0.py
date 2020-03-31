#question
Given a number of with base A to base B, where A is the smallest number which has two factors, and B is a number which is second highest factor of a number which when added with the second ever number which has odd number of factors, they add up to form a number which is the sisth ever number to have odd number of factors.

Input Format

One integer input N

Constraints

1<=N<=10^18

Output Format

The converted base element output

Sample Input 0

11000100000111110

Sample Output 0

1883e

*******************************************************************************************
#answer
a=input()
b=int(a,2)
c=hex(b)[2:]
print(c)
