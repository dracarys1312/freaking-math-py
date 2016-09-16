import random
def generate_quiz():
    signs = ["+", "+", "+", "-", "*", "/"]
    pad = [0, -1, 1, 0]
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sign = random.choice(signs)
    answer = calculate(num1, num2, sign) + random.choice(pad)
    return [num1, num2, sign, answer]

def check_answer(num1, num2, sign, answer, correct):
    right_answer = calculate(num1, num2, sign)
    if correct:
        return right_answer == answer
    else:
        return right_answer != answer

def calculate(num1, num2, sign):
    print(sign)
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "*":
        return num1 * num2
    elif sign == "/":
        return num1 / num2
