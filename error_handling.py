# Error handling in Python
while True:
    try:
        user_name = str(input('What is your name? '))
        user_age = int(input('What is your age? '))
    except ValueError:
        print('Please enter a valid age')
    except ZeroDivisionError:
        print('Please enter an age that is greater than zero')
    else:
        print('Thank you!')
        break
