# from sequence_generator import (genome_sequence_generator,
#                                 random_sequence_generator)
# from lin import lin_runner
# from fasta_dict import fasta_func
# from fastq_dict import fastq_func
# from sa import array_runner

# def test_special():
#     empty_fasta = fasta_func(random_sequence_generator(0, 0, 'fasta','empty_fasta'))
#     empty_fastq = fastq_func(random_sequence_generator(0, 0, 'fastq','empty_fastq'))
#     a1_fasta = fasta_func(random_sequence_generator(1, 0, 'fasta', 'a1_fasta', True))
#     a1_fastq = fastq_func(random_sequence_generator(1, 0, 'fastq', 'a1_fastq', True))
#     a10_fasta = fasta_func(random_sequence_generator(10, 0, 'fasta', 'a10_fasta', True))
#     assert(sorted(array_runner(a10_fasta,a1_fastq))==lin_runner(a10_fasta,a1_fastq))
#     assert(sorted(array_runner(a10_fasta,empty_fastq))==sorted(lin_runner(a10_fasta,empty_fastq)))
#     assert(sorted(array_runner(a1_fasta,a1_fastq))==sorted(lin_runner(a1_fasta,a1_fastq)))
#     assert(sorted(array_runner(empty_fasta,empty_fastq))==sorted(lin_runner(empty_fasta,empty_fastq)))
#     assert(sorted(array_runner(empty_fasta,a1_fastq))==sorted(lin_runner(empty_fasta,a1_fastq)))


# def test_random():
#     fasta100 = fasta_func(random_sequence_generator(100, 8, 'fasta','fastaa100'))
#     fastq4 = fastq_func(random_sequence_generator(4, 0, 'fastq','fastq4'))

#     assert(sorted(array_runner(fasta100,fastq4))==sorted(lin_runner(fasta100,fastq4)))
#     #fastq100 = fastq_func(random_sequence_generator(100, 8, 'fastq','fastq100'))
#     #assert(sorted(tree_runner(fasta100,fastq100))==sorted(lin_runner(fasta100,fastq100)))

    
# def test_genome():
#     gen = fasta_func(genome_sequence_generator('src/sample_sequence.gz',
#      500, 8, 'fasta', 'genome'))
    
#     fastq0 = fasta_func(genome_sequence_generator('src/sample_sequence.gz',
#      0, 8, 'fastq', 'fastq0'))
#     fastq1 = fasta_func(genome_sequence_generator('src/sample_sequence.gz',
#      1, 8, 'fastq', 'fastq1'))
#     fastq10 = fasta_func(genome_sequence_generator('src/sample_sequence.gz',
#      10, 8, 'fastq', 'fastq10'))
#     fastq25 = fasta_func(genome_sequence_generator('src/sample_sequence.gz',
#      25, 8, 'fastq', 'fastq25'))
#     assert(sorted(array_runner(gen,fastq0))==sorted(lin_runner(gen,fastq0)))
#     assert(sorted(array_runner(gen,fastq1))==sorted(lin_runner(gen,fastq1)))
#     assert(sorted(array_runner(gen,fastq10))==sorted(lin_runner(gen,fastq10)))
#     assert(sorted(array_runner(gen,fastq25))==sorted(lin_runner(gen,fastq25)))