import time
import concurrent.futures

#import multiprocessing

start = time.perf_counter()


def do_something(seconds):
    print('Sleeping for %.2f second(s)..'%seconds)
    time.sleep(seconds)
    #print('Done Sleeping for %.2f second(s)..'%seconds)
    #Use return for concurrent
    return('Done Sleeping for %.2f second(s)..'%seconds)


#Lets see a process that runs two times synchronously
# do_something()
# do_something()

#########################################################
#We can use multiprocessing module to split above two tasks so that each process is done
#using different cores

#We don't get much speed using threading on CPU bound processes
#But threading can improve IO bound tasks' speed

#Multiprocessing can improve both IO and CPU bound tasks.
##########################################################

#Multiprocesses run at the same time as opposed to threading.

#Lets look at some older ways to use Multiprocessing.

#lets turn both above functions into processes

# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# #We need to use start method to start the above processes

# p1.start()
# p2.start()

# #Also we need to use join method so that our script doesn't move forward before our processes are complete

# p1.join()
# p2.join()

#USING A FOR LOOP NOW

#processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args = [1.5])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()

#The above code doesn't work in Python 3.5.2

#############################################################
#Now we will use the newer method
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 1)
        # print(f1.result())
        # print(f2.result())
        #Using a for loop for 10 processes
        #Since I have 4 cores, 5, 4, 3, 2 will be executed first and then 1 will be executed once a core gets free
        secs = [5, 4, 3, 2, 1]
        
        #results = [executor.submit(do_something, sec) for sec in secs]

        #Now mapping our results to the seconds list,
        results = executor.map(do_something, secs)

        #for f in concurrent.futures.as_completed(results):
        for result in results:
            print(result)
            #print(f.result())
        
    #concurrent joins automatically.


#processes = []

finish = time.perf_counter()

print('Finished in %.2f second(s)..'%(finish-start))