'''
Created on Jan 23, 2017

@author: 19augusthummert
'''
file = open("data.txt", "w")
file.write("Sample file writing\n")
file.write("This is line 2\n")
file.close()

text_lines = {
    "Boillie is pretty cool\n"
    "Her phone was taken away\n"
    "She plays volleyball\n"
    "Shes pretty good at that!!\n"
    }
file = open("data.txt", "w")
file.writelines(text_lines)
file.close()