import random 

def welcome():
    print("Welcome to this funny game")
    print("I will guess a number between 1 and 20 and")  # ✅ اصلاح شد
    print("you have to guess it... ")
    print("go go go")
    print()

def finish(number, count):
    print("Good game.")
    print(f"My number was {number} and you found it in {count} guesses")  # ✅ اصلاح شد
    print("\n")
    answer = input("Do you want to play again? (Y/N) ")
    return answer.upper() in ['Y', 'YES']

def win(computer_number, guess):
    return computer_number == guess

def answer(computer, user):
    if computer > user:
        return "My number is larger"
    if computer < user:
        return "Oh no, you went too high! My number is smaller"  # ✅ اصلاح شد
    return "Wow! you won! Good Guess!"

def get_a_guess():
    while True:  # ✅ افزوده شد
        ans = input("What is your guess? ")
        try:
            return int(ans)  # ✅ اصلاح شد
        except ValueError:
            print("⚠️ لطفاً یک عدد صحیح وارد کنید!")  # ✅ اصلاح شد

welcome()
continue_playing = True

while continue_playing:
    computer_number = random.randint(1, 20)
    guess = 0
    count = 0
    while not win(computer_number, guess):
        guess = get_a_guess()
        count += 1
        print(answer(computer_number, guess))
    continue_playing = finish(computer_number, count)