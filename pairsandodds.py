number = int(input("Insert a number, please."))
word = str(input("Tell me a word that you can see replacing pair numbers:"))
numlist = [1, f"{word}"]
counter = 1
while True:
    if number < 0:
        print("Please, insert a positive number.")
        number = int(input("Insert a number, please."))
    else:
        if number % 2 == 0:
            if counter > number  - 2:
                break
            counter = counter + 2                
            numlist.append(counter)
            numlist.append(word)
        if number % 2 != 0:
            if counter > number - 1:
                break
            counter = counter + 2
            numlist.append(counter)
            numlist.append(word)
print(f"Odd numbers from 1 to {number} are {numlist}")