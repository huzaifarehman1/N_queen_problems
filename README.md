The approch to solving it effeciently is to use "k best memory bounded random restart hill climbing search"
To find the problem statement see rules.txt

Approach — K-best memory-bounded random-restart hill-climbing search
Goal. Efficiently solve the problem (see rules.txt) using a hill-climbing local search enhanced with:

a memory of the k best states seen so far, and

random restarts seeded from this elite set (not purely random), while keeping memory bounded.

This document explains the idea, data structures, algorithm, parameters, pseudo-code, and practical implementation tips so you can drop it into your project.

1. High-level idea
Run a standard hill-climb from an initial state until you reach a local optimum (or termination condition).

Maintain an elite set (size ≤ k) that stores the best k states discovered so far (sorted by objective).

When a run gets stuck, restart from a state sampled from the elite set (optionally perturb it slightly).

Continuously update the elite set with newly discovered good states.

Terminate when budget (time, iterations, or evaluations) is used up or when solution quality meets the target.

Advantages:

restarts are focused on promising regions (exploitation), not blind random starts (exploration),

memory stays bounded (size k),

improves chance of finding global optimum while reusing good work.

