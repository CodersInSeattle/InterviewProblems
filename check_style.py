import os
import subprocess
import sys


class ImproperStyleError(Exception):
    pass


class PythonStyleChecker(object):
    def __init__(self, linter_name):
        self.passed = 0
        self.failed = set()
        self._linter_name = linter_name

    @property
    def linter_name(self):
        return self._linter_name

    def check_style(self, module):
        raise NotImplementedError


class PylintRunner(PythonStyleChecker):

    def __init__(self):
        super(PylintRunner, self).__init__('pylint')

    def check_style(self, module):
        '''Runs pylint on a Python module.'''
        try:
            subprocess.check_output([self.linter_name, module])
            self.passed += 1
        except subprocess.CalledProcessError:
            self.failed.add(os.path.relpath(module))


class Pep8Runner(PythonStyleChecker):

    def __init__(self):
        super(Pep8Runner, self).__init__('pep8')

    def check_style(self, module):
        '''Runs pep8 on a Python module.'''
        try:
            subprocess.check_output([self.linter_name, module])
            self.passed += 1
        except subprocess.CalledProcessError:
            self.failed.add(os.path.relpath(module))


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
    for linter in [PylintRunner(), Pep8Runner()]:
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
