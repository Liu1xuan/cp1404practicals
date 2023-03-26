import random

def main():
    user_score = get_valid_score()
    print(get_result(user_score))

    random_score = random.randint(0,100)
    print(f"Random score {random_score}")
    print(f"Result for random score: {get_result(random_score)}")

def get_valid_score():
    score = float(input("Enter score: "))
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