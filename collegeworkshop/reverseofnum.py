num = 1234
reverse= 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number: ",reverse)