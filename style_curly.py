def indent_change(line, indentation, comment):
    if comment == '#{':
        return 1
    elif comment == '#}':
        return -1
    else:
        return 0

