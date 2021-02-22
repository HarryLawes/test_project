def try_me():
    input('Think of a number \n >> Got it?')
    input('Double it')
    input('Add 8')
    input('Subtract 2')
    input('Halve it')
    input('Subtract your original number')
    check = input('Now you have 3! Am I correct?? \n >> Yes/No?')
    if check != 'Yes' and check != 'yes' and check != 'Y' and check != 'y' and \
        check != 'No' and check != 'no' and check != 'N' and check != 'n':
        check = input("I don't understand. Type 'Yes' or 'No' \n >> ")
    if check == 'Yes' or check == 'yes' or check == 'Y' or check == 'y':
        print("Magic!")
    if check == 'No' or check == 'no' or check == 'N' or check == 'n':
        print("I think you should use a calculator next time")
