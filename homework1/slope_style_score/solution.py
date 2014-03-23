def slope_style_score(scores):
    scores = sorted(scores)
    print(scores)
    result = []
    for i in range(1, len(scores) - 1):
        result.append(scores[i])
    sum_of_scores = sum(result)
    score = round(sum_of_scores / len(result), 2)
    return score


