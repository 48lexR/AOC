def main():
    instructions = open("inputs/Ten.txt").readlines()

    x = 1
    c = 0
    output = ""

    def pix(c, x): return "#" if abs(c - x) <= 1 else "."

    for instr in instructions:
        output += pix(c, x)
        c = (c + 1) % 40
        if instr.startswith("addx"):
            output += pix(c, x)
            c = (c + 1) % 40
            x += int(instr.split()[1])

    for row in range(0, 6):
        print(output[row*40:(row+1)*40])


if __name__ == "__main__":
    main()
