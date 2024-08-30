# 2 задание

import sys
import math


def calculate_position(xc, yc, r, x, y):
    distance_squared = (x - xc) ** 2 + (y - yc) ** 2
    r_squared = r ** 2

    if math.isclose(distance_squared, r_squared):
        return 0
    elif distance_squared < r_squared:
        return 1
    else:
        return 2


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        with open(circle_file, 'r') as file:
            circle_data = file.readline().strip().split()

            if len(circle_data) != 3:
                sys.exit(1)

            xc, yc, r = map(float, circle_data)

        with open(points_file, 'r') as file:
            points_data = file.readlines()
            points = [tuple(map(float, line.strip().split())) for line in points_data]

        for point in points:
            x, y = point
            result = calculate_position(xc, yc, r, x, y)
            print(result)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)