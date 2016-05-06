__author__ = 'Vigo'


# This program is to find antonyms in dictionary
# record file
words = list()
# record signs and line index
dic = {}


def find_antonym(file_path, sign_file_path):
    file = open(file_path)
    out = open(sign_file_path, 'w')
    index = 1
    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip()
        words.append(line)
        word = list(line)
        word.sort()
        s = ''.join(word)
        if dic.get(s) is None:
            line_nums = list()
            line_nums.append(index)
            dic[s] = line_nums
        else:
            line_nums = dic.get(s)
            line_nums.append(index)
            dic[s] = line_nums
        index += 1

    for (key, value) in dic.items():
        result = list()
        for i in value:
            out.write(key + ' ' + words[i - 1] + '\n')
            result.append(words[i - 1])
        print(result)

find_antonym('/Users/lwg/b.txt', '/Users/lwg/c.txt')


