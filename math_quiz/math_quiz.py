import random

def RandomNumber(minVal, maxVal):
    """
    Generates a random integer between the given min and max values.
    """
    return random.randint(minVal, maxVal)

def RandomOperator():
    """
    Generates a random mathematical operator (+, -, or *).
    """
    return random.choice(['+', '-', '*'])

def Calculation(num1, num2, operator):
    """
    Performs the arithmetic operation based on the operator provided.
    Returns a tuple containing the problem and the actual answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def MathQuiz():
    """
    Create a math quiz game for the user with three questions.
    """
    score = 0
    totalQuestions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(totalQuestions):
        num1 = RandomNumber(1, 10)
        num2 = RandomNumber(1, 10) 
        operator = RandomOperator()

        problem, answer = Calculation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            userAnswer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if userAnswer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{totalQuestions}")

if __name__ == "__main__":
    MathQuiz()
