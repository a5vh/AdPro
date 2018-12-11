'''
Created on Jan 20, 2017

@author: 19augusthummert
'''
s = input("Enter a number...")

try:
    number = float(s)
except:
    number = 0
    
answer = number * number
print(number, "*", number, "=", answer)