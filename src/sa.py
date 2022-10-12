import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using a suffix array")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()
    print(f"Find every reads in {args.reads.name} " +
          f"in genome {args.genome.name}")


if __name__ == '__main__':
    main()
