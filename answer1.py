# print("Please enter 2 sets of any letters (A~Z).")
a = set(input("Please enter array1: "))
b = set(input("Please enter array2: "))

b.issubset(a)


#return True if 2nd array is subset of 1st array
#else, return False
#computational complexity = O(len(b) * len(a))

