"""
Exercise 1: Personal Information Collector
Module: Programming Fundamentals - Day 2

Description:
Create a program that collects personal information from a user and 
displays it in a formatted way. This exercise practices variables, 
data types, and input/output operations.

Learning Objectives:
- Use input() to collect user data
- Store data in appropriate variable types
- Practice string formatting
- Implement basic data validation

Instructions:
1. Ask the user for their name, age, favorite color, and hometown
2. Convert age to integer and validate it's positive
3. Display the information in a nicely formatted output
4. Add error handling for invalid age input

Extension Challenges:
- Add more personal details (hobbies, occupation, etc.)
- Implement input validation for all fields
- Save the information to a text file
- Add a welcome message with the current date/time
"""

# TODO: Implement the personal information collector here

def collect_personal_info():
    """
    Collects and displays personal information from user input.
    
    Returns:
        dict: Dictionary containing user's personal information
    """
    print("=== Personal Information Collector ===")
    print("Please provide the following information:\n")
    
    # Collect basic information
    # TODO: Add your code here
    
    # Example structure (students should implement this):
    # name = input("Enter your name: ")
    # age = input("Enter your age: ")
    # favorite_color = input("Enter your favorite color: ")
    # hometown = input("Enter your hometown: ")
    
    # TODO: Add age validation and conversion to integer
    
    # TODO: Create a dictionary to store the information
    
    # TODO: Display the formatted information
    
    pass

def main():
    """Main function to run the exercise."""
    try:
        user_info = collect_personal_info()
        # TODO: Add any additional processing here
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# Sample expected output:
"""
=== Personal Information Collector ===
Please provide the following information:

Enter your name: Alice Johnson
Enter your age: 25
Enter your favorite color: Blue
Enter your hometown: Seattle

=== Your Information ===
Name: Alice Johnson
Age: 25 years old
Favorite Color: Blue
Hometown: Seattle, WA

Thank you for using the Personal Information Collector!
"""
