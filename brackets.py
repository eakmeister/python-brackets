"""
Scans the previous frame, and raises a SyntaxError if it finds any indented
blocks not ending with "pass".
"""
import inspect

def get_indent(line):
    spaces = 0

    for c in line:
        if c == ' ':
            spaces += 1
        elif c == '\t':
            spaces += 4
        else:
            break

    return spaces

def raise_exception(last_line, line_no, file_name):
    e = SyntaxError()
    e.filename = file_name
    e.lineno = line_no + 1
    e.msg = 'Expected "pass" before end of indented block'
    e.text = last_line
    raise e

if __name__ == '__main__':
    print 'module not meant to be called direclty, import instead'
else:
    # get the previous stack frame
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    # If the import is at the module level, the target is the entire module,
    # otherwise get the funcion/class where the import occured.
    if frame[3] == '<module>':
        target = module
    else:
        target = getattr(module, frame[3])

    # target will be None if this is called from a python shell, for example
    if not target is None:
        source = inspect.getsourcelines(target)[0]
        last_line = None
        last_indent = 0

        for line_no, line in enumerate(source):
            if line.strip() == '':
                continue

            indent = get_indent(line)

            if indent < last_indent and not last_line.strip().startswith('pass'):
                raise_exception(last_line, line_no + 1, module.__file__)
            
            last_line = line
            last_indent = indent

        if last_indent > 0 and not last_line.strip().startswith('pass'):
            raise_exception(last_line, line_no + 1, module.__file__)
