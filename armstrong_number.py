n = int(input("Enter a number: "))
sum = 0
order = len(str(n))
dup_n = n

while(n > 0):
    digit = n % 10
    sum += digit ** order
    n = n // 10

if (sum == dup_n):
    print(f"{dup_n} is an armstrong number!")
else:
    print(f"{dup_n} is not an armstrong number")
