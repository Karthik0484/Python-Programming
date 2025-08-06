
# Easy Question
'''

def count_words(text):
    lower = text.lower()
    spli = str.split(lower)
    dic = {}

    for item in spli:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1


count_words("Hello hello world  welcome to python world")

'''

# Medium question

def group_by_first_letter(words):
    grouped = {}

    for word in words:
        lower = word.lower()
        first=word[0]

        if first in grouped:
            grouped[first].append(word)
        else:
            grouped[first] = [word]

    return grouped

words = ['apple','aircraft','ball','bat','cat','car']
result = group_by_first_letter(words)
print(result)




#