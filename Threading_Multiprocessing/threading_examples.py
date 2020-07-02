import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print('Sleeping for %.2f second(s)..'%seconds)
    time.sleep(seconds)
    #print('Done Sleeping..') replace with return for use with CONCURRENT
    return('Done Sleeping in %.2f second(s)..' %seconds)
#first we will try the normal method
#do_something()
#do_something()

#############################################################################
#now we will use threading
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# #Now to wait for above processes to END we use .join() so that once the abpve processes have finished only
# #then may the program proceed to the next line of code. This is done so we may be able to calculate the time basically
# #to know more, comment the two joins below to find out what happens.

# t1.join()
# t2.join()

#We can also use a for loop to do above 10 times,

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args = [1.5]) #arguments to a function are given in a list to the thread.
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

########################################################

#And now we will use the most advanced method of the above using concurrent.futures.
#concurrent.futures.Executor() as
with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)

    # print(f1.result())
    # print(f1.result())
    
    #we can also use list comprehension or even mapping to get a for loop type of thing going on,
    secs = [5, 4, 3, 2, 1]

    # results = [executor.submit(do_something, 1) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    #Now mapping to another list containing our arguments.

    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)



finish = time.perf_counter()

print()
print('Finished in %.2f second(s)'%(finish - start))