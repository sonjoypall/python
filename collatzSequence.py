def collatz(number):
    if number % 2 == 0:
        print(number)
        return number // 2
    else:
        print(number)
        return 3 * number + 1

result = collatz(int(input("Enter a int Number ")))
    
while 1:
    if result == 1:
        print(result)
        break
    else:
        result = collatz(result)
        continue
    
