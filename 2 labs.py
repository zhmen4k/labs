def returned_idx(temp: list[int]) -> int:
    for pivot in range(len(temp)):
        left_moment = sum(temp[i] * (pivot - i) for i in range(pivot))
        right_moment = sum(temp[i] * (i - pivot) for i in range(pivot + 1, len(temp)))
        if left_moment == right_moment:
            return pivot
    return -1
def main():
    print(returned_idx([6, 6, 9]))
    print(returned_idx([43, 51, 35, 4]))
    print(returned_idx([19, 25, 5, 42, 38, 8, 34, 16, 14, 8, 47, 42, 4, 20, 23]))
    print(returned_idx([7, 24, 3, 38]))
    pass
if __name__ == '__main__':
    main()