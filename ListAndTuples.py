# Prompts the user for the number of Tests
# Note that this function will include call(s) to the input function
# Keep prompting until the number is an integer. Each grade is in between 0 and 100..
# Returns the number of Tests


def getNumberOfTests():
    while True:
        try:
            test_num = int(input('Please enter the number of tests: '))
            if test_num < 0 or test_num > 100:
                print('Please Enter the Number of tests between 0 and 100:\n')
                continue
            return test_num
        except ValueError:
            print('The value entered is not a valid integer.')


# Prompts the user for the weigth of Assignments
# Note that this function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 1
# Returns the weight of assignments

def getWeightOfAssignments():
    while True:
        try:
            w_assignment = float(input('Please enter weight of the assignments between 0 and 1:\n'))
            if w_assignment < 0.0 or w_assignment > 1.0:
                print('weight of the assignments must be a number between 0 and 1')
                continue
            return w_assignment
        except ValueError:
            print('The value entered is not a valid float.')


# Prompts the user for the weigth of Midterms
# Note that this function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 1
# Returns the weight of midterms

def getWeightOfMidTerms():
    while True:
        try:
            w_midterm = float(input('Please enter weight of midterm between 0 and 1:\n'))
            if w_midterm < 0.0 or w_midterm > 1.0:
                print('Weight of midterm must be a number between 0 and 1')
                continue
            return w_midterm
        except ValueError:
            print('The value entered is not a valid float.')


# Prompts the user for the weigth of the final
# Note that this function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 1
# Returns the weight of final

def getWeightOfFinal():
    while True:
        try:
            w_final = float(input('Enter the weight of final test score between 0 and 1:\n'))
            if w_final < 0.0 or w_final > 1.0:
                print(' the weight of final test score must be between 0 and 1')
                continue
            return w_final
        except ValueError:
            print('The value entered is not a valid float.')


# returns True if the sum of the 3 arguments is 1, False otherwise
# Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively

def checkWeights(w_assignment=0.4, w_midterm=0.35, w_final=0.25):
    total = w_assignment + w_midterm + w_final
    if total == 1:
        return True
    else:
        return False


# calculate the numeric grade as specified in the course outline

def calculateNumericGrade(avgAssignment, avgTests, final, wOfAssign, wOfMidTerms, wFinal):

    return avgAssignment * wOfAssign + avgTests * wOfMidTerms + final * wFinal


# convert the numeric grade to a letter according to the conversion table
# in the course outline

def calculateLetterGrade(numericGrade):
    if numericGrade >= 90:
        return 'A+'
    elif numericGrade >= 85:
        return 'A'
    elif numericGrade >= 80:
        return 'A-'
    elif numericGrade >= 77:
        return 'B+'
    elif numericGrade >= 73:
        return 'B'
    elif numericGrade >= 70:
        return 'B-'
    elif numericGrade >= 67:
        return 'C+'
    elif numericGrade >= 63:
        return 'C'
    elif numericGrade >= 60:
        return 'C-'
    elif numericGrade >= 57:
        return 'D+'
    elif numericGrade >= 53:
        return 'D'
    elif numericGrade >= 50:
        return 'D-'
    else:
        return 'F'


# Get the weight value of the assignments (call the appropriate function)
# Get the weight value of tests (call the appropriate function)
# Get the weight value of the final (call the appropriate function)
# Check the sum of weight values is 1 (call the appropriate function)
# Repeat the last four lines if not equal to 1

user_input_right_value = False
while not user_input_right_value:
    w_Of_assignment = getWeightOfAssignments()
    w_of_midterm = getWeightOfMidTerms()
    w_of_final = getWeightOfFinal()
    if checkWeights(w_Of_assignment, w_of_midterm, w_of_final):
        user_input_right_value = True
    else:
        print('sum of the assignments, midterm and final weights must be equal to 1. Try again!')


# Get the average grade obtained on the assignments
# Validate the input as a float between 0 and 100

user_input_right_value = False
while not user_input_right_value:
    try:
        avgAssignments = float(input('Please enter the average grade of the assignments between 0 and 100:\n'))
        if 0.0 <= avgAssignments <= 100.0:
            user_input_right_value = True
    except ValueError:
        print('The value entered is not a valid the average grade of the assignments must between 0 and 100')


# Get the number of tests (call the appropriate function)
# Prompt the user for each test grades and accumulate the value
# Validate the input as a float between 0 and 100
# Calculate the average test grade.
num_test = getNumberOfTests()
sum_grade = 0
user_input_right_value = True

for i in range(num_test):
    while user_input_right_value:
        try:
            grade = float(input('Please enter test {} grade between 0 and 100:\n'.format(i+1)))
            if grade < 0.0 or grade > 100.0:
                print(' the grade must be between 0 and 100. You will be prompted to insert again.')
                user_input_right_value = False
            sum_grade += grade
            break
        except ValueError:
            print('The value entered is not a valid')
avgMidterm = sum_grade/num_test


# Prompt and get the final grade
# Validate the input as a float between 0 and 100

user_input_right_value = False
while not user_input_right_value:
    try:
        final_grade = float(input('Please enter the final grade between 0 and 100:\n'))
        if 0.0 <= final_grade <= 100.0:
            user_input_right_value = True
    except ValueError:
        print('The value entered is not a valid the average grade of the assignments must between 0 and 100 ')


# Calculate and display the final numeric grade (call the appropriate function)

numeric_grade = calculateNumericGrade(avgAssignments, avgMidterm, final_grade, w_Of_assignment, w_of_midterm, w_of_final)
print(f'Numeric grade is: {numeric_grade}')


# Calculate and display the final alphabetical grade (call the appropriate function)

alphabetical_grade = calculateLetterGrade(numeric_grade)
print(f'Alphabetical grade is: {alphabetical_grade}')
