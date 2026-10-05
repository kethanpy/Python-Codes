# 1.	Task Scheduling Problem
# Write an asyncio program where two API calls take different times to complete. Use asyncio.create_task() so both start immediately, and print which task finishes first. 
# 2.	Sequential vs Concurrent Execution Problem
# Create three coroutines that each take 2 seconds. First run them using normal await, then run them using asyncio.gather(). Compare total execution time. 
# 3.	Gather with Errors Problem
# Build three async tasks: two return data successfully and one raises an exception. Use asyncio.gather(..., return_exceptions=True) to collect all results without stopping the program. 
# 4.	Wait with Timeout Problem
# Create three tasks simulating file downloads: 1 sec, 3 sec, and 5 sec. Use asyncio.wait() with a timeout of 2 seconds. Print completed downloads and cancel pending ones. 
# 5.	Process Results as They Complete Problem
# Simulate three web requests with different delays. Use asyncio.as_completed() to process each response immediately when it finishes instead of waiting for all. 
# 6.	Timeout Protection Problem
# Write a coroutine that simulates a slow database query. Use asyncio.wait_for() to cancel it if it takes more than 2 seconds, and print "Database timeout". 
# 7.	Cancellation Problem
# Create a long-running background task like sending email notifications. Cancel it after 2 seconds and handle asyncio.CancelledError properly. 
# 8.	Callback Problem
# Create an async task that returns a calculated value. Attach a callback using add_done_callback() to print the result as soon as the task is completed. 
# 9.	Lock Synchronization Problem
# Create three coroutines trying to update the same shared account balance. Use asyncio.Lock() so only one coroutine updates the balance at a time. 
# 10.	Producer–Consumer Queue Problem
# Build an async producer that adds 10 jobs into an asyncio.Queue, and two consumers that process the jobs concurrently. Use queue.join() and cancel consumers after all jobs are done.


######### 1 ######

# 1.	Task Scheduling Problem
# Write an asyncio program where two API calls take different times to complete.
# Use asyncio.create_task() so both start immediately, 
# and print which task finishes first.

# import asyncio  # method edi
# async def api_call_1(): # async anedi co_rotine 
#     print("API call 1 started")
#     await asyncio.sleep(2) # await ane agu ani cheputhadi asyncio.sleep ane method use chesi aputham anthe
#     print("API call 1 completed")
#     return "API 1 result"
# async def api_call_2():
#     print("API call 2 started")
#     await asyncio.sleep(5)
#     print("API call 2 complede")
#     return "API 2 result"

# async def main():
#     task1=asyncio.create_task(api_call_1())
#     task2=asyncio.create_task(api_call_2())
#     print("both api calls started....")
    
#     done,pending=await asyncio.wait(
#         [task1,task2], # task pendi unda complete inda ani edi cheputhadi
#         return_when= asyncio.FIRST_COMPLETED
#         )   
#     for task in done :
#         print("\nFIrst completed:",task.result())
    
#     for task in pending:
#         result=await task # pending lo unna task kuda complte aye varaku untadi
#         print("Remaining task completed:",result)
        
# asyncio.run(main())
#============================================================================

# 2.Sequential vs Concurrent Execution Problem
# Create three coroutines that each take 2 seconds. 
# First run them using normal await, then run them using asyncio.gather().
# Compare total execution time. 

# import asyncio
# import time
# async def task(name):
#     print(f"{name} started")
#     await asyncio.sleep(2)
#     print(f"{name}finished")
    
# async def sequential():
#     print("\nconcurrent Execution")
#     start=time.time()
    
#     await task("task 1")
#     await task("task 2")
#     await task("task 3")
#     print("time:",round(time.time()- start,2),"seconds")
    
# async  def concurrent():
#     print("\n concurrent Execution")
#     start=time.time()
    
#     await asyncio .gather(
#         task("task 1"),
#         task("task 2"),
#         task("task 3"),
#     )
#     print("time",round(time.time()-start,2),"seconds")
    
# async def main():
    
#     await sequential()
#     await concurrent()
# asyncio.run(main())

# =========================

# 3.	Gather with Errors Problem
# Build three async tasks: two return data successfully and one raises an exception.
# Use asyncio.gather(..., return_exceptions=True) to collect all results without stopping the program. 

#######
# gather ane error problem kavali and mudu async task kavli two return kavali
# okadinki raises valueError kavli 
#method ni oka result lo unchukoni asyncio.gather ni use cheyali andulo return_exceptions=True vadal
# async def main ane function lo call cheyali last asyncio.run(main()) call chestene run avuthadi 
# ledu ante kadu

# import asyncio # manam asyncio ni thisukuntam import chesukuntam

# async def task1(): # corotine ni create chesukunnam
#     await asyncio.sleep(2) # mana estam edi co rotine asyncion.sleep vadachu 
#     return "Data from Task 1" # return cheyadam valla use chestam
# async def task2():
#     await asyncio.sleep(1)
#     return "Data from task2"
# async def task3():
#     await asyncio.sleep(3)
#     raise ValueError("something went wrong")
# async def main():
#     result= await asyncio.gather(
#         task1(),
#         task2(),
#         task3(),
#         return_exceptions=True
#     )
#     print(result)
# asyncio.run(main())
#=================================================================================
# 4.	Wait with Timeout Problem
# Create three tasks simulating file downloads: 1 sec, 3 sec, and 5 sec.
# Use asyncio.wait() with a timeout of 2 seconds.
# Print completed downloads and cancel pending ones. 
# import asyncio
# # File download coroutine
# async def download(file_name, delay):
#     print(f"{file_name} download started")
#     await asyncio.sleep(delay)
#     print(f"{file_name} download completed")
#     return file_name
# async def main():
#     # Create tasks
#     t1 = asyncio.create_task(download("File-1", 1))  # manam pampe parameter file name and time 
#     t2 = asyncio.create_task(download("File-2", 3)) # manam pampe parameter file name and time 
#     t3 = asyncio.create_task(download("File-3", 5)) # manam pampe parameter file name and time
#     # Wait only for 2 seconds
#     done, pending = await asyncio.wait(
#         [t1, t2, t3],
#         timeout=2
#     )
#     print("\nCompleted Downloads:")
#     for task in done:
#         print(task.result())
#     print("\nCancelling Pending Downloads:")
#     for task in pending:
#         print(task.get_name(), "cancelled")
#         task.cancel()
#     # Pending tasks cancel complete అవ్వడానికి wait చేయడం
#     await asyncio.gather(*pending, return_exceptions=True)
# asyncio.run(main()) 



# 5.Process Results as They Complete Problem
# Simulate three web requests with different delays. 
# Use asyncio.as_completed() to process each response immediately when it finishes instead of waiting for all.

# import asyncio
# async def web_request(name, delay):
    
#     print(f"{name} Started") 
#     await asyncio.sleep(delay)
#     return f"{name} Response Received"
# async def main():
#     tasks = [
#         asyncio.create_task(web_request("Request-1",5)),
#         asyncio.create_task(web_request("Request-2",2)),
#         asyncio.create_task(web_request("Request-3",3))  # list of task lo store chesam avi use avuthavi
#     ]
#     print("\nProcessing Responses...\n")
#     for task in asyncio.as_completed(tasks):  # vatini for loop lo petti vadam 
#         result = await task
#         print(result)
# asyncio.run(main())


# 6.Timeout Protection Problem
# Write a coroutine that simulates a slow database query. 
# Use asyncio.wait_for() to cancel it if it takes more than 2 seconds,
# and print "Database timeout". 

# import asyncio
# async def database_query():
#     print("database query started")
#     await asyncio.sleep(5)
#     print("database query completed")
#     return "Employee data"
# async def main():
#     try:
#         result=await asyncio.wait_for(
#             database_query(),
#             timeout=2
#         )
#         print(result)
#     except asyncio.TimeoutError:
#         print("database timeout")
# asyncio.run(main())

# 7. Cancellation Problem #
# Create a long-running background task like sending email notifications.
# Cancel it after 2 seconds and handle asyncio.CancelledError properly.
    
# import asyncio
# async def send_emails():
#     try:
#         print("Email Sending Started")
#         await asyncio.sleep(1)
#     except asyncio.CancelledError:
#         print("Email Sending Cancelled")
#         raise
# async def main():
#     task = asyncio.create_task(send_emails())
#     await asyncio.sleep(2)
#     print("Cancelling Task...")
#     task.cancel()
#     try:
#         await task
#     except asyncio.CancelledError:
#         print("Task Cancelled Successfully")
# asyncio.run(main())

# # 8.	Callback Problem
# # Create an async task that returns a calculated value.
# # Attach a callback using add_done_callback()
# to print the result as soon as the task is completed. 
# import asyncio
# async def square(n):
#     await asyncio.sleep(2)
#     return n*n
# def show_result(task):
#     print("Square =", task.result())
# async def main():
#     task = asyncio.create_task(square(10))
#     task.add_done_callback(show_result) # show result ane function call cheyali
#     await task # task =.add_done_callback ni method ni call cheyali
# asyncio.run(main())

# # 9. Lock Synchronization Problem 
# # Create three coroutines trying to update the same shared account balance.
# # Use asyncio.Lock() so only one coroutine updates the balance at a time.
import asyncio
balance = 1000 
lock = asyncio.Lock()
async def deposit(name, amount):
    global balance
    async with lock:
        print(f"{name} Entered")
        temp = balance
        await asyncio.sleep(1)
        temp = temp + amount
        balance = temp
        print(f"{name} Updated Balance = {balance}")
async def main():
    await asyncio.gather(
        deposit("Person-1",100),
        deposit("Person-2",200),
        deposit("Person-3",300)
    )
    print("\nFinal Balance =", balance)
asyncio.run(main())


###############################
# 10.	Producer–Consumer Queue Problem
# Build an async producer that adds 10 jobs into an asyncio.Queue,
# and two consumers that process the jobs concurrently. 
# Use queue.join() and cancel consumers after all jobs are done.

import asyncio
async def producer(queue):
    for i in range(1, 11):
        print(f"Produced Job-{i}")
        await queue.put(f"Job-{i}")
    print("Producer Finished")
async def consumer(name, queue):
    while True:
        job = await queue.get()
        print(f"{name} Processing {job}")
        await asyncio.sleep(1)
        print(f"{name} Finished {job}")
        queue.task_done()
async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer1 = asyncio.create_task(consumer("Consumer-1", queue))
    consumer2 = asyncio.create_task(consumer("Consumer-2", queue))
    await producer_task
    await queue.join()
    consumer1.cancel()
    consumer2.cancel()
    print("All Jobs Completed")
asyncio.run(main())