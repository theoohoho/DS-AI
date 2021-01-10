"""Array Implementation"""
# random access
# Time Complexity is O(1)
arr = [1,2,3,4,5,6]
arr[0]

# linear searching
# Time Complexity is O(n)
max = a[0]
for i in arr:
    if i >= max:
        print(i)

"""Multi dimention array"""
# Two dimention array
# Array[row, column]
# For example: 班上有三個學生，進行考試，總共考了3 個科目
# Row: 學生名稱、Column 科目名稱
# 'jack':{'math': 10,'english': 20,'chinese': 30}
two_dimention_array = [{10,20,30}, {20,30,40},{30,40,50}]

# 一個學期有兩次考試
three_dimention_array = [
    [{10,20,30}, {20,30,40},{30,40,50}],
    [{10,20,30}, {20,30,40},{30,40,50}],
]

# 一年有兩個學期，每個學期有兩次考試，每次考試都有3個科目要考
four_dimention_array = [[
    [{10,20,30}, {20,30,40},{30,40,50}],
    [{10,20,30}, {20,30,40},{30,40,50}],
],
[
    [{10,20,30}, {20,30,40},{30,40,50}],
    [{10,20,30}, {20,30,40},{30,40,50}],
]]