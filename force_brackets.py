"""
Scans the previous frame, and raises a SyntaxError if it finds any indented
blocks not ending with "pass".
"""
import inspect
import styles

def get_indent(line):
    spaces = 0

    for c in line:
        if c == ' ':
            spaces += 1
        elif c == '\t':
            spaces += 4
        else:
            break

    return spaces / 4

def raise_exception(last_line, line_no, file_name):
    e = SyntaxError()
    e.filename = file_name
    e.lineno = line_no + 1
    e.msg = 'Bracket error'
    e.text = last_line
    raise e

def enable(style = 0):
    indent_change = styles.styles[style]

    # get the previous stack frame
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    source = inspect.getsourcelines(module)[0]

    # target will be None if this is called from a python shell, for example
    expected_indent = get_indent(source[0])

    for line_no, line in enumerate(source):
        if line.strip() == '':
            continue

        indent = get_indent(line)
        line = line.strip()

        if '#' in line:
            comment = line[line.find('#'):]
            line = line[:line.find('#')].strip()
        else:
            comment = ''

        change = indent_change(line, indent, comment)

        if (change < 0 and not indent in (expected_indent, expected_indent + change)) \
                or (change >= 0 and indent != expected_indent):
            raise_exception(line, line_no, frame[1])

        expected_indent += change
    
    if expected_indent != 0:
        raise_exception(source[-1], line_no, frame[1])

