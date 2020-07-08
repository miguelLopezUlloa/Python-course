
def coins(coin_list):
    first = coinsChanges(coin_list)
    first_coin = coin_list[0]
    if first_coin == 1:
        coin_list[0] = 0;
    else:
        coin_list[0] = 1;
    with_changes = coinsChanges(coin_list)
    with_changes += 1
    if first <= with_changes:
        print(first)
        return first
    else:
        print(with_changes)
        return with_changes


def coinsChanges(coin_list):
    previus_coin = coin_list[0];
    index = 0
    changes = 0
    for current_coin in coin_list:
        if index != 0:
            if previus_coin == current_coin:
                changes += 1
                if previus_coin == 1:
                    previus_coin = 0
                else:
                    previus_coin = 1
            else:
                previus_coin = current_coin
        else:
            index += 1
    return changes



