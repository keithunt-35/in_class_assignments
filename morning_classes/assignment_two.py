def divide_numbers():
    """
    Continuously asks for two numbers and divides them,
    handling potential errors with appropriate messages.
    """
    while True:  # Infinite loop
        print("\n--- Division Calculator ---")
        
        try:
            # Get first number
            num1 = float(input("Enter first number: "))
            
            # Get second number
            num2 = float(input("Enter second number: "))
            
            # Attempt division
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result:.2f}")
            
            # Ask if user wants to continue
            choice = input("\nDo you want to perform another calculation? (y/n): ").lower()
            if choice != 'y':
                print("Goodbye!")
                break  # Exit the loop
            
        except ValueError:
            print("Error: Please enter valid numbers (digits only)")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    divide_numbers()