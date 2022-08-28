def read_last(lines, file):
    all_lines = []
    with open(file, 'r') as fp:
        line = fp.readline()
        while line:
            line = line.rstrip('\n')
            all_lines.append(line)
            line = fp.readline()
    return all_lines[-1:- lines - 1:-1]