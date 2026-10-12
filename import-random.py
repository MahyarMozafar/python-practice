import random

def play_game():
    # computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    tries = 0
    max_tries = 7

    print("🎮 به بازی حدس زدن عدد خوش اومدی!")
    print(f"من یه عدد بین 1 تا 100 انتخاب کردم. {max_tries} تا شانس داری.")
    print("-" * 40)

    while tries < max_tries:
        guess_input = input("حدس تو: ")

        # check if input is a valid number
        if not guess_input.isdigit():
            print("❌ لطفاً فقط عدد وارد کن.")
            continue

        guess = int(guess_input)
        tries += 1

        if guess < secret_number:
            print(f"⬆️ بزرگ‌تر بگو! (تلاش {tries}/{max_tries})")
        elif guess > secret_number:
            print(f"⬇️ کوچیک‌تر بگو! (تلاش {tries}/{max_tries})")
        else:
            print(f"🎉 آفرین! درست حدس زدی! عدد {secret_number} بود.")
            print(f"تعداد تلاش‌هات: {tries}")
            return

    print(f"😢 شانست تموم شد. عدد درست {secret_number} بود.")


if __name__ == "__main__":
    play_game()

    # ask if user wants to play again
    again = input("\nدوباره بازی کنیم؟ (y/n): ")
    while again.lower() == "y":
        print("-" * 40)
        play_game()
        again = input("\nدوباره بازی کنیم؟ (y/n): ")

    print("ممنون که بازی کردی! 👋")