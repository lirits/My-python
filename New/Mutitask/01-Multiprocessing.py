import multiprocessing
import threading
import time
import os
def dancing():
    print('Dancing_ID：',os.getpid())
    print('Process_name',multiprocessing.current_process())
    print('Dancing_PID：',os.getppid())
    for i in range(5):
        print('Dancing..')
        time.sleep(0.2)

def sing(name):
    print('SingID：',os.getpid())
    print('SingPID：',os.getppid())
    print(f'{name} sing now')
if __name__ == '__main__':
    print('Main_pid:',os.getpid())
    Dance = multiprocessing.Process(target=dancing)
    Sing = multiprocessing.Process(target=sing,kwargs={'name':'lirit'})
    Dance.start()
    Sing.start()