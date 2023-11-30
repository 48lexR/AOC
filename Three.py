import math


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetDictionary = {}
    n = 1
    for letter in alphabet:
        alphabetDictionary[letter] = n
        n = n+1
    total = []
    total2 = []

    with open("./inputs/Three.txt") as f:
        puzzle = f.read().split("\n")  # split based on rucksack
        # for rucksack in puzzle:
        #     t = 0
        #     # split rucksack in half
        #     compartment1 = rucksack[:math.floor(len(rucksack)/2)]
        #     compartment2 = rucksack[math.floor(len(rucksack)/2):]
        #     # run repeats through dictionary
        #     for j in range(len(compartment1)):
        #         for k in range(len(compartment2)):
        #             if(compartment1[j] == compartment2[k] and t == 0):
        #                 t = t+1
        #                 total.append(alphabetDictionary[compartment1[j]])
        #                 break
        # print(f"Total 1 -> sum(total)")
        total2 = []
        for i in range(0, len(puzzle), 3):
            currentPuzzle = [puzzle[i], puzzle[i+1], puzzle[i+2]]
            t = 0
            for a in range(len(currentPuzzle[0])):
                for b in range(len(currentPuzzle[1])):
                    for c in range(len(currentPuzzle[2])):
                        if (currentPuzzle[0][a] == currentPuzzle[1][b] and currentPuzzle[0][a] == currentPuzzle[2][c] and t == 0):
                            t = t + 1
                            print(currentPuzzle[0][a])
                            total2.append(
                                alphabetDictionary[currentPuzzle[0][a]])
                            break
        print(sum(total2))


if __name__ == "__main__":
    main()
