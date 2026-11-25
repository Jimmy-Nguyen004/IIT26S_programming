def calc_sum(PValues: list[float]) -> float:
    total = 0.0
    for value in PValues:
        total += value
    return round(total, 1)

def calc_average(PValues: list[float]) -> float:
    total = 0.0
    for value in PValues:
        total += value
    return round(total / len(PValues), 1)