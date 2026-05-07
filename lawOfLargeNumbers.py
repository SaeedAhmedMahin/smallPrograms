import random
n = 1
while n < 1000000:
    n *= 10
    total_dice = 0
    total_coin = 0
    for _ in range(n):
        total_dice += random.randint(1, 6)
        total_coin += random.randint(0,1)
    expected_value_dice = total_dice / n
    expected_value_coin = total_coin / n
    print(f'for {n} throws: \ndice expected value: {expected_value_dice} \ncoin expected value: {expected_value_coin}')

