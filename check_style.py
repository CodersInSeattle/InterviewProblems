import logging
import os
import sys

import python_style_checker


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

LINTERS = [python_style_checker.PylintRunner(),
           python_style_checker.Pep8Runner()]

IGNORED_FILES = set()


def _should_check(module):
    module_name = os.path.basename(module)
    return module.endswith('.py') and module_name not in IGNORED_FILES


def _get_starting_directory(args):
    try:
        base_directory = args[1]
    except IndexError:
        base_directory = os.getcwd()
    return base_directory


def _run_linter(base_directory, linter):
    LOGGER.info('***************Running %s***************', linter.linter_name)
    for root, _, files in os.walk(base_directory):
        for name in files:
            file_path = os.path.join(root, name)
            if _should_check(file_path):
                LOGGER.info('Checking %s', file_path)
                linter.check_style(file_path)
            else:
                LOGGER.debug('Ignore %s', file_path)
    LOGGER.info('%s:\n\tPassed: %d;\n\tFailed: %d', linter.linter_name,
                linter.passed, linter.failed)


def main():
    base_directory = _get_starting_directory(sys.argv)
    LOGGER.debug('Inspecting in directory %s...', base_directory)
    for linter in LINTERS:
        _run_linter(base_directory, linter)

    if any(linter.failed > 0 for linter in LINTERS):
        sys.exit()


if __name__ == '__main__':
    main()
