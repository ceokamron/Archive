"""
Text Type:	                              /:str
Numeric Types:	                           /:int, float, complex
Sequence Types:	                        /:list, tuple, range
Mapping Type:	                           /:dict
Set Types:	                              /:set, frozenset
Boolean Type:	                           /:bool
Binary Types:	                           /:bytes, bytearray, memoryview
None Type:	                              /:NoneType

"""

"""

x = "Hello World"	                                 ::    str	
x = 20	                                          ::    int	
x = 20.5	                                          ::    float	
x = 1j	                                          ::    complex	
x = ["apple", "banana", "cherry"]	               ::    list	
x = ("apple", "banana", "cherry")	               ::    tuple	
x = range(6)	                                    ::    range	
x = {"name" : "John", "age" : 36}	               ::    dict	
x = {"apple", "banana", "cherry"}	               ::    set	
x = frozenset({"apple", "banana", "cherry"})	      ::    frozenset	
x = True	                                          ::    bool	
x = b"Hello"	                                    ::    bytes	
x = bytearray(5)	                                 ::    bytearray	
x = memoryview(bytes(5))	                        ::    memoryview	
x = None	                                          ::    NoneType

"""

# ---> int() - constructs an integer number from an integer literal, 
# a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# ---> float() - constructs a float number from an integer literal, 
# a float literal or a string literal (providing the string represents a float or an integer)
# ---> str() - constructs a string from a wide variety of data types, 
# including strings, integer literals and float literals

   # -> x = 1    # int              ""<- x = 1j ->
   # -> y = 2.8  # float            ""<-- Print(type(x)) -->
   # -> z = 1j   # complex

"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
   
"""

# <---------------- String ------------------------>

#  Get the character at position 1 (remember that the first character has the position 0):
""""

a = "Hello, World!"
print(a[1])

"""

# Loop through the letters in the word "banana":

# for x in "banana":
#   print(x)

# The len() function returns the length of a string:

# a = "Hello, World!"
# print(len(a))

# Check if "free" is present in the following text:

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# Get the characters from position 2 to position 5 (not included):

# b = "Hello, World!"
# print(b[2:5])

# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

# b = "Hello, World!"
# print(b[-5:-2])

#                                                      """  <--   String   -->  """

# The strip() method removes any whitespace from the beginning or the end:

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string:

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# Example
# Use the format() method to insert numbers into strings:

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

   # quantity = 3
   # itemno = 567
   # price = 49.95
   # myorder = "I want {} pieces of item {} for {} dollars."
   # print(myorder.format(quantity, itemno, price))
   
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))


   # Bu qo'shtirnoq ichida qo'shtirnoq ishlatmoqchi bo'lsak shu formuladan foydalanadi
   # txt = "We are the so-called \"Vikings\" from the north."

                                    # """

                                    # \'	         Single Quote	
                                    # \\	         Backslash	
                                    # \n	         New Line	
                                    # \r	         Carriage Return	
                                    # \t	         Tab	
                                    # \b	         Backspace	
                                    # \f	         Form Feed	
                                    # \ooo	      Octal value	
                                    # \xhh	      Hex value	   

                                    # """

"""
                                                         # ------ !!! STRING METHODS !!! ------------  #

# 
# Python has a set of built-in methods that you can use on strings.

# Note: All string methods return new values. They do not change the original string.

# Method	Description
# capitalize()	                             ::                    Converts the first character to upper case
# casefold()	                             ::                    Converts string into lower case
# center()	                                ::                    Returns a centered string
# count()	                                ::                    Returns the number of times a specified value occurs in a string
# encode()	                                ::                    Returns an encoded version of the string
# endswith()	                             ::                    Returns true if the string ends with the specified value
# expandtabs()	                             ::                    Sets the tab size of the string
# find()	                                   ::                    Searches the string for a specified value and returns the position of where it was found
# format()	                                ::                    Formats specified values in a string
# format_map()	                             ::                    Formats specified values in a string
# index()	                                ::                    Searches the string for a specified value and returns the position of where it was found
# isalnum()	                                ::                    Returns True if all characters in the string are alphanumeric
# isalpha()	                                ::                    Returns True if all characters in the string are in the alphabet
# isdecimal()	                             ::                    Returns True if all characters in the string are decimals
# isdigit()	                                ::                    Returns True if all characters in the string are digits
# isidentifier()	                          ::                    Returns True if the string is an identifier
# islower()	                                ::                    Returns True if all characters in the string are lower case
# isnumeric()	                             ::                    Returns True if all characters in the string are numeric
# isprintable()	                          ::                    Returns True if all characters in the string are printable
# isspace()	                                ::                    Returns True if all characters in the string are whitespaces
# istitle()	                                ::                    Returns True if the string follows the rules of a title
# isupper()                                 ::            	      Returns True if all characters in the string are upper case
# join()                                    ::    	               Joins the elements of an iterable to the end of the string
# ljust()                                   :: 	                  Returns a left justified version of the string
# lower()                                   ::                    Converts a string into lower case
# strip()	                                ::                    Returns a left trim version of the string
# maketrans()	                             ::                    Returns a translation table to be used in translations
# partition()                               ::             	      Returns a tuple where the string is parted into three parts
# replace()	                                ::                    Returns a string where a specified value is replaced with a specified value
# rfind()	                                ::                    Searches the string for a specified value and returns the last position of where it was found
# rindex()	                                ::                    Searches the string for a specified value and returns the last position of where it was found
# rjust()	                                ::                    Returns a right justified version of the string
# rpartition()	                             ::                    Returns a tuple where the string is parted into three parts
# rsplit()	                                ::                    Splits the string at the specified separator, and returns a list
# rstrip()	                                ::                    Returns a right trim version of the string
# split()	                                ::                    Splits the string at the specified separator, and returns a list
# splitlines()	                             ::                    Splits the string at line breaks and returns a list
# startswith()	                             ::                    Returns true if the string starts with the specified value
# strip()	                                ::                    Returns a trimmed version of the string
# swapcase()	                             ::                    Swaps cases, lower case becomes upper case and vice versa
# title()	                                ::                    Converts the first character of each word to upper case
# translate()	                             ::                    Returns a translated string
# upper()	                                ::                    Converts a string into upper case
# zfill()	                                ::                    Fills the string with a specified number of 0 values at the beginning

"""