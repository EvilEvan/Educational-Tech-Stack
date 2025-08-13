"""
Exercise 2: Grade Calculator with Conditional Feedback
Module: Programming Fundamentals - Day 3

Description:
Build a program that calculates grades and provides feedback based on performance.
This exercise practices arithmetic operators, conditional statements, and logical thinking.

Learning Objectives:
- Use arithmetic operators for calculations
- Implement conditional logic with if/elif/else
- Apply comparison and logical operators
- Provide meaningful user feedback

Instructions:
1. Ask user for their scores in 5 subjects (0-100 each)
2. Calculate the average grade
3. Determine letter grade (A, B, C, D, F)
4. Provide personalized feedback based on performance
5. Handle edge cases and invalid input

Grading Scale:
A: 90-100 (Excellent)
B: 80-89  (Good)
C: 70-79  (Satisfactory)
D: 60-69  (Needs Improvement)
F: 0-59   (Failing)

Extension Challenges:
- Add weighted grades for different subjects
- Calculate GPA on 4.0 scale
- Show improvement suggestions for each grade range
- Add data visualization with simple ASCII charts
"""

def get_subject_scores():
    """
    Collects scores for 5 subjects from user input.
    
    Returns:
        list: List of valid scores (0-100)
    """
    subjects = ["Math", "Science", "English", "History", "Art"]
    scores = []
    
    print("Enter your scores for each subject (0-100):")
    
    # TODO: Implement score collection with validation
    # for subject in subjects:
    #     while True:
    #         try:
    #             score = input(f"{subject}: ")
    #             # Add validation logic here
    #             break
    #         except ValueError:
    #             print("Please enter a valid number between 0 and 100.")
    
    return scores

def calculate_average(scores):
    """
    Calculates the average of a list of scores.
    
    Args:
        scores (list): List of numeric scores
        
    Returns:
        float: Average score
    """
    # TODO: Implement average calculation
    pass

def determine_letter_grade(average):
    """
    Determines letter grade based on average score.
    
    Args:
        average (float): Average score
        
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    # TODO: Implement grading logic
    # Use if/elif/else statements
    pass

def provide_feedback(letter_grade, average):
    """
    Provides personalized feedback based on grade.
    
    Args:
        letter_grade (str): Letter grade
        average (float): Average score
    """
    # TODO: Implement feedback system
    print(f"\n=== Grade Report ===")
    print(f"Average Score: {average:.1f}")
    print(f"Letter Grade: {letter_grade}")
    
    # Add conditional feedback based on grade
    # if letter_grade == "A":
    #     print("Excellent work! Keep it up!")
    # elif letter_grade == "B":
    #     print("Good job! You're doing well.")
    # ... etc.

def main():
    """Main function to run the grade calculator."""
    print("=== Grade Calculator ===\n")
    
    # Get scores from user
    scores = get_subject_scores()
    
    if scores:  # Check if we have valid scores
        # Calculate average
        average = calculate_average(scores)
        
        # Determine letter grade
        letter_grade = determine_letter_grade(average)
        
        # Provide feedback
        provide_feedback(letter_grade, average)
        
        # TODO: Add additional features
        # - Show individual subject performance
        # - Calculate GPA
        # - Suggest areas for improvement
    else:
        print("No valid scores entered. Please try again.")

if __name__ == "__main__":
    main()

# Sample expected output:
"""
=== Grade Calculator ===

Enter your scores for each subject (0-100):
Math: 85
Science: 92
English: 78
History: 88
Art: 95

=== Grade Report ===
Average Score: 87.6
Letter Grade: B

Good job! You're doing well.
You're close to an A - keep pushing yourself!

Subject Breakdown:
Math: 85 (B)
Science: 92 (A)
English: 78 (C+)
History: 88 (B+)
Art: 95 (A)

Suggested Focus Areas:
- English: Consider additional reading practice
- Math: Review problem-solving techniques
"""
