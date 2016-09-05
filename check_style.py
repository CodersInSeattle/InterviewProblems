import os
import sys

import python_style_checker


class ImproperStyleError(Exception):
    pass


LINTERS = [python_style_checker.PylintRunner(),
           python_style_checker.Pep8Runner()]


def _get_starting_directory(args):
    try:
        base_directory = args[1]
    except IndexError:
        base_directory = os.getcwd()
    return base_directory


def _run_linter(base_directory, linter):
    for root, _, files in os.walk(base_directory):
        for name in files:
            file_path = os.path.join(root, name)
            if file_path.endswith('.py'):
                linter.check_style(file_path)
    return linter.failed


def run_linters(base_directory):
    failed_modules = set()
    for linter in LINTERS:
        failed = _run_linter(base_directory, linter)
        failed_modules.update(failed)
    return failed_modules


def main():
    base_directory = _get_starting_directory(sys.argv)

    failed_modules = run_linters(base_directory)

    if failed_modules:
        raise ImproperStyleError(
            'These modules failed style checking: {}'.format(failed_modules))


if __name__ == '__main__':
    main()
