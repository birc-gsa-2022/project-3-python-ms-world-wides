import argparse
from fasta_dict import fasta_func
from fastq_dict import fastq_func
from tree import construct_sorted_tree, subtree_labels

def construct_array(x):
    '''Return the suffix array of string x
    
    >>> construct_array('mississippi')
    [11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
    '''
    T = construct_sorted_tree(x)
    L = subtree_labels(T[0])

    return list(L)



def p_included(x, p, sa):
    start, end = 0, len(sa)-1
    m = len(p)
    
    while start!=end:
        print('included_loop')

        mid = (start+end)//2
        suffix = x[sa[mid]:sa[mid]+m]

        if p == suffix:
            return True, start, mid, end
        if p < suffix:
            end = mid
        else:
            start = mid+1

    return False, -1, -1, -1

def lower_bound(p, x, sa, start, end):
    m = len(p)
    mid = end
    suffix = x[sa[mid]:sa[mid]+m]
    previous_suffix = x[sa[mid-1]:sa[mid-1]+m]

    while previous_suffix == p or suffix != p: 
        print('lower_loop')
        
        if p <= previous_suffix:
            end = mid
        else:
            start = mid+1
        mid = (start+end)//2
        suffix = x[sa[mid]:sa[mid]+m]
        previous_suffix = x[sa[mid-1]:sa[mid-1]+m]
    return mid

def upper_bound(p, x, sa, start, end):
    m = len(p)
    mid = end
    suffix = x[sa[mid]:sa[mid]+m]
    previous_suffix = x[sa[mid-1]:sa[mid-1]+m]

    if suffix == p:
        return end+1

    while previous_suffix != p or suffix == p: 
        print('upper_loop')
        
        if p < previous_suffix:
            end = mid
        else:
            start = mid+1
        mid = (start+end)//2
        suffix = x[sa[mid]:sa[mid]+m]
        previous_suffix = x[sa[mid-1]:sa[mid-1]+m]
    return mid

def search_array(x, p):
    sa = construct_array(x)
    x += '$'
    occ = []
    if len(p)==0:
        return occ
    results = p_included(x, p, sa)
    if results[0]:
        [start, mid, end] = results[1:]
        start = lower_bound(p, x, sa, start, mid)
        end = upper_bound(p, x, sa, mid, end)
        occ = [sa[i] for i in range(start, end)]
    
    return occ


def array_runner(fasta_dict, fastq_dict):

    l = []
    for p_key, p_val in fastq_dict.items():
        for x_key, x_val in fasta_dict.items():
            matches = search_array(x_val, p_val)
            for i in matches:
                l.append('\t'.join([p_key, x_key, str(i), f'{str(len(p_val))}M', p_val]))
    
    return '\n'.join(l)

def main():
    
    argparser = argparse.ArgumentParser(
        description="Exact matching in linear time")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()

   #translate files into dicts
    fasta_dict = fasta_func(args.genome)
    fastq_dict = fastq_func(args.reads)

    print(search_array(fasta_dict, fastq_dict))



if __name__ == '__main__':
    main()
