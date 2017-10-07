def anagram_test(s1,s2):
    alist = list(s2)

    pos1 = 0
    OK = True

    while pos1 < len(s1) and OK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            OK = False

        pos1 = pos1 + 1

    return OK

print(anagram_test('12345','12534'))
print(anagram_test('aeta','tame'))
print(anagram_test('pesto','tespo'))

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))

# the above are quite inefficient. Here is the n linear solution:

def anagram_test(s1,s2):
    alist = list(s2)

    pos1 = 0
    OK = True

    while pos1 < len(s1) and OK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            OK = False

        pos1 = pos1 + 1

    return OK

print(anagram_test('12345','12534'))
print(anagram_test('aeta','tame'))
print(anagram_test('pesto','tespo'))

