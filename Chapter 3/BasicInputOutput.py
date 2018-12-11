'''
Created on Jan 20, 2017

@author: 19augusthummert
'''
welcome = "Fare thee well master"
name = input("Pray tell, what is thy name? ")
print(welcome, name)

title = input("What would you rather be called than master?")
welcome.replace("Master", title)
print(welcome,name,"...Is that better?")


