def get_all_substrings(input_string, Vowels = True):
    length = len(input_string)
    input_string = str(input_string).lower()
    if Vowels == True:
        return len([input_string[i:j + 1] for i in range(length) for j in range(i,length) if input_string[i] in ["a", "e", "i", "o", "u"]])
    else:
           return len([input_string[i:j + 1] for i in range(length) for j in range(i,length) if input_string[i] not in ["a", "e", "i", "o", "u"]])


def minion_game(string):
    vw = 'aeiou'.upper()
    strl = len(string)
    kevin = sum(strl-i for i in range(strl) if string[i] in vw)
    stuart = sum(strl-i for i in range(strl) if string[i] not in vw)

    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin %d' % kevin)
    else:
        print('Stuart %d' % stuart)

if __name__ == "__main__":
    minion_game(input())
        
    