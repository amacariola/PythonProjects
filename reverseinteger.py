# Strings manipulation
# given an integer, return the integer in reverse

def solution(x):
    try:
        string = str(x) # make x a string in order to manipulate it
        if string[0] == '-':
            return int('-' + string[:0:-1])
        else:
            return int(string[::-1])
    except:
        print('Error')


print(solution(input('Input String here:')))