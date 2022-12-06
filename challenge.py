import math

points = []
constellation = []


def calculateDistance(arr1, arr2):
    """
        BOTH ARRAYS MUST HAVE FOUR ELEMENTS
    """
    getX = (arr1[0] - arr2[0])**2
    getY = (arr1[1] - arr2[1])**2
    getZ = (arr1[2] - arr2[2])**2
    getV = (arr1[3] - arr2[3])**2
    return math.sqrt(getX + getY + getZ + getV)


def merge(x, y, inCommon):
    del constellation[x][inCommon]
    constellation[x] += constellation[y]
    del constellation[y]
    return constellation[x]


def compare(x, y):
    """
        X AND Y MUST BE INTEGERS REPRESENTING INDECES OF CONSTELLATIONS
    """
    for z in range(len(constellation[x])):
        for a in range(len(constellation[y])):
            print(a, constellation[y][a])
            if constellation[x][z] == constellation[y][a]:
                print("Merge")
                merge(x, y, z)
                return


def main():

    with open("challenge.txt") as f:
        content = f.read().split("\n")
        print("Parsing Data: ")

        for line in content:
            points.append([int(i) for i in line.split(",")])

    print("Done! Making initial constellations...")
    # go through the first element in the array--find all points that are less than 3 away
    for i in range(len(points)):
        constellation.append([])
        for j in range(i+1, len(points) - 1):
            if(calculateDistance(points[i], points[j]) <= 3):
                constellation[i].append(points[j])

    print("Done! Finding Duplicates...")
    # compare all the list and find duplicate points
    for i in range(1, len(constellation)):
        for j in range(0, i-1):
            compare(i, j)
            for i in range(len(constellation)):
                if i == []:
                    del constellation[i]
            break
        print(constellation[i])

if __name__ == "__main__":
    main()
