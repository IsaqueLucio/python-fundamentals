'''
Create a variable grade (from 0 to 100). 
Use if/elif/else to print "A" (>= 90), "B" (>= 80), "C" (>= 70) or "Failed" (< 70).
'''

grade = 80

if grade >= 90:
    print(f"Congratulations! You got an A. Passed with flying colors!")
elif grade >= 80:
    print(f"Congratulations! You got a B. Passed with good results!")
elif grade >= 70:
    print(f"Congratulations! You got a C. Passed with satisfactory results!")
else:
    print(f"Sorry, you failed. Better luck next time!")