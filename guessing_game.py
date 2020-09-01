secret_word = "secret"
guess_word = ""
guess_count = 0
guess_finished = False

while guess_word != secret_word and not guess_finished:
    if guess_count < 3:
        guess_word = input("Enter word: ")
        guess_count += 1
    else:
        guess_finished = True

if guess_finished:
    print("Out of guesses")
else:
    print("You win.")