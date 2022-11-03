import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the sequences from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    for line in args.fastq:
        if line.startswith('@'):
            continue
        else:
            seq = line.strip()
            print(seq)


if __name__ == '__main__':
    main()
