#!/usr/bin/env python
# coding: utf-8

# 1. Write a function that counts how many concentric layers a rug.
# Examples
# count_layers([
# &quot;AAAA&quot;,
# &quot;ABBA&quot;,
# &quot;AAAA&quot;
# ]) ➞ 2
# count_layers([
# &quot;AAAAAAAAA&quot;,
# &quot;ABBBBBBBA&quot;,
# &quot;ABBAAABBA&quot;,
# &quot;ABBBBBBBA&quot;,
# &quot;AAAAAAAAA&quot;
# ]) ➞ 3
# count_layers([
# &quot;AAAAAAAAAAA&quot;,
# &quot;AABBBBBBBAA&quot;,
# &quot;AABCCCCCBAA&quot;,
# &quot;AABCAAACBAA&quot;,
# &quot;AABCADACBAA&quot;,
# &quot;AABCAAACBAA&quot;,
# &quot;AABCCCCCBAA&quot;,
# &quot;AABBBBBBBAA&quot;,
# &quot;AAAAAAAAAAA&quot;
# ]) ➞ 5
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def count_layers(in_list):
    out_list = []
    for ele in in_list:
        if ele not in out_list:
            out_list.append(ele)
    print(f'count_layers({in_list}) ➞ {len(out_list)}')

count_layers(["AAAA","ABBA","AAAA"])
count_layers(["AAAAAAAAA","ABBBBBBBA","ABBAAABBA","ABBBBBBBA","AAAAAAAAA"])
count_layers(["AAAAAAAAAAA","AABBBBBBBAA","AABCCCCCBAA","AABCAAACBAA","AABCADACBAA","AABCAAACBAA","AABCCCCCBAA","AABBBBBBBAA","AAAAAAAAAAA"])


# 2. There are many different styles of music and many albums exhibit multiple
# styles. Create a function that takes a list of musical styles from albums and
# returns how many styles are unique.
# Examples
# unique_styles([
# &quot;Dub,Dancehall&quot;,
# &quot;Industrial,Heavy Metal&quot;,
# &quot;Techno,Dubstep&quot;,
# &quot;Synth-pop,Euro-Disco&quot;,
# &quot;Industrial,Techno,Minimal&quot;
# ]) ➞ 9
# unique_styles([
# 
# &quot;Soul&quot;,
# &quot;House,Folk&quot;,
# &quot;Trance,Downtempo,Big Beat,House&quot;,
# &quot;Deep House&quot;,
# &quot;Soul&quot;
# ]) ➞ 7
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def unique_styles(in_list):
    out_list = []
    for ele in in_list:
        for sub_ele in ele.split(','):
            out_list.append(sub_ele)
    print(f'unique_styles({in_list}) ➞ {len(set(out_list))}')
                
unique_styles(["Dub,Dancehall","Industrial,Heavy Metal","Techno,Dubstep","Synth-pop,Euro-Disco","Industrial,Techno,Minimal"]) 
unique_styles(["Soul","House,Folk","Trance,Downtempo,Big Beat,House","Deep House","Soul"])


# 3. Create a function that finds a target number in a list of prime numbers.
# Implement a binary search algorithm in your function. The target number will
# be from 2 through 97. If the target is prime then return &quot;yes&quot; else return &quot;no&quot;.
# Examples
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
# 71, 73, 79, 83, 89, 97]
# 
# is_prime(primes, 3) ➞ &quot;yes&quot;
# is_prime(primes, 4) ➞ &quot;no&quot;
# is_prime(primes, 67) ➞ &quot;yes&quot;
# is_prime(primes, 36) ➞ &quot;no&quot;
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def is_prime(in_list,in_num):
    output = 'No'
    start_point = 0
    end_point = len(in_list) - 1
    mid_point = 0
    while start_point <= end_point:
        mid_point = (end_point+start_point)//2
        if in_list[mid_point] < in_num:
            start_point = mid_point + 1
        elif in_list[mid_point] > in_num:
            end_point = mid_point - 1
        else:
            output = 'Yes'
            break
    print(f'is_prime({in_num}) ➞ {output}')

is_prime(primes, 3)
is_prime(primes, 4)
is_prime(primes, 67)
is_prime(primes, 36)


# 4. Create a function that takes in n, a, b and returns the number of positive
# values raised to the nth power that lie in the range [a, b], inclusive.
# Examples
# power_ranger(2, 49, 65) ➞ 2
# # 2 squares (n^2) lie between 49 and 65, 49 (7^2) and 64 (8^2)
# power_ranger(3, 1, 27) ➞ 3
# # 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)
# power_ranger(10, 1, 5) ➞ 1
# # 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)
# power_ranger(5, 31, 33) ➞ 1
# power_ranger(4, 250, 1300) ➞ 3
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


import math
def power_ranger(in_base,in_min,in_max):
    output = []
    for ele in range(in_min,in_max+1):
        root = round(math.exp(math.log(ele)/in_base),1)
        if str(root).split(".")[1] == '0':
            output.append(int(root))
    print(f'power_ranger{in_base,in_min,in_max} ➞ {len(set(output))}')

power_ranger(2, 49, 65)
power_ranger(3, 1, 27)
power_ranger(10, 1, 5)
power_ranger(5, 31, 33)
power_ranger(4, 250, 1300)


# 5. Given a number, return the difference between the maximum and minimum
# numbers that can be formed when the digits are rearranged.
# Examples
# rearranged_difference(972882) ➞ 760833
# # 988722 - 227889 = 760833
# rearranged_difference(3320707) ➞ 7709823
# # 7733200 - 23377 = 7709823
# rearranged_difference(90010) ➞ 90981
# # 91000 - 19 = 90981.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def rearranged_difference(in_num):
    split_num = []
    for ele in str(in_num):
        split_num.append(ele)
    min_num = int(''.join(sorted(split_num))) 
    max_num = int(''.join(sorted(split_num, reverse=True)))
    print(f'rearranged_difference({in_num}) ➞ {max_num} - {min_num} ➞ {max_num-min_num}')
    
rearranged_difference(972882)    
rearranged_difference(3320707)
rearranged_difference(90010)

