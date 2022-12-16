import random

mylist = ["apple", "banana", "cherry"]

#no exception throw
#when exception occurs , always get the same element.
print("1",random.choices(mylist, weights = [1, 1, 1], k = 14))
print("2",random.choices(mylist, weights = [1, 2, 3], k = 14))
print("3",random.choices(mylist, weights = [10, 1, 1], k = 14))
print("4",random.choices(mylist, weights = [0, 1, 1], k = 14))
print("5",random.choices(mylist, weights = [10, 21, 1], k = 14))
print("6",random.choices(mylist, weights = [10, -1, 1], k = 14))
print("7",random.choices(mylist, cum_weights = [1, 2, 3], k = 14))
print("8",random.choices(mylist, cum_weights = [1, 1, 1], k = 14))
print("9",random.choices(mylist, cum_weights = [3, 3, 3], k = 14))
print("10",random.choices(mylist, cum_weights = [0, 2, 2], k = 14))
print("11",random.choices(mylist, cum_weights = [1, 0, 0], k = 14))
print("12",random.choices(mylist, cum_weights = [1, 2, -1], k = 14))
