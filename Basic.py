"""         Data Type           """

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType


# that function is showing is type of Data
# x = 5
# print(type(x))


# x = "Hello World"	                    str	
# x = 20	                            int	
# x = 20.5	                            float	
# x = 1j	                            complex	
# x = ["apple", "banana", "cherry"]	    list	
# x = ("apple", "banana", "cherry")	    tuple	
# x = range(6)	                        range	
# x = {"name" : "John", "age" : 36}	    dict	
# x = {"apple", "banana", "cherry"}	    set	
# x = frozenset({"apple", "banana"})	frozenset	
# x = True	                            bool	
# x = b"Hello"	                        bytes	
# x = bytearray(5)	                    bytearray	
# x = memoryview(bytes(5))	            memoryview	
# x = None	                            NoneType

"""         Python Variables        """

# name = 'Kamron'
# surname = 'Azimboyev'
# age = 19.5
# born_year = 2004

# x = {'Ism' : name, 'Familiya' : surname, 'Yosh' : age, 'Tug`ilgan yil' : born_year}

# print(type(age))
# print(x)
# print(type(x))


"""         Python Lists            """

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# !Pythondagi elementlar nechtaligini aniqlash!

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# Строковые, int и логические типы данных:

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# Список со строками, целыми числами и логическими значениями:

# list1 = ["abc", 34, True, 40, "male"]

# Использование list()конструктора для создания списка:

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)


"""            Python Tuple List            """

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# !One item tuple, remember the comma:
# thistuple = ("apple",)
# print(type(thistuple))

# !NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# !Using the tuple() method to make a tuple:

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

"""            Python Set List            """

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# !Sets are unordered, so you cannot be sure in which order the items will appear.

# !Duplicate values will be ignored:

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# !True and 1 is considered the same value:

# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# !False and 0 is considered the same value:

# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)

# !Using the set() constructor to make a set:

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

"""         Python Dictionaries            """

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# !Print the "brand" value of the dictionary:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# !Duplicate values will overwrite existing values:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# !Using the dict() method to make a dictionary:

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

"""                             Listni o'zgartirish
Listni Index orqali o'zgartirsak bo'ladi 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

!Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

!Change value of variables with index
   
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

!Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

!Измените второе и третье значение, заменив их одним значением:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

!Метод insert()вставляет элемент по указанному индексу:

!Вставьте «арбуз» третьим пунктом:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

List Methods
Python has a set of built-in methods that you can use on lists.

                                Method	Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list

Отсортируйте список по тому, насколько близко число к 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)             #key = function ---> myfunc highlight
print(thislist)

"""