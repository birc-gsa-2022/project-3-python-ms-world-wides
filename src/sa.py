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
    
    suffix = x[sa[end]:sa[end]+m]
    if suffix == p:
        return True, end-1, end, end

    while start!=end:

        mid = (start+end)//2
        suffix = x[sa[mid]:sa[mid]+m]

        if p == suffix:
            return True, start, mid, end
        if p < suffix:
            end = mid
        else:
            start = mid+1

    return False, -1, -1, -1

def recursive_lower_bound(p, x, sa, start, end, i_letter):
    # base case
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
    # base case
    if start == end:
        return start
    else:
        mid = (end+start)//2
        if p[i_letter] >= x[sa[mid]+i_letter]: # check only one letter
            start = mid+1
        else:
            end = mid
    
    return recursive_upper_bound(p, x, sa, start, end, i_letter)

def lower_bound(p, x, sa, start, end):
    m = len(p)
    mid = end # I think this doesn't make sense
    suffix = x[sa[mid]:sa[mid]+m]
    previous_suffix = x[sa[mid-1]:sa[mid-1]+m]

    while previous_suffix == p or suffix != p: 
        
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
        
        if p < previous_suffix:
            end = mid
        else:
            start = mid+1
        mid = (start+end)//2
        suffix = x[sa[mid]:sa[mid]+m]
        previous_suffix = x[sa[mid-1]:sa[mid-1]+m]
    return mid

def search_array_old(x, p):
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


def search_array(x, p):
    start = 0
    end = len(x)-1
    
    sa = construct_array(x)
    x += '$'
    occ = []
    if len(p)==0 or len(x)==1:
        return occ

    for i in range(len(p)):
        start, end = recursive_lower_bound(p, x, sa, start, end, i), recursive_upper_bound(p, x, sa, start, end, i)

    occ = [sa[i] for i in range(start, end)]
    
    return occ


def array_runner(fasta_dict, fastq_dict):

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

   #translate files into dicts
    fasta_dict = fasta_func(args.genome)
    fastq_dict = fastq_func(args.reads)

    #print(array_runner(fasta_dict, fastq_dict))

    chrom = 'acatattaggaggtaatcaaggcaatgcgcgatgaaaagatgagatgaccacggagtctcctggtgcttattctagaacaagcaagtacccggccgagtt'

    read = 'ttctagaaca'

    print(search_array(chrom, read))



if __name__ == '__main__':
    main()
