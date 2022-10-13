import argparse

def fasta_func(fastafile):
    '''Function that can take file or list of strings and return dictionary
    with fasta sequence coupled with its sequence name'''

    sequence = []
    name = ''
    fasta_dict = {}
    for line in fastafile:
        if type(line) == list:
            line = line[0]
        if line.startswith('>'):
            if name != '':
                fasta_dict[name] = ''.join(sequence)
                sequence = []
            name = line[1:].strip()
        else:
            sequence.append(line.strip())

    if name != '':
        fasta_dict[name] = ''.join(sequence)

    return fasta_dict


def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    dic = fasta_func(args.fasta)
    print(dic)

if __name__ == '__main__':
    main()
