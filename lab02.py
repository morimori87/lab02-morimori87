# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(seconds: int):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    
    hours = seconds // 3600
    remainder = seconds % 3600
    minutes = remainder // 60
    seconds = seconds % 60
    formatted = f'{hours}:{minutes:02d}:{seconds:02d}'
    return (formatted)

# print(seconds_to_hms(3661))


def admission_price(age: int):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    if (age >= 65):
        ticket_price: float = 10.00
    elif (age >= 13):
        ticket_price: float = 15.00
    elif (age >= 5):
        ticket_price: float = 8.00
    else:
        ticket_price = 0.00
    return ticket_price

# print(admission_price(8))


def sum_multiples(limit: int):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    sum = 0
    for below in range(0, limit, 1):
        if (below % 3 == 0) or (below % 5 == 0): #when equalling use 2 = otherwise itll think ur naming a variable
            sum += below # have a variable before otherwise itll be confusing //also using a += adds to existing value
    return sum
# print(sum_multiples(26))



def total_of_positives(numbers: list):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    total = 0
    for within in numbers:
        if within > 0:
            total += within
    return total
# print(total_of_positives([13,-2,3]))
    



def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    #  print(seconds_to_hms(3661))            # 1:01:01
    #  print(admission_price(10))             # 8
    #  print(sum_multiples(10))               # 23
    #  print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
