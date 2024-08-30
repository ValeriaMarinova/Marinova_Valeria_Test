def min_moves_to_equal_elements(nums):
    nums.sort()

    median = nums[len(nums) // 2]

    return sum(abs(num - median) for num in nums)


nums = [1, 2, 9, 2, 6]
result = min_moves_to_equal_elements(nums)
print(f"Минимальное количество ходов: {result}")