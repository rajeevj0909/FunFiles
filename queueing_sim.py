import random as r
from matplotlib import pyplot, style
import numpy as np

'''
    Challenge:
        - Create a queueing simulator
        - Generate queueing data for 200 people
        - Assume every second there is a 1/20 chance of someone joining the back of the queue
        - Assume every second there is a 1/20 chance of the person at the front leaving the queue

        - Plot the wait time for each customer
        - Plot the queue length at each point in time
        - What else can you plot?
        - What happens when you change the probabilities?

    author: github.com/jupilogy
'''

# Set initial timestep to 0
t = 0

# Set number of people served to 0
p = 0

# Let's track these things to plot at the end
wait_times = np.array([])
size_of_queue = []
max_wait_time = []

# Store length of queue as integer
queue = 0

while p < 200:
    if r.choice([False] * 19 + [True]):
        # Add someone to the queue, start timing their wait
        queue += 1
        wait_times = np.append(wait_times, [0])

    if r.choice([False] * 19 + [True]):
        if queue != 0:
            # Mark extra person as served
            # Remove person from queue
            p += 1
            queue -= 1

    # Update our datas
    size_of_queue.append(queue)
    try:
        max_wait_time.append(max(wait_times[p:]))
    except:
        max_wait_time.append(0)
    wait_times[p:] += 1

# Cut excess values (people who were never served) from wait_times
wait_times = wait_times[:200]

# Plot wait_times
style.use('seaborn')
pyplot.figure()
pyplot.title('wait times for each customer')
pyplot.xlabel('Customer no.')
pyplot.ylabel('queue time')
pyplot.plot(wait_times)

style.use('dark_background')
pyplot.figure()
pyplot.title('length of queue over time')
pyplot.xlabel('Time')
pyplot.ylabel('Length of queue')
pyplot.scatter(range(len(size_of_queue)), size_of_queue, marker="x")

style.use('_classic_test')
pyplot.figure()
pyplot.title('maximum time waiting for any person in queue')
pyplot.xlabel('Time')
pyplot.ylabel('max amount of time someone was waiting in the queue')
pyplot.plot(max_wait_time)

pyplot.show()
