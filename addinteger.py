# add integers without using BigInt libs

num1 = input('Input integers here:')
num2 = input('Input integers here:')

def solution(num1,num2):
    try:
        eval(num1) + eval(num2)
        return str(eval(num1) + eval(num2))
    except Exception as e:
        print('Error',str(e))

print(solution(num1,num2))