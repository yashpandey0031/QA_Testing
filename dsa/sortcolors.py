def sort_colors(nums):
    """
    Sorts an array containing 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.
    
    Args:
    nums (List[int]): The input list containing 0s, 1s, and 2s.
    
    Returns:
    None: The input list is sorted in-place.
    """
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers (0s, 1s, and 2s) separated by spaces: ").split()))
    sort_colors(nums)
    print("Sorted colors:", nums)