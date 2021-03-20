# 写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写。

# 使用for循环
def count_letter_in_for():
    letter = "A"
    sentence = "ABCabc"
    count = 0
    for i in sentence:
        if i == "A" or i == "a":
            count += 1
    print(count)


# 使用count函数
def count_letter_in_fun(letter="a", sentence="ABCabc"):
    new_letter = letter.lower()
    new_sentence = sentence.lower()
    print(new_sentence.count(new_letter))


count_letter_in_for()
count_letter_in_fun()