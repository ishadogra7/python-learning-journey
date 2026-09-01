print('hello \'s isha') # \   escape charrecter -->normally be interpreted as the end of the string.
message =  """isha\'s  
mmutilnne tex
           """
print(message)
# when  i access a  particular char from a string 
print(message[0])  # prints the first character of the string
print(message[10]) # nothing write 


# when i find a range of char from a string
print(message[0:5])  # prints characters from index 0 to 4 ..... doesnot include the char 5


# upper case and lower case
print(message.upper())
print(message.lower())


# dir and help function in pyhton

print(dir(message.upper())) # all the available methods and attributes

print(help(message.upper()))  # explain what those what do and how to use them  in a function
# count char in a string
print(message.count('i'))  
  
# find char in a string
print(message.find('f'))  

# replace char in a string
print(message.replace('i', 'I'))  


# concatenate string

message1 = 'Hello,' 
message2 = ' Isha Dogra....'
message3 = ' what are you doing........I think you are fine'
 
print(message1 + message2 + message3 + '\n' ) # this is typical  way  to concatenate string


# use of format method ttoconactenate a string 
message  = ' {} {} ,{} ...... Welcome to this python tutorials !'. format( message1 , message2 , message3)

### or 

message = f'{message1} ....{message2}....... {message3}.....welcome to this pyhton tutorials!'
print(message + '\n')


