import argparse
from tree import construct_sorted_tree, subtree_labels

def construct_array(x):
    '''Return the suffix array of string x
    
    >>> construct_array('mississippi')
    [11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
    '''
    T = construct_sorted_tree(x)
    L = subtree_labels(T[0])

    return list(L)


def main():
    # argparser = argparse.ArgumentParser(
    #     description="Exact matching using a suffix array")
    # argparser.add_argument("genome", type=argparse.FileType('r'))
    # argparser.add_argument("reads", type=argparse.FileType('r'))
    # args = argparser.parse_args()
    # print(f"Find every reads in {args.reads.name} " +
    #       f"in genome {args.genome.name}")

    print(construct_array('mississippi'))


if __name__ == '__main__':
    main()
