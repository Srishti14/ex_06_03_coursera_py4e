def counter(string,the_letter):
    count = 0
    for letter in string:
        if letter == the_letter:
            count = count + 1
    print(count)

counter("srishti","s")
counter("grapes","j")
