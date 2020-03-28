#answer
a=int(input()) 
b=0 
i=0 
c=[] 
for i in range(2,200): 
    b=0 
    for j in range(2,i): 
        if i%j==0: 
            b=b+1 
            if b==a: 
                c.append(i) 
                break 
print(c[0])

********************************************************************************************
#queestion
Write a program to find the first number that has >= 'n' factors. Excluding 1 and that number

Input Format

Input contains n

Constraints

n - will be in the range 2 to 200.

Output Format

print the value

Sample Input 0

3

Sample Output 0

12

