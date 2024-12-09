import random
import datetime

if __name__ == '__main__':
    first_var = random.randint(1, 5)
    second_var = random.randint(1, 5)
    if first_var == second_var:
        print("The numbers are equals with value: " + str(first_var))
    else:
        print("The numbers are not equals, first num value: " + str(first_var) + " Second number value is: " + str(second_var))

    
    date = datetime.datetime.now()
    formatted_date = date.strftime('%m-%d-%Y %H:%M:%S')
    print(formatted_date)
