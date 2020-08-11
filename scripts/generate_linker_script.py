#!/usr/bin/env python3

import argparse
import os
from string import Template

TEMPLATE = Template('''
{

local:
  $local_symbols_declaration

};
''')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="output", help="Output file")
    parser.add_argument(dest="symbols", help="The list of symbols")
    options = parser.parse_args()
    global_symbols = []
    local_symbols = []
    local_symbols = options.symbols.split(':')

    with open(options.output, "w") as f:
        f.write(TEMPLATE.substitute({

            'local_symbols_declaration': '\t' + ';\n\t '.join(local_symbols) + ';',
            }))
