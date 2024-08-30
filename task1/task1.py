# 1 задание
def circular_array_path(n, m):
    path = []
    current_position = 0

    while True:
        path.append(current_position + 1)

        current_position = (current_position + m) % n

        if current_position == 0:
            break

    return path

n = int(input("Введите n: "))
m = int(input("Введите m: "))

result = circular_array_path(n, m)

print("".join(map(str, result)))