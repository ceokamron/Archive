## Linear Search ##
"""
def linear_search(list, item):
   for n in range(len(list)):
      if list[n] == item:
         return n
      
   return None
"""  
## Bineary Search ##
"""
def binary_search(list, item): # tartibsiz listda ishlamidi
   low = 0
   high = len(list) - 1
   while low <= high:
      mid = (low + high) // 2
      guess = list[mid]
      if guess == item:
         return mid
      if guess > item:
         high = mid - 1
      else: 
         low = mid + 1
   
   return None
"""   
# myList = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 99, 101]
# myList.sort()
# print(linear_search(myList, 11))
# print(binary_search(myList, 11))

# fruits = ['olma','nok','olcha','banan','behi','malina']
# fruits.sort()
# print(linear_search(fruits, 'nok'))
# print(binary_search(fruits, 'nok'))

def lSearch(lst, iteam):
   for n in range(len(lst)):
      if lst[n] == iteam:
         return n
   
   return None
   
nums = [100, 100.1, 200.1, 1, 11, 888, 807, 909, 120, 100.5, 201.1, 2004, 2022, 2021, 4096, 10000.1]
letters = ['k', 'a', 'm', 'r', 'o', 'n', 'b', 'f', 'i', 'v', 'g', 's']
nums.sort()
letters.sort()
print(lSearch(nums, 100))
print(lSearch(letters, 'k'))


def binary_search(start, finish):
   l = 0
   h = len(start) - 1
   while l <= h:
      cen = (l + h) // 2
      enter = start[cen]
      if enter == finish:
         return cen
      if enter > finish:
         h = cen - 1
      else:
         l = cen + 1
         
   return None

print(binary_search(nums, 888))
print(binary_search(letters, 'v'))