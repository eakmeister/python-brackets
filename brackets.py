import imp
import os
import styles
import sys

class Finder:
    def __init__(self, style):
        self.style = style

    def find_module(self, fullname, path = None):
        filename = fullname + '.pyb'
        
        if os.path.exists(filename):
            return Loader(self.style)

class Loader:
    def __init__(self, style):
        self.indent_change = styles.styles[style]

    def load_module(self, fullname):
        indented_lines = []
        indentation = 0
        filename = fullname + '.pyb'

        with open(filename) as f:
            for line in f:
                if '#' in line:
                    comment = line[line.find('#'):]
                    line = line[:line.find('#')].strip()
                else:
                    comment = ''
                    line = line.strip()

                change = self.indent_change(line, 0, comment)

                if change < 0:
                    indentation += change

                indented_lines.append('    ' * indentation + line)

                if change > 0:
                    indentation += change

        module = imp.new_module(fullname)
        exec('\n'.join(indented_lines), module.__dict__)
        return module

def enable(style = 0):
    sys.meta_path.append(Finder(style))
