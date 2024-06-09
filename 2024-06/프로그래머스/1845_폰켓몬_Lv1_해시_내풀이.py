def solution(nums):
    max_pick = len(nums) / 2
    set_nums = set(nums)
    if max_pick > len(set_nums) :
        return len(set_nums)
    else:
        return max_pick
