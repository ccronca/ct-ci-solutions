# Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom(i.e., each disk sits on top of an even larger one). You have the following
# constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using Stacks.


def moveDiscs(n, origin, destination, buffer):
    if n > 0:
        # move top n - 1 disks from origin to buffer, using destination as a buffer.
        moveDiscs(n-1, origin, buffer, destination)
        # move top from origin to destination
        moveTop(origin, destination)
        # move top n - 1 disks from buffer to destination, using origin as a buffer.
        moveDiscs(n-1, buffer, destination, origin)


def moveTop(origin, destination):
    top = origin.pop()
    destination.append(top)


towers = []
n = 4
for i in range(3):
    towers.append([])

for i in range(n - 1, -1, -1):
    towers[0].append(i)

moveDiscs(n, towers[0], towers[2], towers[1])

print(towers)
