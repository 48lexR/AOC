def main():
    content = []
    pairs = []
    numbers = []
    total = []
    ans1 = 0
    ans2 = 0
    with open("./inputs/Four.txt") as f:
        content = f.read().split("\n")
        pairs = [pair.split(",") for pair in content]
        for numbers in pairs:
            for i in numbers:
                i = [int(j) for j in i.split("-")]
                total.append(i)

        for i in range(0, len(total), 2):
            # check which array is contained in other array
            if((total[i][0] >= total[i+1][0]) and (total[i][1] <= total[i+1][1]) or (total[i][0] <= total[i+1][0]) and (total[i][1] >= total[i+1][1])):
                ans1 += 1

            # check if array overlaps with other array
            # an array will overlap if the max of one is greater than the min of the other, or if the min of one is less than the max of the other
            if((total[i][1] >= total[i+1][0]) and (total[i+1][1] >= total[i][0])):
                ans2 += 1

        print(ans1, ans2)


if __name__ == "__main__":
    main()
