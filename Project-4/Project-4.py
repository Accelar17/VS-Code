def remove_duplicates(nums):
    unique_nums = []
    count_dict = {}
    
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
        if count_dict[num] <= 2:
            unique_nums.append(num)
    
    return unique_nums


lists = [
    [1, 1, 2, 3, 3, 3, 5, 5, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 7]
]

for lst in lists:
    result = remove_duplicates(lst)
    print(result)
