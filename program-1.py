class Calculator:
    def __init__(self, num1: float, num2: float, operation: str):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation.lower()

    def perform_operation(self):
        if self.operation == "add":
            return self.num1 + self.num2
        elif self.operation == "subtract":
            return self.num1 - self.num2
        elif self.operation == "multiply":
            return self.num1 * self.num2
        elif self.operation == "divide":
            if self.num2 == 0:
                return "Oops! You can't divide by zero."
            return self.num1 / self.num2
        else:
            return "Hmm... that operation isn't supported."
def main():
    print("Welcome to the Simple Calculator!")

    try:
        # user input
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("What would you like to do?")
        print("Options: add, subtract, multiply, divide")
        op = input("Enter the operation: ")

        # Create calculator object and perform operation
        calc = Calculator(a, b, op)
        result = calc.perform_operation()

        print(f"The result is: {result}")
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()