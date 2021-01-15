# given a string find the first non repeating character in it and return its index

def solution(s):
    try:
        frequency = {}
        for i in s:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i
        return -1
    except:
        print('Error')

print(solution(input('Input your string here: ')))