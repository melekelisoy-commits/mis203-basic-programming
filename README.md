# mis203-basic-programming
Name: Melek Alisoy
Student Number: 2304109905
Department: Management Information Systems
Course Name: Mis203 - Basic Programming

AI Tool Used: ChatGPT
Prompt Used: Write a simple Python program that asks for Name, Department, Age, and Career Goal, then prints a short student profile.
What did you change?: I customized the prompt texts in the input function and formatted the output layout to match the required example.



week02

AI Tool Used: Gemini
Prompt Used: How to handle invald inputs and structure letter grade logic in a Python while lopp.
What did you change? : I integrated the logic into my script, refined the loop conditions using `try-except` for input validation and added formatting for the average score output.
What does break do in your program? : It immediately terminates the `while True` loop when the user enters 'q', allowing to program to proceed to calculating and printing the final summary statistics.


##week03

AI Tool Used: Gemini
Prompt Used: Explain the basic logic, flow and edge cases for a Pyton movie ticket office assignment involving loops, input validation and conditional discount checking
What did you change: I used AI tools to understand the underlying logic and requirement of the project . Based on that understanding. I wrote and structured the entire Python script myself:
Tests:
Input: Name = "Can", Age = 5, Day = "weekend", Student = "no" -> Output: "Can: 0.00 TRY (Free)" (Boundary test for age < 6)
Input: Name = "Deniz", Age = 10, Day = "weekday", Student = "yes" -> Output: "Zeynep: 120.00 TRY (Child) (Boundary test for 6 to 12 age range)
Input: Name = "Zeynep", Age = 20, Day = "weekday", Student = "yes" -> Output: "Zeynep: 140.00 TRY (Student)" (Student discount test)
Why does the order of the rules matter?: The rules are evaluated sequentially using if/elif statements. If the Student rule came before the Child rele, a 10 year old student would trigger the Student rule first.