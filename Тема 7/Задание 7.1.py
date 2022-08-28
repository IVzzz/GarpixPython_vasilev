def writePoem(path):
    lines = []
    with open(path, 'r') as fp:
        line = fp.readline()
        counter = 6
        while line and counter > 0:
            counter -= 1
            line = line.rstrip('\n')
            lines.append(line)
            line = fp.readline()
    return lines