import numpy as np
with open('inputs/Nine.txt', 'r') as f:
    lines = f.readlines()


class Head():
    def __init__(self, position=[0, 0]):
        self.position = np.array(position)

    def update(self, instruction):
        commands = {'L': (0, -1), 'R': (0, 1), 'U': (1, 1), 'D': (1, -1)}
        index, increment = commands[instruction]
        self.position[index] += increment


class Tail():
    def __init__(self, position=[0, 0]):
        self.position = np.array(position)
        self.visited = set([(position[0], position[1])])

    def update(self, head):
        heading = np.array([head.position[0]-self.position[0],
                           head.position[1]-self.position[1]])
        distance = np.linalg.norm(heading)
        movement = np.array([0, 0])
        if (distance >= 2):
            if heading[0] == 0:
                movement = np.array(
                    [0, heading[1]/abs(heading[1])], dtype='int')
            elif heading[1] == 0:
                movement = np.array(
                    [heading[0]/abs(heading[0]), 0], dtype='int')
            else:
                movement = np.array(
                    [heading[0]/abs(heading[0]), heading[1]/abs(heading[1])], dtype='int')
        self.position += movement
        self.visited.add((self.position[0], self.position[1]))


# Part 1
h = Head()
t = Tail()
for l in lines:
    direction, steps = l.split()
    for i in range(int(steps)):
        h.update(direction)
        t.update(h)
print(len(t.visited))

h = Head()
rope = []
for k in range(9):
    rope.append(Tail())
for l in lines:
    direction, steps = l.split()
    for s in range(int(steps)):
        h.update(direction)
        rope[0].update(h)
        for t in range(1, len(rope)):
            rope[t].update(rope[t-1])
print(len(rope[-1].visited))
