def main():
    RPS = {
        "A X": 3,  # rock scissors
        "A Y": 4,  # rock rock
        "A Z": 8,  # rock paper
        "B X": 1,  # paper rock
        "B Y": 5,  # paper paper
        "B Z": 9,  # paper scissors
        "C X": 2,  # scissors rock
        "C Y": 6,  # scissors paper
        "C Z": 7
    }
    total = []
    with open("./inputs/Two.txt") as f:
        text = f.read()
        text = text.split("\n")
        for line in text:
            line.split(" ")
            total.append(RPS[line])

    print(sum(total))


if __name__ == "__main__":
    main()
