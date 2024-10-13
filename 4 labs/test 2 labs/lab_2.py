def weights_equilibrium(temp: list[int]) -> int:
    for pivot in range(len(temp)):
        left_moment = sum(temp[i] * (pivot - i) for i in range(pivot))
        right_moment = sum(temp[i] * (i - pivot) for i in range(pivot + 1, len(temp)))
        if left_moment == right_moment:
            return pivot
    return -1
