#ans
a=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in l:
    if i<0:
        l1.append(i)
    elif i==0:
        l2.append(i)
    else:
        l3.append(i)
s1=l1+l2+l3
print(*s1)



#que
Given an array that has positive numbers and negative numbers and zero in it. You need to separate the negative numbers and positive numbers in such a way that negative numbers lies to left of zero and positive numbers to the right and the original order of elements should be maintained.

Input Format

Each line contains the array size & values

Constraints

1 ≤ array_size ≤ 10000

Output Format

print the altered array

Sample Input 0

6
95 -254 0 12 7 -22
Sample Output 0

-254 -22 0 95 12 7
