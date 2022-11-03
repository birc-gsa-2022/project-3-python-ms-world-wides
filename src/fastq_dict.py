import argparse

def fastq_func(fastqfile):
    read = []
    name = ''
    fastq_dict = {}
    for line in fastqfile:
        if line.startswith('@'):
            if name != '':
                fastq_dict[name] = ''.join(read)
                read = []
            name = line[1:].strip()
        else:
            read.append(line.strip())

    if name != '':
        fastq_dict[name] = ''.join(read)

    return fastq_dict

def main():
    argparser = argparse.ArgumentParser(
        description="Extract the sequences from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    dic = fastq_func(args.fastq)
    print(dic)

if __name__ == '__main__':
    main()
