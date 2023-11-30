def main():
    j = 0
    with open("./inputs/One.txt") as f:
        numbers = f.read()
        nums = numbers.split("\n\n")
        totals = []
        for list in nums:
            total = 0
            list = list.split("\n")
            for i in list:
                total += int(i)
            totals.append(total)
        totals.sort(reverse=True)
        print(totals[0])
        print(sum(totals[0:3]))


if __name__ == "__main__":
    main()
