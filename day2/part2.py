from day2.part1 import intcode

expectation = 19690720
noun = verb = [i for i in range(100)]


def reset_memory():
    f = open('input.txt', 'r')
    data = f.readlines()
    l = [int(e) for e in data[0].split(',')]
    f.close()
    return l


for n in noun:
    for v in verb:
        opcode = reset_memory()
        opcode[1] = n
        opcode[2] = v
        if intcode(opcode)[0] == expectation:
            print(100 * n + v)
