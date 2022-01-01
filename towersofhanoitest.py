def towersofhanoi(a, b, c, n):
    global movecount
    if n == 0:
        print('No more disks to move')
        return
    elif n == 1:
        movecount += 1
        print('Disk Moved from A -> C')
    else:
        towersofhanoi(a, c, b, n-1)
        movecount += 1
        print('Disk Moved from A -> B')
        towersofhanoi(a, b, c, n-1)


movecount = 0
towersofhanoi('A', 'B', 'C', 3)
print('total moves : {}'.format(movecount))
