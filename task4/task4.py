import sys
def min_moves_to_equal_elements(nums):
    nums.sort()

    median = nums[len(nums) // 2]

    return sum(abs(num - median) for num in nums)


# nums = [1, 10, 2, 9]

with open(sys.argv[1]) as file:
    nums = list(map(int, file))

result = min_moves_to_equal_elements(nums)
print(f"Минимальное количество ходов: {result}")