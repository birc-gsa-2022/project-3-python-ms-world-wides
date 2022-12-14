[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8892930&assignment_repo_type=AssignmentRepo)
# Project 3: Suffix array construction

You should implement a suffix array construction algorithm. You can choose to implement the naive O(n² log n)-time construction algorithm based on just sorting all the suffixes using a comparison based algorithm, the O(n²) algorithm you get if you radix sort the suffixes, or you can use the suffix tree from project 2: If you run through the suffix tree, and traverse children in lexicographical order, you will see each leaf in lexicographical order as well, and if you collect all the leaf-labels you have your suffix array.

If you feel adventurous, you are also welcome to implement one of the linear time algorithms *skew* or *SAIS* that we will see the next two weeks, but then you will have to read a bit ahead.

Once you have constructed a suffix array you should use it to implement a binary-search based exact pattern matching. Since I haven’t taught you have to do it faster, it should run in O(m log n + z) where m is the length of the pattern, n is the length of the genome string, and z is the number of matches you output. (One of the algorithms you have seen multiplies z by m, but you know how to avoid this).

Implement the suffix array construction and the exact pattern matching in a single program called `sa`.  The program should take the same options as in project 1, so `sa genome.fa reads.fq`. The program should output (almost) the same Simple-SAM file. Because a search in a suffix array is not done from the start to the end of the string the output might be in a different order, but if you sort the output from the previous project and for this program, they should be identical.

## Evaluation

Once you have implemented the `sa` program (and tested it to the best of your abilities) fill out the report below, and notify me that your pull request is ready for review.

# Report

## Algorithm
We implemented the  suffix array construction algorithm by using the suffix tree from project 2 and then sorting the leaf in lexicographical order. After that we collect all the leaf-labels == suffix array. The running time of building the tree from project 2 is O(n²). Sorting the leafs costs O(n) and reporting costs O(n) if the DNA sequence is random and quadratic if the sequence is a single-symbol string (see below). 

The binary-search based exact pattern matching we implemented by two recursive functions (finding the upper and lower bound). These are called in a for loop over the letter indexes in p and return the start and end indexes used for the following letter in p. Since the sa-boundary for letter i+1 in p is nested in the sa-boundary for letter i, this for loop through p's letters narrows (or keeps constant) the boundary range in every loop until finally returning it for the entire pattern.
It runs in O(m log n + z).

## Insights you may have had while implementing the algorithm
Splicing and comparing entire strings is inefficient as compared to comparing letters recursively with the lower and upper bounds from the previous letter in p.

The first search for lower and upper bounds is double work since it checks the entire range of sa.

## Problems encountered if any
We used the upper bound as the end of sa rather than one outside, which caused issues for a while.

## Validation

To check the correctness of the algorithm we compared the output of our match-algorithm with the output of the linear exact matching algorithm from project one. We used empty strings, uniform ones, random ones and part of existing DNA sequences to test our functions.

## Running time
To test the running time of the algorithm, we simulated random DNA sequences with belonging patterns. The running time was measured for building a suffix tree, sorting the tree, getting the suffix array and doing binary-search exact pattern matching. The running time was also measured for the final function consisting of all the steps. The result is shown in the figure below.
![](figs/time_random.png)

We also tested the running time with single-symbol strings. The result is shown below:

![](figs/time_worst_case.png)

Looking at the scale of the y-axis, we can see, that the running time is around 3 times worse on single-symbol strings for the final algorithm. Sorting the tree and doing the binary-search search doesn't seem to change whether we have random DNA sequences or single-symbol string. Here the running time seems to be linear. We expect to see a running time of O(m log n + z) for binary-search. To see a running time of O(m log n + z) would maybe require to run the experiment with longer sequences than done in this project.

As known the naive approach to build a suffix tree performs very poorly on single-symbol strings and gives us a running time that looks quadratic whereas it performs better on random DNA strings. Here the running time seems linear. 
Getting the suffix array is also influenced by which strings we investigate. The running time looks quadratic on single-symbol strings and linear on random DNA sequences.

