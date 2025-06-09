import pdb

def sum_odds_until(n: int) -> int:
    total: int = 0
    current: int = 1

    while total < n:
        pdb.set_trace()
        total += current
        current += 2

    return total

# Revised Version
def sum_odds_until_fixed(n: int) -> int:
    total: int = 0
    current: int = 1

    while total + current <= n:
        pdb.set_trace()
        total += current
        current += 2

    # while True:
    #     total += current
    #     current += 2
    #     if total + current > n:
    #         break
    return total

print(sum_odds_until(10)) 
print(sum_odds_until_fixed(10)) 
