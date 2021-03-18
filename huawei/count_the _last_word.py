# 题目：计算字符串最后一个单词的长度，单词以空格隔开。
# 输入一行，代表要计算的字符串，非空，长度小于5000。


# 使用自带函数解决
def count_the_last_word_in_func(string):
    if 0 < len(string) < 5000:
        new_string = string.split(' ')
        print(len(new_string[-1]))
    else:
        print("too much char or null")


# 使用for循环
def count_the_last_word_in_normal(string):
    length = 0
    for i in range(len(string), -1, -1):
        if string[i-1] == ' ':
            break
        length = length + 1
    return length


count_the_last_word_in_func("hello luodayu")
print(count_the_last_word_in_normal("yes 21"))
