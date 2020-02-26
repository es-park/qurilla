def best_stock(a):
    val = list(a.values())
    for i, j in a.items():
        if j == max(val):
            answer = i
    return answer