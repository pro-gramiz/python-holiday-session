#question
In english alphabets there are two types of words, vowels and consonents.You are writing a program to reverse a given string, but the vowels are stubborn to move away from their position. So given a string where the vowels are stubborn, print what will be word if the entire word is reversed except for the vowels.

Input Format

One string input

Constraints

3<=String length<=10^5

Output Format

Rversed string output

Sample Input 0

missing

Sample Output 0

ngissim
Explanation 0

m + i + ss + i + ng = ng + i + ss + n The string are taken as fragments {m,ss,ng} and the set is reversed and placed between the vowels.

****************************************************************************
#answer
from re import *
s=input()
k='[a,e,i,o,u,A,E,I,O,U]+'
al=split(k,s)[::-1]
v=findall(k,s)
res=al[0]
for i in range(1,len(al)):
    res+=(v[i-1]+al[i])
print(res)
