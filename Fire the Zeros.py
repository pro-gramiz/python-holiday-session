#question
Given a number N, remove all the zeros from the binary representation of the number and convert the remaining number to integer.

Input Format

One integer value N

Constraints

1<=N<=10^18

Output Format

One integer output

Sample Input 0

7911852283209194

Sample Output 0

268435455

*****************************************************************************************
#answer
a=int(input())
b=bin(a)
c=b[2:]
l=[]
m=[]
for i in c:
    l.append(i)
for k in l:
    if(k=="1"):
        m.append(k)
y="".join(m)
p=int(y,2)
print(p)
