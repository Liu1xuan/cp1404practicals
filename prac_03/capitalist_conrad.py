import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
NUM_DAYS = 425
OUTPUT_FILE = "conrad.txt"

out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)

for day in range(1, NUM_DAYS + 1):
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    price = max(price, MIN_PRICE)
    price = min(price, MAX_PRICE)
    print(f"On day {day} price is: ${price:,.2f}")
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

out_file.close()
