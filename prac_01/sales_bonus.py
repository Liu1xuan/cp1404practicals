sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        user_get = sales * 0.1
        print(f"Your bonus is {user_get}")

    else:
        user_get = sales * 0.15

        print(f"Your bonus is {user_get}")
    sales = float(input("Enter sales: $"))








