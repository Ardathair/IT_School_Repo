'''
Problema 1. Se citeste de la tastatura o parola. Sa se verifice daca parola introdusa are cel putin 10 caractere si nu
contine spatiu.
Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita sau mesajul "OK" in cazul in care parola respecta
regulile.
hints: boolean, conditionals
'''

while True:
    print("Please enter a password containing no spaces and at least 10 letters.")
    password = input("Password: ")

    has_enough_letters = False
    has_no_spaces = True

    letter_count = 0
    for char in password:
        if char.isalpha():
            letter_count += 1

    if letter_count >= 10:
        has_enough_letters = True

    if ' ' in password:
        has_no_spaces = False

    if has_enough_letters and has_no_spaces:
        print("Password entered successfully.")
        break
    else:
        print("Password is invalid.")
        if not has_enough_letters:
            print(f"- The Password should have at least 10 letters (You have {letter_count}).")
        if not has_no_spaces:
            print("- The Password cannot contain spaces.")
        print("Please try again.\n")

#####

'''
Problema 2. Sa se numere de cate ori apare o litera intr-un cuvant.
'''

while True:
    word = input("Enter a word you'd like to count the number of letters of: ")
    if word.isalpha():
        break
    else:
        print("Please enter a word containing only letters.")

while True:
    letter = input("Enter a letter you'd like to count: ")
    if len(letter) == 1:
        break
    else:
        print("Please enter exactly one letter.")

word = word.lower()
letter = letter.lower()
count = word.count(letter)

print(f"The letter '{letter}' is in '{word}' {count} time(s).")

#####

'''
Problema 3. Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.
'''

print("Puterile lui 3 cuprinse intre 200 si 300 sunt: ")

power = 3
exponent = 1

while power <= 300:
    if power >= 200:
        print(f"3^{exponent} = {power}")

    power = power * 3
    exponent += 1

#####

'''
Problema 5. Rezolvati folosind doua variante: 
    Varianta 1 -> FOR
    Varianta 2 -> WHILE
Se citeste un numar n de la tastatura. Sa se scrie un program care face o numaratoare inversa de la numarul respectiv
pana la 0.
'''

##FOR##

for _ in range(1000):
    print("Please enter a number.")
    user_input = input("Number: ")

    try:
        number = int(user_input)
        if number > 0:
            print(f"Counting down from {number} to 0:")
            for i in range(number, -1, -1):
                print(i)
            break
        elif number < 0:
            print(f"Counting up from {number} to 0:")
            for i in range(number, 1):
                print(i)
            break
        else:
            print("This exercise has no point if your number is 0")
            break

    except ValueError:
        print("Error: Please enter numbers only (no letters or symbols).")
        print("Try again.\n")

#####

##WHILE##

while True:
    print("Please enter a number.")
    user_input = input("Number: ")

    try:
        number = int(user_input)
        if number > 0:
            print(f"Counting down from {number} to 0:")
            i = number
            while i >= 0:
                print(i)
                i -= 1
            break
        elif number < 0:
            print(f"Counting up from {number} to 0:")
            i = number
            while i <= 0:
                print(i)
                i += 1
            break
        else:
            print("This exercise has no point if your number is 0")
            break

    except ValueError:
        print("Error: Please enter numbers only (no letters or symbols).")
        print("Try again.\n")

#####

'''
Problema 6. Rezolvati folosind doua variante:
    Varianta 1 -> FOR
    Varianta 2 -> WHILE
Se citeste un numar de la tastatura. Sa se calculeze suma numerelor de la 1 pana la numarul citit. (folositi for si while)
'''