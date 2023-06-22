# Character's alternative
string = "I am happy to learn Python"
string_new = ""

# use loop to access and manipulate each character in the string
for char in range(len(string)):
    if char % 2 == 0:  # even
        string_new += string[char].upper() # concatenate char
    else:              # odd
        string_new += string[char].lower() # concatenate char
  
print(string_new)
         
# Word's alternative
string = "I am happy to learn Python"
string_list = string.split() # convert to a list to access the words count
string_list_new = []

# use loop to access and manipulate each word in the string_list
for i in range(len(string_list)):
    if i % 2 == 1:   # odd
        string_list_new.append(string_list[i].upper()) # add words to the new string_list
    else:            # even
        string_list_new.append(string_list[i].lower()) # add words to the new string_list
    
string_new = " ".join(string_list_new) # join words from list to create one string
print(string_new)



