def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
print("Number is:", even_or_odd(num))
if is_prime(num):
    print("Number is Prime")
else:
    print("Number is Not Prime")
