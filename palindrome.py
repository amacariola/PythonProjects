# determine if the input string is a palindrome, a word that even spelled reverse is still the same

def solution(s):
    try:
        for i in range(len(s)):
            t = s[:i] + s[i + 1:]
            if t == t[::-1]:
                return True
        return s == s[::-1]
    except Exception as e:
        print('Error',str(e))

print(solution(input('Input word here: ')))