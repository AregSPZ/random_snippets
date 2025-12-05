'''Find all possible TOEFL score combinations while having the minimum target cumulative score,
    minimum required score per section, and the minimum score user is confident they can get for each section'''

import time

def combinations(lower_sum, upper_sum):
    '''Find all combinations of 4 non negative integers a, b, c, d where upper_sum >= a + b + c + d >= lower_sum'''
    result = []
    diff = upper_sum - lower_sum
    ceiling = upper_sum // 4
    for D in range(diff+1):
        for a in range(min(lower_sum + 1 + D, ceiling+1)):
            for b in range(min(lower_sum - a + 1 + D, ceiling+1)):
                for c in range(min(lower_sum - a - b + 1 + D, ceiling+1)):
                    d = (lower_sum+D) - a - b - c
                    if d <= ceiling:
                        result.append([a, b, c, d])
    return result

def toefl_combinations(Score, Min=0):
    '''Find all combinations of 4 non negative integers a, b, c, d where a + b + c + d = Score and min(a, b, c, d) >= Min'''
    template = "\n\nWhat's the minimum score you are confident you will get for "
    mina = int(input(template + "Reading Section (0 to 30)?: "))
    minb = int(input(template + "Listening Section (0 to 30)?: "))
    minc = int(input(template + "Speaking Section (0 to 30)?: "))
    mind = int(input(template + "Writing Section (0 to 30)?: "))
    # the minimum required score can be ignored for simplicity, as the solution doesnt change functionally
    all_combinations = [[x+Min for x in s] for s in combinations(Score-4*Min, 120-4*Min)] if Min != 0 else combinations(Score, 120)
    result = []
    for comb in all_combinations:
        if comb[0] < mina or comb[1] < minb or comb[2] < minc or comb[3] < mind:
            continue
        result.append(comb)
    result.sort(key=lambda x: sum(x))
    print(f"\n\nBased on the information provided, here are all the possible score combinations for you, sorted in increasing order:")
    time.sleep(5)
    print(f"\n\n{result}\n\n{len(result)} combinations in total.")

toefl_combinations(int(input("\n\nType your minimum target TOEFL Score (0 to 120): ")), int(input("\n\nType the minimum required score per section (0 to 30): ")))
