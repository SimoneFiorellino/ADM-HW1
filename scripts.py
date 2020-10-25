#Problem 1

#--->Introduction
#Say "Hello, World!" With Pyhton

print("Hello, World!")

#Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    a = int(input().strip())
    if (a % 2) != 0 or a in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
        
        
#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    
#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
    
    
#Loops

def print_num(n):
    for i in range(n):
        print(i*i)

if __name__ == '__main__':
    n = int(input())
    print_num(n)
    
#Write a function


def is_leap(year):
    leap = False
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
    
    
#Print Function

def print_number(n):
    num=''
    for i in range(1,n+1):
        num = num + f'{i}'
    print(num)

if __name__ == '__main__':
    n = int(input())
    print_number(n)


#--->Data Type

#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    my_list = []

    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if(i+j+k!=n):
                    my_list.append([i,j,k])
    print(my_list)

#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    my_map = map(int, input().split())

    print(sorted(set(list(my_map)))[-2])

#Nested Lists

if __name__ == '__main__':
    len=0
    my_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([score, name])
        len+=1

    my_list.sort()

    first = 1
    second = 1

    #how many players are first
    for i in range(0,len):
        if my_list[i][0]==my_list[i+1][0]:
            first+=1
        else:
            break

    #how may players are sec
    for j in range(first,len-1):
        if my_list[j][0]==my_list[j+1][0]:
            second+=1
        else:
            break

    my_final_list = []
    for i in range(first,first+second):
        my_final_list.append(my_list[i][1])

    my_final_list.sort()
    for i in my_final_list:
      print(i)
      
#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('%.2f'%((student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2])/3))


#Lists

if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for i in range(N):
        cmd = input()
        if cmd[0:2]=="in":
            cmd,n1,n2=cmd.split()
            my_list.insert(int(n1),int(n2))
        elif cmd[0:3]=="rem":
            cmd,n1=cmd.split()
            my_list.remove(int(n1))
        elif cmd[0:2]=="ap":
            cmd,n1=cmd.split()
            my_list.append(int(n1))
        elif cmd[0:2]=="so":
            my_list.sort()
        elif cmd[0:2]=="pr":
            print(my_list)
        elif cmd[0:2]=="po":
            my_list.pop()
        else:
            my_list.reverse()

#Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    my_tupla = tuple(integer_list)
    print(hash(my_tupla))
    
#--->Strings

#sWAP cASE

def swap_case(s):
    swap = ''
    for i in s:
        if i.isupper():
            swap+=i.lower()
        else:
            swap+=i.upper()
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join

def split_and_join(line):
    # write your code here
    line = line.split()
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?

def print_full_name(a, b):
    return print(f'Hello {a} {b}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations

def mutate_string(string, position, character):
    string = string[:position] + f'{character}' + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Find a string

def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)):
        if sub_string==string[i:i+(len(sub_string))]:
            count+=1   
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#String Validators

def is_function(a):
    alnum=False
    alpha=False
    digit=False
    lower= False
    upper= False
    for i in a:
        if i.isalnum():
            alnum=True
        if i.isalpha():
            alpha=True
        if i.isdigit():
            digit=True
        if i.islower():
            lower=True
        if i.isupper():
            upper=True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

if __name__ == '__main__':
    s = input()

    is_function(s)


#Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap

import textwrap

def wrap(string, max_width):
    answer=""
    size=len(string)-max_width
    count=0
    for i in range(0,size):
        if i%max_width==0:
          answer += string[i:i+max_width]+"\n"
          count+=1
    answer += string[max_width*count:]
    return answer

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int,input().split())

x=".|."
y="-"
z="WELCOME"

result=""
cap=int((n-1)/2)+1
cap_=int((m-7)/2)
count = 0
for i in range(1,cap):
    for j in range(0,int((m-((i+count)*3))/2)):
        result+=y
    for j in range(1,i*2):
        result+=x
    for j in range(0,int((m-((i+count)*3))/2)):
        result+=y
    result+="\n"
    count+=1

count=0
for j in range(0,cap_):
    result+= y
result+=z
for j in range(0,cap_):
    result+= y
supp=""

for i in range(1,cap):
    for j in range(0,int((m-((i+count)*3))/2)):
        supp=y+supp
    for j in range(1,i*2):
        supp=x+supp
    for j in range(0,int((m-((i+count)*3))/2)):
        supp=y+supp
    supp="\n"+supp
    count+=1
result+= supp
print(result)

#String Formatting

def print_formatted(n):
    not_final = []

    for i in range(1, n+1):
        d = str(i)
        o = str(oct(i)[2:])
        h = str(hex(i)[2:]).upper()
        b = str(bin(i)[2:])

        not_final.append([d, o, h, b])

    count = len(not_final[-1][3])

    my_final=''
    count_02=True
    for i in not_final:
        count_02=True
        for j in i:
            if count_02==True:
                my_final += j.rjust(count)
            else:
                my_final += j.rjust(count+1)

            count_02=False
        my_final+="\n"

    print(my_final)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Alphabet Rangoli

def print_rangoli(n):
    #notation found on internet (code with counts was too long)
    my_alfa = 'abcdefghijklmnopqrstuvwxyz'[0:n]
    #'-'.join(my_alfa[i:n])[::-1] --> "-" & myalfa left
    #'-'.join(my_alfa[i:n])[1:] --> "-" & myalfa right
    #(L+R).center(4*n-3, '-') --> "frame"
    row = [(('-'.join(my_alfa[i:n])[::-1]+'-'.join(my_alfa[i:n])[1:])).center(4*n-3, '-')for i in range(n)]
    #row[::-1] first n rows
    #row[1:] n - 1 rows
    print(*(row[::-1]+row[1:]), sep="\n")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s=s.split(" ")
    result=""
    for i in s:
        result+= i.capitalize() +" "
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

    
#The Minion Game

def minion_game(string):
    Stuart=0
    Kevin=0
    count=0
    lenght=len(string)
    for i in string:
        if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
            Kevin+=lenght-count
        else:
            Stuart+=lenght-count
        count+=1

    if Kevin>Stuart:
        print(f"Kevin {Kevin}")
    elif Kevin<Stuart:
        print(f"Stuart {Stuart}")
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)

#Merge the Tools!
 
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(dict.fromkeys(string[i:i+k])))
        #print("".join(set(string[i:i+div])))   #ordered version
 
 if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
 
 #--->Sets
 
 
 #Introduction to Sets
 
 def average(array):
    res=0
    for i in set(array):
        res+=i
    return res/ len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
 
 #No Idea!
 
n = input()
array = input().split()
A = set(input().split())
B = set(input().split())

happi=0
for i in array:
    if i in A:
        happi+=1
    if i in B:
        happi-=1
print(happi)
 
 #Symmetric Difference
 
 _ = input()
my_set_01 = set(input().split())
_ = input()
my_set_02 = set(input().split())

result = sorted(my_set_01.symmetric_difference(my_set_02),key=int)
print("\n".join([i for i in result]))

#Set .add()

n = int(input())
print(len(set([str(input()) for i in range(n)])))

#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))

num_command = int(input())

for i in range(num_command):
    command = input()
    type=command[0:1]
    if type=="p":
        s.pop()
    elif type=="r":
        #print(command[int(command.find(" ")+1):])
        s.remove(int(command[int(command.find(" ")+1):]))
    else:
        #print(command[int(command.find(" ")+1):])
        s.discard(int(command[int(command.find(" ")+1):]))

print(sum(s))

#Set .union() Operation

_ = input()
my_set_01 = set(input().split())
_ = input()
my_set_02 = set(input().split())

print(len(set(my_set_01.union(my_set_02))))

#Set .intersection() Operation

_ = input()
my_set_01 = set(input().split())
_ = input()
my_set_02 = set(input().split())

print(len(set(my_set_01.intersection(my_set_02))))

#Set .difference() Operation

_ = input()
my_set_01 = set(input().split())
_ = input()
my_set_02 = set(input().split())

print(len(set(my_set_01.difference(my_set_02))))

#Set .symmetric_difference() Operation

_ = input()
my_set_01 = set(input().split())
_ = input()
my_set_02 = set(input().split())

print(len(set(my_set_01.symmetric_difference(my_set_02))))

#Set Mutations

_ = input()
my_set_01 = set(input().split())
num_operation = int(input())

for i in range(num_operation):
    command=input()
    my_set_02=set(input().split())
    type=command[0:1]
    if type=="i":
        my_set_01.intersection_update(my_set_02)
    elif type=="u":
        my_set_01.update(my_set_02)
    elif type=="s":
        my_set_01.symmetric_difference_update(my_set_02)
    else:
        my_set_01.difference_update(my_set_02)

sum=0
for i in my_set_01:
    sum+=int(i)

print(sum)

#The Captain's Room

num = int(input())
my_list = list(map(int, input().split()))
my_list_set=set(my_list)
print(int(((sum(num*i for i in my_list_set))-sum(my_list))/(num-1)))
"""
for i in set(my_list):
    if my_list.count(i)==1:
        print(i)
        break
"""

#Check Subset

num = int(input())

for i in range(num):
    _ = input()
    my_set_01=set(input().split())
    _ = input()
    my_set_02=set(input().split())
    print("True" if my_set_01.intersection(my_set_02)==my_set_01 else "False")

#Check Strict Superset

my_set=set(input().split())
num=int(input())
result=True
for i in range(num):
    my_set_01=set(input().split())
    if my_set.intersection(my_set_01)!=my_set_01:
        result=False

print(result)



#--->Collections

#collections.Counter()

from collections import Counter

_ = input()
my_list= map(int, input().split())
my_list=Counter(my_list)
num = int(input())
money_earned=0
for i in range(num):
    item_size, item_price = map(int, input().split())
    if my_list[item_size]:  #is the item in my_list?
        my_list[item_size]-=1   #remove the item purched
        money_earned+=item_price    #add to the total the money earned 

print(money_earned)

#DefaultDict Tutorial

from collections import defaultdict
d = defaultdict(list)

#n,m inputs
n, m = input().split()

#fill d with position of key
for i in range(int(n)):
    d[input()].append(str(i+1))

#print the items with input of group B
for i in range(int(m)):
    print(" ".join(d[input()]) or -1) 


#Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
dunno = namedtuple('Product', input())
average=0
for i in range(n):  
    field_01, field_02, field_03, field_04 = (input().split())
    xyz=dunno(field_01, field_02, field_03, field_04)
    average+=int(xyz.MARKS)
print('%.2f' % (average/n))

#Collections.OrderedDict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ordinary_dictionary = {}
num = int(input())
my_list=list()

#crate ordinary_dictionary
for i in range(num):
    my_list=input().split()
    if (" ".join(my_list[:-1])) in ordinary_dictionary:
        ordinary_dictionary[" ".join(my_list[:-1])]+=int(my_list[-1])
    else:
        ordinary_dictionary[" ".join(my_list[:-1])] = int(my_list[-1])

#print
for i in ordinary_dictionary:
    print(i+" "+str(ordinary_dictionary[i]))

#Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
num = int(input())
ordinary_dictionary = {}
word=""
for i in range(num):
    word=input()
    if word in ordinary_dictionary:
        ordinary_dictionary[word]+=1
    else:
        ordinary_dictionary[word]=1

#print
count=0
result=""
for i in ordinary_dictionary:
    result+=str(ordinary_dictionary[i])+" "
    count+=1

print(count)
print(result)

#Collections.deque()

from collections import deque
d = deque()
num = int(input())
cmd=""
for i in range(num):
    cmd=input()

    if cmd=="popleft":
        d.popleft()
    elif cmd=="pop":
        d.pop()
    elif cmd[0:1]=="a":
        cmd,n=cmd.split()
        if cmd=="append":
            d.append(n)
        else:
            d.appendleft(n)

print(" ".join(d))

#Company Logo

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict


if __name__ == '__main__':
    ordinary_dictionary = {}
    s = input()
    for i in set(s):
        ordinary_dictionary[str(i)]=s.count(i)

    ordinary_dictionary=OrderedDict(sorted(ordinary_dictionary.items(), key=lambda t: (-t[1], t[0])))
    count=0
    for i in ordinary_dictionary:
        if count<3:
            print(f'{i} {ordinary_dictionary[i]}')
            count+=1

#Piling Up!

from collections import deque

num = int(input())

for i in range(num):  
    n = input()
    my_deque = deque(map(int, input().split()))
    
    for i in sorted(my_deque, reverse=True):
        l=my_deque[0]
        r=my_deque[-1]
        if r == i: 
            my_deque.pop()  # using pop() to delete element from right end 
        elif l == i: 
            my_deque.popleft()  # using popleft() to delete element from left end 

    if len(my_deque)==0:
        print('Yes')
    else:
        print('No')

#-->Date and Time

#Calendar Module

import calendar

mm, dd, yyyy = map(int, input().split())

#calendar.weekday(year, month, day)
#Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).
day=calendar.weekday(yyyy, mm, dd)

print(calendar.day_name[day].upper())   #day_name An array that represents the days of the week in the current locale.

#Time Delta

import math
import os
import random
import re
import sys
import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    s1_ = '%a %d %b %Y %H:%M:%S %z'
    s1=dt.datetime.strptime(t1, s1_)
    s2=dt.datetime.strptime(t2, s1_)
    count=abs((s1-s2).total_seconds())
    """
    dif=((int(t1[-4:]))-(int(t2[-4:])))
    count=0
    count+=((dif)%100)*60
    count+=((dif)%1000-(dif)%100)*36
    """
    return str(count)[:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
    
#--->Errors and Exceptions

#Exceptions

num = int(input())

for i in range(num):
    try:
        n,m=map(int, input().split())
    except ValueError as e:
        print("Error Code:", e)
        continue
    
    try:
        print(n//m)
    except ZeroDivisionError as e:
        print("Error Code:",e)
        
        
        
#--->Built-ins

#Zipped!

def average(my_list, n):

    for i in my_list:
        summ=0
        for j in i:
            summ+=float(j)
        print(summ/n)

col, row = map(int, input().split())
my_list=list()
supp=list()
for i in range(row):
    supp=input().split()
    my_list.append(supp)

my_zip=zip(*my_list)

#method for average calculation
average(list(my_zip),row)

#Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    # Using sorted and lambda 
    arr = sorted(arr, key=lambda x: x[k])

    #print arr
    res=""
    for i in arr:
        for j in i:
            res+=str(j)+" "
        res+="\n"
    print(res)

#ginortS

my_string = input()

lower=""
upper=""
digit=""

demo=[[],[],[[],[]]]

for i in my_string:
    if i.isdigit():
        if int(i)%2==0:
            demo[2][1].append(i)
        else:
            demo[2][0].append(i)
    elif i.isupper():
        demo[1].append(i)
    else:
        demo[0].append(i)

res=""
for i in sorted(demo[0]):
    res+=i
for i in sorted(demo[1]):
    res+=i
for i in demo[2]:
    for j in sorted(i):
        res+=j

print(res) 

#--->Python Functionals

#Map and Lambda Function

cube = lambda x: x*x*x

def fibonacci(n):
    my_fibo=list()
    for i in range(n):
        if i<2:
            my_fibo.append(i) 
        else:
            my_fibo.append(my_fibo[i-1]+my_fibo[i-2])
        
    return my_fibo

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#--->Regex and Parsing challenges

#Detect Floating Point Number

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.w3schools.com/python/python_regex.asp#search
import re
"""
for _ in range(int(input())):
    #x = re.search("\s", txt)
    x=re.search("^[+-]?[0-9]*.[0-9]+$", input())
    print(bool(x))

"""
for _ in range(int(input())):
    try:
        i=input()
        j=float(i) #but if input() is int like 0 should be false
        x=re.search("^[+-]?[0-9]*.[0-9]+$", i)
        print(bool(x))
    except:
        print("False")

#Re.split()

regex_pattern = r"\b[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Group(), Groups() & Groupdict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

m = input()
res = re.search(r"([a-zA-Z0-9])\1", m)  
#\number
#Matches the contents of the group of the same number.
print(res.group(1) if res else -1)  

#per stampare tutto il gruppo es. 33333:
#res = re.search(r"([a-zA-Z0-9])\1+", m) 
#print(res.group(0) if res else -1) 

#Re.findall() & Re.finditer()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

demo = input()
m = re.split(r"[^aeiouAEIOU]", demo)
#\number
#Matches the contents of the group of the same number.
my_match=True
for i in range(len(m)):
    if len(m[i])>1 and i!=(len(m)-1) and i!=(0):
        print(m[i])
        my_match=False

if my_match:
    print(-1)

#Re.start() & Re.end()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

demo=input()
pattern=input()

no_match=True
for i in range(len(demo)-(len(pattern)-1)):
    if demo[i:i+len(pattern)]==pattern:
        print(f'({i}, {i+len(pattern)-1})')
        no_match=False

if no_match:
    print((-1,-1))

#Regex Substitution

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def change(match):
    if match.group(0)=='&&':
        return 'and'
    else:
        return 'or'


for _ in range(int(input())):
    my_string=input()
    print(re.sub(r"(?<=[ ])(&&|\|\|)(?=[ ])", change, my_string)) #use of positive lookbehind

#Validating Roman Numerals

regex_pattern = r"^(?=[MDCLXVI])M{,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
import re
print(str(bool(re.match(regex_pattern, input()))))

#Validating phone numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    print("YES" if (re.match(r"(?<=)(?=[789])([0-9]{10})(?=)$", input())) else "NO")

#Validating and Parsing Email Addresses

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

for _ in range(int(input())):
    my_mail = input().split()
    if re.match(r"(^[a-zA-Z][a-zA-Z0-9_.-]{0,})([@])([a-zA-Z]{0,})([.])([a-zA-Z]{0,3}$)", my_mail[1][1:-1]):
        print(f'{my_mail[0]} {my_mail[1]}')

#Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

my_trigger=False
for _ in range(int(input())):
    my_string=input()
    if len(my_string)>6:
        result=re.findall(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}', my_string)
        for i in result:
            print(i)

#HTML Parser - Part 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attribute in attrs:
            print ('->',attribute[0],'>',attribute[1])

    def handle_endtag(self, tag):
        print ("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for attribute in attrs:
            print ('->',attribute[0],'>',attribute[1])

parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())
parser.close()

#HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if '\n' in data: pass
        else:
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
  
 
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attribute in attrs:
            print ('->',attribute[0],'>',attribute[1])

    def handle_startendtag(self, tag, attrs):
        print (tag)
        for attribute in attrs:
            print ('->',attribute[0],'>',attribute[1])


parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())

#Validating UID

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    my_uid = input()
    if re.match(r'^((?=.*\d.*\d.*\d)(?=.*[A-Z].*[A-Z])[a-zA-Z0-9]{10})$', my_uid):
        for i in my_uid:
            if my_uid.count(i)>1:
                print('Invalid')
                break
        else: print('Valid')
    else:
        print('Invalid')

#Validating Credit Card Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    my_input=input()

    if re.match(r'^(?=[456])([0-9]{16})$|^((?=[456])([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4}))$', my_input):
        my_input=re.sub(r'[-]', "", my_input)
        #res=re.match(r'[\d]{,12}([0-9])\1\1\1', my_input)
        if re.match(r'[\d]{,12}([0-9])\1\1\1', my_input):
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')

#Validating Postal Codes

regex_integer_in_range = r"^(?=[1-9])[\d]{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Matrix Script

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
my_string=""
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
        #print(matrix[0])
    for j in range(n):
        #if j!="\n":
        my_string+=matrix[j][i]

print(re.sub(r'(?<=[a-zA-Z])[^a-zA-Z0-9]{1,}(?=[a-zA-Z])', " ",my_string))

#--->XML

#XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree
from html.parser import HTMLParser

def get_attr_number(node):
    count=0
    for i in node.iter():
        count+=len(i.attrib)
    return count


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    
    
    if level==maxdepth:
        maxdepth+=1

    if(len(elem)>0):
        for i in elem:
            depth(i, level+1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#--->Closures and Decorations

#Standardize Mobile Number Using Decorators

import re

def wrapper(f):
    def fun(l):
        #[\d]{10}$
        my_agenda=list()
        for i in l:
            my_agenda.append('+91 '+ i[-10:-5]+' '+ i[-5:])
        f(j for j in my_agenda)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        my_ordered_list=sorted(people, key=lambda x: int(x[2]))
        return (f(j) for j in my_ordered_list)  #"f(i)" notation found from discuss
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#--->Numpy

#Arrays

def arrays(arr):
    return numpy.array(list(reversed(arr)), float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape

import numpy


my_array = input().strip().split(' ')

my_matrix = numpy.array(my_array, int)
print(numpy.reshape(my_matrix, (3,3)))

#Transpose and Flatten

import numpy

my_array=[]
m,n = map(int, (input().split()))

for i in range(m):
    arr = input().strip().split(' ')
    my_array.append(arr)

print(numpy.transpose(numpy.array(my_array,int)))
print(numpy.array(my_array,int).flatten())

#Concatenate

import numpy

my_array=[]
m,n,p = map(int, (input().split()))

for i in range(m+n):
    arr = input().strip().split(' ')
    my_array.append(arr)

print(numpy.array(my_array,int))

#Zeros and Ones

import numpy

my_dim = tuple(map(int, (input().split())))
#print(my_dim)

print(numpy.zeros(my_dim, dtype = numpy.int))
print(numpy.ones(my_dim, dtype = numpy.int))

#Eye and Identity

import numpy

numpy.set_printoptions(sign=' ')

m,n = map(int, (input().split()))
k=0
print((numpy.eye(m, n, k)))

#Array Mathematics

import numpy

m,n = map(int, (input().split()))
my_arr=[]
#A & B
for _ in range(m):
    my_arr.append(input().strip().split(' '))
A = numpy.array(my_arr,int)
my_arr.clear()
for _ in range(m):
    my_arr.append(input().strip().split(' '))
B = numpy.array(my_arr,int)


print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)

#Floor, Ceil and Rint

import numpy
numpy.set_printoptions(sign=' ')

arr = input().strip().split(' ')
my_arr=(numpy.array(arr, float))

print(numpy.floor(my_arr))
print(numpy.ceil(my_arr))
print(numpy.rint(my_arr))

#Sum and Prod

import numpy


my_array=[]
m,n = map(int, (input().split()))

for i in range(m):
    arr = input().strip().split(' ')
    my_array.append(arr)

print(numpy.prod((numpy.sum(numpy.array(my_array,int), axis = 0)), axis=0))

#Min and Max

import numpy

my_array=[]
m,n = map(int, (input().split()))

for i in range(m):
    arr = input().strip().split(' ')
    my_array.append(arr)

print(numpy.max(numpy.min(numpy.array(my_array,int), axis = 1)))

#Mean, Var, and Std

import numpy
numpy.set_printoptions(sign=' ')

my_array=[]
m,n = map(int, (input().split()))

for i in range(m):
    arr = input().strip().split(' ')
    my_array.append(arr)

my_array=numpy.array(my_array,int)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(numpy.around(numpy.std(my_array, axis = None),decimals=12))

#Dot and Cross

import numpy

my_array=[]
m = int(input())

for i in range(m):
    arr = input().strip().split(' ')
    my_array.append(arr)
A=numpy.array(my_array, int)

my_array.clear()
for i in range(m):
    arr = input().strip().split(' ')
    my_array.append(arr)
B=numpy.array(my_array, int)

print(numpy.dot(A, B))

#Inner and Outer

import numpy


A = numpy.array(input().strip().split(' '), int)
B = numpy.array(input().strip().split(' '), int)

print(numpy.inner(A, B))
print(numpy.outer(A, B))

#Polynomials

import numpy

print(numpy.polyval(numpy.array(input().strip().split(' '), float),int(input())))

#Linear Algebra

import numpy

my_array=[]
m = int(input())

for i in range(m):
    arr = input().strip().split(' ')
    my_array.append(arr)

A = numpy.array(my_array, float)

print(round(numpy.linalg.det(A),2))

#Problem 2

#Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):

    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    t1=x1
    t2=x2
    if x1==x2: return "YES"
    elif x1<x2 and v1>v2:
        for i in range(0,10000000):
            t1+=v1
            t2+=v2
            if t1==t2: return 'YES'
            if t1>t2: return 'NO'
    elif x1>x2 and v1<v2:
        for i in range(0,10000000):
            t1+=v1
            t2+=v2
            if t1==t2: return 'YES'
            if t1<t2: return 'NO'
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    liked=2
    shared=0
    cumulative=2
    for i in range(1,n):
        shared=liked*3
        liked=shared//2
        cumulative+=liked
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    my_str=str(n)
    count=0
    for i in range(len(my_str)):
        count+=int(my_str[i:i+1])
    if k!=0: count*=k
    if count>=10: 
        return superDigit(count, 0)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



#Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    datum=0
    j=0
    for i in range(1,n):
        datum=arr[i]
        j=i-1
        result=""
        while j>=0 and arr[j]>datum:
            if arr[j]>datum:
                arr[j+1]=arr[j]
                j-=1
            for i in arr:
                result+=str(i)+" "
            print(result)
            result=""
        arr[j+1]=datum
    result=""
    for i in range(n):
        if arr[i+1]>datum: 
            arr[i]=datum
            for i in arr:
                result+=str(i)+" "
            print(result)
            break
        
            
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)



#Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    datum=0
    j=0
    for i in range(1,n):
        datum=arr[i]
        j=i-1
        result=""
        while j>=0 and arr[j]>datum:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=datum
        for i in arr:
            result+=str(i)+" "
        print(result)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
 
 
 
