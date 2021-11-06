"""
找出字串a 中含有字串b所有字母的相同/異子字串的起點位置
String a = “abcdefgcabegswkuncbakun”
String b = “cba”
->ex abc [0], cab [7],  cba [17]
"""


# Quiz_1
def start_position(text, key_word):
    results = []
    count = 0
    for key_a, value_a in enumerate(text):
        for value_b in key_word:
            # find one character
            if value_a == value_b:
                count += 1
                # find all character
                if count >= len(key_word):
                    index = key_a - len(key_word) + 1
                    string = text[index:index+len(key_word)]
                    results.append(f'{string}[{index}]')
                break
        # not find all character
        else:
            count = 0
    return results


if __name__ == '__main__':
    a = 'abcdefgcabegswkuncbakun'
    b = 'cba'

    results = start_position(a, b)
    list(map(lambda x: print(x, end=', '), results))
