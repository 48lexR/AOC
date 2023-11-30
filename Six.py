

def findRepeat(arr):
    for i in range(1, len(arr)):
        for j in range(0, i-1):
            print(arr[i], arr[j])
            if arr[i] == arr[j]:
                return True  # if there's a repeated element

    return False


def main():
    content = []
    chunk = ""
    chunkSize = 14
    iterator = chunkSize

    with open("./inputs/Six.txt") as f:
        content = f.read()

    for i in range(len(content)):
        chunk = content[i:i+chunkSize]
        chunk_set = set(chunk)
        if len(chunk) != len(chunk_set):
            print(chunk, " ", iterator)
            iterator += 1
        else:
            print(chunk, " ", iterator)
            break
    print(iterator)


if __name__ == "__main__":
    main()
