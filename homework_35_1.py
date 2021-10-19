previous_number = 0
for index in range(0, 100):
    number = int(input('Enter a number: '))
    if number >= previous_number:
        pass
    else:
        print ('Not sorted.')
        break
    previous_number = number

if index == 99 :
    print('Sorted.')
