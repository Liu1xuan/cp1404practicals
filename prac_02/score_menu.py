MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = str(input(">>> ")).upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()

        elif choice == "P":
            result = get_result
            print(f"Your score is {score} and Your level is {result}")

        elif choice == "S":
            print("*" * score)

        else:
            print("Invalid choice")
        print(MENU)
        choice = str(input(">>> ")).upper()

    print("Thanks for using with us !")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()


