#!/usr/bin/python
f = open("data.txt", "r")

#whole file in a variable
#data = f.read()



#iterate through the file by reaeding one line at a time
#useful for log files
for line in f:
    
    print(line.upper())

#close the file
f.close()

myData = "I'm sample data to be written to a file"

#open file in append mode
f = open("data.txt", "a")

#write data into the file
f.write(myData)


