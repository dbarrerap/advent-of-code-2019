def intcode(l):
    for i in range(0, len(l), 4):
        if l[i] == 1:
            l[l[i + 3]] = l[l[i + 1] ]+ l[l[i + 2]]
        elif l[i] == 2:
            l[l[i + 3]] = l[l[i + 1]] * l[l[i + 2]]
        elif l[i] == 99:
            return l
        else:
            raise ValueError


if __name__ == '__main__':
    f = open('input.txt', 'r')
    st = f.readlines()
    opcode = [int(e) for e in st[0].split(',')]
    f.close()

    print(intcode(opcode))
