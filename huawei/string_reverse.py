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


string_reverse_in_slices("1234567")
string_reverse_in_reverse("12345")
string_reverse_in_reduce("987654")
print(string_reverse_in_recursion("123456"))
