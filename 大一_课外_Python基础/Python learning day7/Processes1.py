#---------------------------------------Processes and Threads 1----------------------------------------------#
#Multiprocessing
from multiprocessing import Process
import os
def run_proc(name):
    print('Child process %s is running (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

#Pool
from multiprocessing import Pool
import time, random
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    print('Task %s runs %0.2f seconds...' % (name, end - start))

if __name__ == '__main__' :
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocessed done..')
    p.close()
    p.join()
    print('All works done...')
