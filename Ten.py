def main():
    cycle = 1
    strengthMod = 1
    ans = []
    result = ""
    with open("inputs/Ten.txt") as f:
        content = f.read().split("\n")

    print()
    for x in content:
        x = x.split(" ")
        cycle += 1

        if cycle in [strengthMod-1, strengthMod, strengthMod+1]:
            result += '#'
        else:
            result += "."

        if cycle in [20, 60, 100, 140, 180, 220]:
            val = cycle * strengthMod
            ans.append(val)

        if x[0] == "noop":
            pass
        elif x[0] == "addx":
            strengthMod += int(x[1])
            cycle += 1

        if cycle in [20, 60, 100, 140, 180, 220]:
            val = cycle * strengthMod
            ans.append(val)
    # print(ans)
    # print(sum(set(ans)))
    for inx, char in enumerate(result):
        print(char)
        if inx % 39 == 0:
            print()


if __name__ == "__main__":
    main()
