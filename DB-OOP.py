from mysql.connector import MySQLConnection, Error
from mySqlDbConfig import readDbConfig


def insertGrade(FName, LName, Province, Grade):
    try:
        dbLab12Config = readDbConfig(filename='config.ini', section='lab12')
        conn = MySQLConnection(**dbLab12Config)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Grades (FName, LName,Province,Grade) VALUES ("{}", "{}", "{}", "{}");'
                       .format(FName, LName, Province, Grade))
        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def deleteGrade(FName, LName, Province, Grade):
    try:
        dbLab12Config = readDbConfig(filename='config.ini', section='lab12')
        conn = MySQLConnection(**dbLab12Config)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Grades WHERE FName="{}" AND LName="{}" AND Province="{}" AND Grade="{}";'
                       .format(FName, LName, Province, Grade))
        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def displayGrade(FName, LName, Province):
    try:
        dbLab12Config = readDbConfig(filename='config.ini', section='lab12')
        conn = MySQLConnection(**dbLab12Config)
        cursor = conn.cursor()
        cursor.execute('Select FName, LName, Province,Grade from Grades where FName like "%{}%" AND LName like "%{}%" '
                       'AND Province like "%{}%";'.format(FName, LName, Province))
        row = cursor.fetchone()
        print("<table border='1'>")
        print("<tr><td>FirstName</td><td>LastName</td><td>Province</td><td>Grade</td></tr>")
        while row is not None:
            print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()
        print("</table>")

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def askForValues(description, gradeOrNot=True):
    print(description)
    FName = input('Fist Name: ')
    LName = input('Last Name: ')
    Province = input('Province: ')
    if gradeOrNot:
        Grade = input('Grade: ')
        return {"FName": FName, "LName": LName, "Province": Province, "Grade": Grade}
    else:
        return {"FName": FName, "LName": LName, "Province": Province}


def getUserChoice():
    while True:
        try:
            user_choice = int(input('Select your options (0 to exit): \n 1. Enter a grade \n 2. Delete a grade \n 3. '
                                    'Display a grade \n'))
            if user_choice == 1:
                values = askForValues("Please provide all the following arguments to be inserted into the database.")
                insertGrade(**values)
            elif user_choice == 2:
                values = askForValues("Please provide all the following arguments to be deleted from the database.")
                deleteGrade(**values)
            elif user_choice == 3:
                values = askForValues("Enter the following arguments to look for Grades.", False)
                displayGrade(**values)
            elif user_choice == 0:
                print('OK! exiting')
                break
            else:
                print("PLease insert a valid choice. Try again!")
                continue
        except Error as e:
            print(e)


if __name__ == '__main__':
    getUserChoice()
