def calculate_average(scores):
    total = 0
    for score in scores:
        if isinstance(score, int):
            total += score
    average = total / len(scores)
    return average

# Revised Version
def calculate_average2(scores):
    try:
        total = 0
        numLen = 0
        for score in scores:
            if isinstance(score, int):
                total += score
                numLen += 1
        average = total / numLen
        return average
    except ZeroDivisionError:
        return "Error: No valid scores to calculate average!"

grades = [80, 90, 100, "A"]
print("Average grade:", calculate_average(grades))
