import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable
countrycode = str(input("Enter the code of the country: "))

#Scan the list l line by line and add 1 to the counter if the country is the one looked for
counter = 0
for i in l:
    if i == countrycode:
        counter = counter + 1

#Format and print the result
print("the code appears {} times".format(counter))

#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
user_input_right_value = False

while user_input_right_value == False:
    try:
        population = int(input("Enter the population: "))
        user_input_right_value = True
    except ValueError:
        print("your input error")

#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list
lstOfRecords = []

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
pindex = 0
for i in l1:
    if i > population:
        lstOfRecords.append(pindex)
    pindex = pindex + 1

print("list 0f Records is:")
print( lstOfRecords)

#Print the list lstOfRecords


#Bonus: Print the name of the cities whose index is in lstOfRecords
print ("The name of the cities are:")
l2 = list(db.ws(ws='Sheet1').col(col=4))
for i in lstOfRecords:
    print (l2[i])