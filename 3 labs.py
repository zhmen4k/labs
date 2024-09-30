def reverse_exercise(list_: list[int]) -> None:
    left = 0
    right = len(list_) - 1

    while left < right:
        list_[left], list_[right] = list_[right], list_[left]
        left += 1
        right -= 1


list_ = [1, 5, 10, 2]
print("Оригінальний список:", list_)

reverse_exercise(list_)
print("Перевернутий список:", list_)

# Перевірка за допомогою assert
assert list_ == [2, 10, 5, 1]
print("Тест пройдено успішно!")

def get_numbers_in_between(a: list[int], b: list[int]) -> list[int]:
    result = []
    for i in range(max(a), min(b) + 1):
        for j in a:
            if i % j != 0:
                break
        else:
            for k in b:
                if k % i != 0:
                    break
            else:
                result.append(i)
    return result

print(get_numbers_in_between([2, 4], [32, 16, 96]))
print(get_numbers_in_between([6, 2], [24, 36]))
print(get_numbers_in_between([3, 4], [24, 48]))