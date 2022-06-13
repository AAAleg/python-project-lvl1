from brain_games.tools import generate_number


DESCRIPTION = "Find the greatest common divisor of given numbers."


def play():
    number1 = generate_number()
    number2 = generate_number()
    question = f'Question: {number1} {number2}'
    correct_answer = gcd(number1, number2)
    return question, str(correct_answer)


def gcd(num1, num2):
    if not num2:
        return num1
    return gcd(num2, num1 % num2)
