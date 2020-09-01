def translate(phrase):
    translation = ""
    for letter in phrase:   # checking each letter from 'phrase' and putting it in variable 'translation'
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation


print(translate(input("Enter a phrase: ")))
