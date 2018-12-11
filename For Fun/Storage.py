
file = open('File.txt', 'w')
file.write("My dog is amazing")
file.close()

file = open('File.txt', 'r')
file.read()
print(file)
file.close()