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

def recursive_lower_bound(p, x, sa, start, end, i_letter):
    '''Function recursive_lower_bound that takes a pattern p, string x, suffix 
    array sa of x, to recursively find a the lower bound of p[:i_letter] in sa'''

    if start == end:
        return start
    else:
        mid = (end+start)//2
        if p[i_letter] <= x[sa[mid]+i_letter]:
            end = mid
        else:
            start = mid+1
    
    return recursive_lower_bound(p, x, sa, start, end, i_letter)

def recursive_upper_bound(p, x, sa, start, end, i_letter):
    '''Function recursive_lower_bound that takes a pattern p, string x, suffix 
    array sa of x, to recursively find a the upper bound of p[:i_letter] in sa'''

    if start == end:
        return start
    else:
        mid = (end+start)//2
        if p[i_letter] >= x[sa[mid]+i_letter]:
            start = mid+1
        else:
            end = mid
    
    return recursive_upper_bound(p, x, sa, start, end, i_letter)

def search_array(x, p):
    '''Pattern matching function using a suffix array 
    Return the occurences of p in x'''
    
    sa = construct_array(x)
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

def array_runner(fasta_dict, fastq_dict):

    '''Pattern matching function using a suffix array through a dictionnary of sequences'''

    l = []
    for p_key, p_val in fastq_dict.items():
        for x_key, x_val in fasta_dict.items():
            matches = search_array(x_val, p_val)
            for i in matches:
                l.append('\t'.join([p_key, x_key, str(i+1), f'{str(len(p_val))}M', p_val]))
    
    return '\n'.join(l)

def main():
    
    argparser = argparse.ArgumentParser(
        description="Exact matching using a suffix array")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()

    # translate files into dicts
    fasta_dict = fasta_func(args.genome)
    fastq_dict = fastq_func(args.reads)

    print(array_runner(fasta_dict, fastq_dict))

if __name__ == '__main__':
    main()
