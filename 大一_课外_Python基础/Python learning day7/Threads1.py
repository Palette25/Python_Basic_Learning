#-----------------------------------------------Multithreads-------------------------------------------------#
import time, threading
def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n<5:
        n += 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ends' % threading.current_thread().name)

    
print('Thread %s is running...'  % threading.current_thread().name)
#When begin, the current thread's name will be MainThread
t = threading.Thread(target=loop, name='loopThread')
#We use the thread function to start a subthread, and make its name as LoopThread, and run loop
#function in this thread
t.start()
t.join()
print('Thread %s ends' % threading.current_thread().name)

#Lock...only for global varible
#When we use different threads to change to value of one global varible, due to the random order
#of the running time of threads, we may get wrong answer, so we need to get a lock for every thread
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance += n
    balance  -= n
    
def run_thread(n):
    for i in range(100000):
        #get my lock
        lock.acquire()
        try:
            change_it(n)
        finally:
            # release my lock
            lock.release()

t1 = threading.Thread(target=run_thread, args=(4,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#Threadlocal
#When we truly use lock to change the varible correctly, we always find that it works slowly, so we
#get the Threadlocal to bind the correspondind varible for different threads sharing same name
local_school = threading.local()
def process_student():
    std = local_school.student
    print('Hello, Student %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
          local_school.student = name
          process_student()

t1 = threading.Thread(target=process_thread, args=('Clown', ), name='Thread1')
t2 = threading.Thread(target=process_thread, args=('SUN', ), name='Thread2')
t1.start()
t2.start()
t1.join()
t2.join()
