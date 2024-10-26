def process_scores(scores: list[tuple[str, int]]) -> dict[str, int]:

    if not scores:
        return {}

    average_score = sum(score for _, score in scores) / len(scores)

    above_average = {name: score for name, score in scores if score > average_score}

    sorted_above_average = dict(sorted(above_average.items(), key=lambda item: item[1], reverse=True))
    print(sorted_above_average)

    return sorted_above_average
