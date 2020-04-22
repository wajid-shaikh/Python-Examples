# else and finally clause in exception handling

while True:
    try:
        number = int(input('enter a number = '))
    except ValueError:
        print('Please enter integer ... ')
    except:
        print('unexpected error !!! ')
    else:
        print(f"user input = {number}")
        break
    finally:
        print('finally always runs ')

