try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number')

print('\nAttempted Input\n')

while True:
    try:
        x = int(input('Enter a number: '))
    except ValueError:
        print('That\'s not a valid number')
    except KeyboardInterrupt:
        print('\nNo input taken')
        break
    finally:
        print('\nAttempted Input\n')
