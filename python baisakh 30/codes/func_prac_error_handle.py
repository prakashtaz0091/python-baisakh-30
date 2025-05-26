# 11.Check if a number is prime or not
def is_prime(num):
    a = 10
    if num == 0 or num == 1:
        raise ValueError("Number cannot be 0 or 1")

    for number in range(2, num):
        if num % number == 0:
            break
    else:
        return True

    return False


try:
    number = int(input("Enter a number: "))
    prime = is_prime(number)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    if prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")
finally:
    print("Prime check completed")


# print(is_prime(number))  # function  call -> function lai bolaunu
print("This is the last line")
