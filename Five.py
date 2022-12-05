stack1 = ["WBGZRDCV",
          "VTSBCFWG",
          "WNSBC",
          "PCVJNMGQ",
          "BHDFLST",
          "NMWTVJ",
          "GTSCLFP",
          "ZDB",
          "WZNM"]

stack2 = ["WBGZRDCV",
          "VTSBCFWG",
          "WNSBC",
          "PCVJNMGQ",
          "BHDFLST",
          "NMWTVJ",
          "GTSCLFP",
          "ZDB",
          "WZNM"]

stack1 = [list(arr[::-1]) for arr in stack1]
stack2 = [list(arr[::-1]) for arr in stack2]


def move1(amount, of, to):
    of = of-1
    to = to-1
    for i in range(amount):
        stack1[to].append(stack1[of].pop())


def move2(amount, of, to):
    of = of-1
    to = to-1
    stack2[to] += stack2[of][-amount:]
    stack2[of] = stack2[of][:-amount]


def main():
    with open("Five.txt") as f:
        content = f.read().split("\n")
        for message in content:
            message = message.split(" ")
            move1(int(message[1]), int(message[3]), int(message[5]))
            move2(int(message[1]), int(message[3]), int(message[5]))
    for s in stack1:
        print(s[-1], end="")
    print("")
    for s in stack2:
        print(s[-1], end="")


if __name__ == "__main__":
    main()
