import sys

def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))
    path = []
    current_index = 0

    while True:

        path.append(circular_array[current_index])
        
        current_index = (current_index + m - 1) % n
        
        if current_index == 0:
            break
    
    return path

if len(sys.argv) != 3:
    print("ошибка")
else:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = circular_array_path(n, m)
    print("полученный путь:", result)