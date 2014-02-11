
def style_pass(line, indentation, comment):
    if line.endswith(':'):
        return 1
    elif line == 'pass':
        return -1
    else:
        return 0

def style_curly(line, indentation, comment):
    if comment == '#{':
        return 1
    elif comment == '#}':
        return -1
    else:
        return 0

styles = {
        0 : style_pass,
        1 : style_curly
}
