import sys
from argparse import ArgumentParser
from pathlib import Path

from . import __description__ as desc


def entrypoint():
    parser = ArgumentParser(
        prog='msh',
        description=desc,
    )

    parser.add_argument(
        '--entry',
        required=True,
        type=Path,
    )

    parser.add_argument(
        '--output',
        type=Path,
        default='build.sh'
    )

    options = parser.parse_args(sys.argv[1:])

    if not options.entry.exists():
        sys.stdout.write('Please provide existing path\n')
