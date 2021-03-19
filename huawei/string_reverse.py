# 倒转字符串

# 使用切片
from functools import reduce


def string_reverse_in_slices(string):
    print(string)
    raver_string = string[::-1]
    print("Reversed: %s" % raver_string)


# 使用reverse函数,该方法没有返回值，但是会对列表的元素进行反向排序
def string_reverse_in_reverse(string):
    new_list = list(string)
    new_list.reverse()
    result = ''.join(new_list)
    print(result)


# 使用reduce解决
def string_reverse_in_reduce(string):
    result = reduce(lambda x, y: y + x, string)
    print(result)


# 使用递归函数
def string_reverse_in_recursion(string):
    if len(string) < 1:
        return string
    return string_reverse_in_recursion(string[1:]) + string[0]


# 使用while循环
def string_reverse_in_while(string):
    new_string = ""
    index = len(string)
    while index:
        new_string += string[index-1]
        index = index - 1
    print(new_string)


# 使用for循环
def string_reverse_in_for(string):
    new_string = ''
    index = len(string) - 1
    for i, v in enumerate(string):
        new_string += string[index - i]
    return new_string


# 使用栈（先进后出，类似箱子，先放的书本会先被压在最底下）
def string_reverse_in_pop(string):
    new_string = ''
    inter_stack = list(string)  # 模拟进栈
    while len(inter_stack) > 0:
        new_string += inter_stack.pop()  # 模拟出栈
    return new_string


string_reverse_in_slices("1234567")
string_reverse_in_reverse("12345")
string_reverse_in_reduce("987654")
print(string_reverse_in_recursion("123456"))
string_reverse_in_while("1234")
print(string_reverse_in_pop("abcdefg"))
print(string_reverse_in_for("qwert"))
