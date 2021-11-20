c = True
menu = 'Options:\n'\
       '1 - "+"\n'\
       '2 - "*"\n'\
       '3 - ">"\n'\
       '4 - "CHANGE VALUES"\n'\
       '5 - "OUT"'
menuSelection = 4
while c:
    if menuSelection == 1:
        print('\n\n{} + {} = {}\n\n'.format(num1, num2, num1 + num2))
    elif menuSelection == 2:
        print('\n\n{} * {} = {}\n\n'.format(num1, num2, num1 * num2))
    elif menuSelection == 3:
        print('\n\n' + str(num1) + ' is bigger\n\n' if num1 > num2 else '\n\n' + str(num2) + ' is bigger\n\n')
    elif menuSelection == 4:
        num1 = float(input('Type a number'))
        num2 = float(input('Type a number'))
    elif menuSelection == 5:
        c = False
        break
    else:
        print('\nInvalid value\n')
    print('\n\n' + menu + '\n\n')
    menuSelection = int(input('Select a option of the menu:'))
