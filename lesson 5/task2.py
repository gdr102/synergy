word = input("Введите слово маленькими латинскими буквами: ")

vowels_count, consonants_count, a_count, e_count, i_count, o_count, u_count = 0, 0, 0, 0, 0, 0, 0

for letter in word:
    if letter in 'aeiou':
        vowels_count += 1

        if letter == 'a':
            a_count += 1

        elif letter == 'e':
            e_count += 1

        elif letter == 'i':
            i_count += 1

        elif letter == 'o':
            o_count += 1

        elif letter == 'u':
            u_count += 1

    else:
        consonants_count += 1

print("Количество гласных букв:", vowels_count)
print("Количество согласных букв:", consonants_count)

if a_count > 0:
    print("a:", a_count)

else:
    print("a: False")

if e_count > 0:
    print("e:", e_count)

else:
    print("e: False")

if i_count > 0:
    print("i:", i_count)

else:
    print("i: False")

if o_count > 0:
    print("o:", o_count)

else:
    print("o: False")

if u_count > 0:
    print("u:", u_count)

else:
    print("u: False")