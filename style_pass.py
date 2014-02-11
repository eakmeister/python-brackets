def indent_change(line, indentation, comment):
    if line.endswith(':'):
        return 1
    elif line == 'pass':
        return -1
    else:
        return 0

