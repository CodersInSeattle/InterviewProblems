import os
import Queue
import sys
import threading

import check_style


class WorkerThread(threading.Thread):

    def __init__(self, dir_q, result_q):
        super(WorkerThread, self).__init__()
        self.dir_q = dir_q
        self.result_q = result_q
        self.stoprequest = threading.Event()

    def run(self):
        while not self.stoprequest.isSet():
            try:
                dirname = self.dir_q.get(True, 0.05)
                filenames = check_style.run_linters(dirname)
                self.result_q.put((self.name, dirname, filenames))
            except Queue.Empty:
                continue

    def join(self, timeout=None):
        self.stoprequest.set()
        super(WorkerThread, self).join(timeout)


def main(args):
    dir_q = Queue.Queue()
    result_q = Queue.Queue()

    pool = [WorkerThread(dir_q=dir_q, result_q=result_q) for _ in range(4)]

    for thread in pool:
        thread.start()

    work_count = 0
    for dirname in os.listdir(args):
        if os.path.isdir(dirname) and not dirname.startswith('.'):
            work_count += 1
            dir_q.put(dirname)

    print 'Assigned %s dirs to workers' % work_count

    while work_count > 0:
        thread_name, dirname, filenames = result_q.get()
        print 'From thread %s: %s files found in dir %s' % (
            thread_name, len(filenames), dirname)
        work_count -= 1

    for thread in pool:
        thread.join()


if __name__ == '__main__':
    main(sys.argv[1])
