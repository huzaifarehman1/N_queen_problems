The approch to solving it effeciently is to use "random restart hill climbing search"
To find the problem statement see rules.txt

Approach — random-restart hill-climbing search
to Efficiently solve the problem (see rules.txt) using a hill-climbing local search enhanced with:


random restarts seeded 

1. High-level idea
Run a standard hill-climb from an initial state until you reach a local optimum (or termination condition).


When a run gets stuck, restart  a state 

Continuously update the max_ for the best score 

Terminate when budget (time, iterations, or evaluations) is used up or when solution quality meets the target.

Advantages:

restarts are focused 

memory stays bounded (size = 1),

improves chance of finding global optimum 

