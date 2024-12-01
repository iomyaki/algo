def main() -> None:
    nums = []
    while True:
        try:
            nums.append(input())
        except EOFError:
            break

    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i):
            if nums[j + 1] + nums[j] > nums[j] + nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print("".join(nums))


if __name__ == "__main__":
    main()
