# 求列表元素的最大值
def indexMax(list_number):
    max_number = list_number[0]
    for i in range(len(list_number)):
        if max_number < list_number[i]:
            max_number = list_number[i]
    return max_number
    

list1 = [5, 8, 2, 1, 9, 3, 6, 7]
print(indexMax(list1))