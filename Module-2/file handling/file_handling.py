#Opening, Creating , Reading, Writing and Deleting files in Python
# There are two file handling functions in Python: open() and with open().

#Open - Reading, writing and creating files in python.
#it accepts twon arguments. Open(<file_name> <File_location>, <mode>) mode in this case is creating, reading or writing to file.
# mode sets. R for reacding in text formatt while rb is for reading in binary format. r+ is for reading and writing.
#w  is for writing. w will orverwrite any existing file with the same name. wb is for writing in binary format.
#a opens file for appending. it will create the file if it doesnt exit. ab is for appending in binary format.

#Close - is for closing the file. it doesnt take any arguments. 

# if you dont want to manually close the file, you can use with open() function.

# One way.
file = open('testfile.txt', mode = 'r')  #opens file in read mode
first_line = file.readline() #reads first line of the file
print(first_line)
file.close()

#Another way using with open() function
with open('testfile.txt', 'r') as file:
    data = file.readline()
    print(data)


# Creating files- We can create files using the open function with 'w' or 'a' mode.
try:
    with open('new_file.txt', 'w') as file: # this creates a new file since new_file doesnt exist yet.
        file.write("adding some text to my new file.\n") #this adds text to the new file.
        file.write("adding another line to my new file.\n") #this adds another line to the new file.


#i can simply add multiple lines to the files using the writelines method, and passing a list of strings to it.
        list_of_lines = ["this is a new linee", "this is another new line", "yet another new line"]
        file.writelines("\n".join(list_of_lines))
except FileNotFoundError as e:
    print("File not found: ", e)

#mode w overwrites content in any existing file with the same name. so basically if file already exists, it replaces all its content.
# otherwise if file doenst exist, it just writes in a new file

#if you do not want to overwrite the content of the exixting file but add to it instead, we can use mode "a" for appending
file = open('testfile.txt', 'a') as file:
    file.write("\nThis line is added to the existing file.")




#read() returns the entire content of a file. we can also specify the number of characters to read by passing an integer value to it.
# like this: file.read(20)
#readline() returns a single line from the file as a string. we can also pass in an integer to specify the number of characters to read from that file
#readlines() returns the entire content of a file as a list of string. each line in the file becomes an item in the list.
