def min_coin_count(value, coin_list):
    total_coin_count = 0
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_count = value // coin
        total_coin_count += coin_count
        value -= coin_count * coin
    return total_coin_count

    
coin_list = [100,10,500,1000]
value = 2610
print(min_coin_count(2610, coin_list))
