- # Notes
    - ## Understanding
        - get dataset  (www.computerchess.org.uk/ccrl
    - How to implement?
        - Pos2Vec class 
            - training of deep belief network. Using notebook for it for displaying images
        - deepchess class

    - Problemstatement
        - Given a state of all figures on a chess board at a certain moment. How is it possible to predict a move which one is close to the best possible move?

    - Get PGN data
    - How can I solve this problem??? 
        - first of all i could do a simple regression where I input the the chess board state-1 in one column and the last move in one column 
        - than could i use this regression model for inputting in it the current state  

    - I dont want to go with that way because I than do not really learn something about deep learning right?
    

- # Approach
    1. Reading material on the topic
        - Paper 
            - https://arxiv.org/abs/1509.01549 -
            - https://ieeexplore.ieee.org/document/9708405 -
            - https://www.cs.tau.ac.il/~wolf/papers/deepchess.pdf -
        - Video 
            - https://www.youtube.com/watch?v=bJfqn4Ysvsk - 
        - Summary/History
            - https://www.chessprogramming.org/Deep_Learning - 
        - Blog 
            - https://gregthompson27.medium.com/a-look-at-artificial-intelligence-and-deep-learning-in-chess-4ff8a24822e3 -
            - https://erikbern.com/2014/11/29/deep-learning-for-chess.html - 
    2. Decide for an learning technique
        - Reimplementation of the deepchess paper
    3. Implementation
        - Steps
            1. Understanding
            2. 