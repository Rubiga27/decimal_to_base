A = int(input())
B = int(input())
result = ""
while A > 0:
    remainder = A % B
    result = str(remainder) + result
    A //= B
print(result)
