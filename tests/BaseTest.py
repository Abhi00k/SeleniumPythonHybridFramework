# import pytest
# from datetime import datetime
#
#
# @pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
# class BaseTest:
#     pass
#
#     def generate_email_with_time_stamp(self):
#         time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#         return "kumar.abhishek" + time_stamp + "@gmail.com"


# str = "ram is the god of all"
# print(str.split())
# str1 = str.replace(" ", "")
# str1 = "".join(str.split())
# print(str1)
# dict = {}
# for item in str1:
#     if item in dict:
#         dict[item] += 1
#     else:
#         dict[item] = 1
# print(dict)
# print(max(dict.values()))
# char_count = 0
# special_count =0
# number_count =0
# sum =0
# str = "qerty@#445"
# for i in str:
#     if i.isdigit()==True:
#         y = int(i)
#         sum = sum+y
# print(sum)
# for i in str:
#     if i.isdigit():
#         number_count+=1
#     elif i.isalpha():
#         char_count+=1
#     else:
#         special_count+=1
# print(char_count, special_count, number_count)

list = [1, 2, 3]
left = 0
right = len(list)-1
while (left<right):
    temp = list[left]
    list[left] = list[right]
    list[right] = temp
    left+=1
    right -=1
print(list)






