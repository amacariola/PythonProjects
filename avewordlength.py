# average word length

s1 = input('Input your sentence here:')

def solution(s1):
    try:
        for p in "!?';.":
            s = s1.replace(p,'')
        words = s.split()
        return round(sum(len(word) for word in words)/len(words),2)
    except KeyboardInterrupt:
        print('Program Closing')
    except:
        print('Error')
print(solution(s1))