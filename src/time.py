import time
import matplotlib.pyplot as plt
from random import choice
import random
from sa import search_array
import math


def time_data(length):
    """Function that generates DNA sequences and patterns used 
       to calculate the running time for bulding a suffix array 
       using a suffix tree build on the naive approach.

    Args:
        length (int): The length of the longest sequence generated.

    Returns:
        Two lists, n and t: 
                    n is a list of the pattern length times the sequence length.
                    t is a list of the running times.
    """    
    n = []
    t = []
    y = []
    bases = ['a','t','g','c']

    for i in range(10, length):
        sequence = ''.join([choice(bases) for j in range(i)])
        start = random.randint(0, i - round(i/10))
        pattern = sequence[start:(start + round(i/10))]
        
        t0 = time.time()
        search_array(sequence, pattern)
        t1 = time.time()

        total = t1 - t0
       
        n.append(round(i/10) * i)
        t.append(total)
        y.append(round(i/10) * math.log(i))
        time.sleep(0.05)
    
    return n,t


n,t = time_data(1000)

fig, ax = plt.subplots()
ax.scatter(n, t)
ax.set_title('Time complexity')
ax.set_ylabel('Time (s)')
ax.set_xlabel('Length of sequence times pattern (n * m)')
plt.savefig('time.png')


x = []
y = []
for i in range(10,1000):
    x.append(i)
    y.append(math.log(i))


fig, ax = plt.subplots()
ax.scatter(n, y)
ax.set_title('Time complexity')
ax.set_ylabel('Time (s)')
ax.set_xlabel('Length of sequence times pattern (n * m)')
plt.savefig('log.png')

    