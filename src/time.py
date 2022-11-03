import time
import matplotlib.pyplot as plt
from random import choice
import random
from sa import *
from tree import *


def search_array_2(x, p, SA):
    '''Pattern matching function using a suffix array 
    Return the occurences of p in x'''
    sa = SA
    x += '$'
    start = 0
    end = len(x)
    occ = []
    if len(p)==0 or len(x)==1:
        return occ

    for i in range(len(p)):
        start, end = recursive_lower_bound(p, x, sa, start, end, i), recursive_upper_bound(p, x, sa, start, end, i)

    occ = [sa[i] for i in range(start, end)]
    
    return occ

def time_data1(length, bases):
    """Function that generates DNA sequences and patterns used 
       to calculate the running time 

    Args:
        length (int): The length of the longest sequence generated.

    Returns:
        Lists, n and t: 
                    n is a list of the sequence length.
                    The t lists are the running times.
    """    
    n = []
    t_construct_tree = []
    t_sort_tree = []
    t_construct_SA = []
    t_exact = []
    t_final = []

    for i in range(10, length):
        sequence = ''.join([choice(bases) for j in range(i)])
        start = random.randint(0, i - round(i/10))
        pattern = sequence[start:(start + round(i/10))]

        # Time to construct suffix tree
        t0_construct_tree = time.time()
        T = construct_tree(sequence)
        t1_construct_tree = time.time()
        total_construct_tree = t1_construct_tree - t0_construct_tree
       

        # Time for sorting the tree
        t0_sort_tree = time.time()
        ST = sorted_tree(T)
        t1_sort_tree = time.time()
        total_sort_tree = t1_sort_tree - t0_sort_tree

        # Time for construction of SA from sorted tree
        t0_construct_SA = time.time()
        SA = list(subtree_labels(ST[0]))
        t1_construct_SA = time.time()
        total_construct_SA = t1_construct_SA - t0_construct_SA

        # Time for exact search
        t0_exact = time.time()
        search_array_2(sequence, pattern, SA)
        t1_exact = time.time()
        total_exact = t1_exact - t0_exact

        # Time for function doing everything
        t0 = time.time()
        search_array(sequence, pattern)
        t1 = time.time()

        total = t1 - t0
        
        n.append(i)
        t_construct_tree.append(total_construct_tree)
        t_sort_tree.append(total_sort_tree)
        t_construct_SA.append(total_construct_SA)
        t_exact.append(total_exact)
        t_final.append(total)

        time.sleep(0.05)
    
    return n,t_construct_tree, t_sort_tree, t_construct_SA, t_exact, t_final

bases = ['a','t','g','c']
worst_case = ['a']

n, t1, t2, t3, t4, t5 = time_data1(1000, bases)
n1, t11, t21, t31, t41, t51 = time_data1(500, worst_case)

def plot_fig(n, t1, t2, t3, t4, t5, name, number):
    plt.figure(number)
    # Plotting all times simultaneously
    plt.scatter(n, t1, label='Build suffix tree')
    plt.scatter(n, t2, label='Sort tree')
    plt.scatter(n, t3, label='Get suffix array')
    plt.scatter(n, t4, label='Exact search')
    plt.scatter(n, t5, label='Final')

    # Naming figure, x-axis and y-axis
    plt.title('Time complexity')
    plt.ylabel('Time (s)')
    plt.xlabel('Size (n)')


    # Adding legends
    plt.legend()


    # Save figure in folder figs
    plt.savefig('/home/mathilde/Documents/Kandidat/GSA/Project/Project3/project-3-python-ms-world-wides/figs/{}.png'.format(name))

plot_fig(n, t1, t2, t3, t4, t5, 'time_random', 1)
plot_fig(n1, t11, t21, t31, t41, t51, 'time_worst_case', 2)