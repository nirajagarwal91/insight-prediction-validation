## Details of challenge

You are given the following input files

1. `actual.txt`: A time-ordered file listing the actual value of stocks at a given hour.
1. `predicted.txt`: A time-ordered file of the predicted value of certain stocks at a given hour. 
1. `window.txt`: Holds a single integer value denoting the window size (in hours) for which you must calculate the `average error`.

You are expected to produce the following output file

1. `comparison.txt`: A time-ordered file containing the average error of stock predictions for a certain time period

## My Repo directory structure
```
.
├── README.md
├── run.sh
├── src
│   └── prediction-validation.py
├── input
│   ├── actual.txt
│   ├── predicted.txt
│   └── window.txt
├── output
│   └── comparison.txt
└── insight_testsuite
    ├── run_tests.sh
    └── tests
        ├── test_1
        │   ├── input
        │   │   ├── actual.txt
        │   │   ├── predicted.txt
        │   │   └── window.txt
        │   └── output
        │       └── comparison.txt
        │
        └── my_test
            ├── input
            │   ├── actual.txt
            │   ├── predicted.txt
            │   └── window.txt
            └── output
                └── comparison.txt
```


# Instructions

./src is the directory where your source code would reside.

Source code file name: prediction-validation.py

This file uses files as below:

Input for Stock Data: ./input/actual.txt Predicted Stock Data: ./input/predicted.txt Window for Stock Data: ./input/window.txt

Output: ./output/comparison.txt

# Run Instructions

To get the comparison.txt file as output run the shell file run.sh placed on the root directory on the terminal.

`$ ./run.sh`

or

`$ sh run.sh`

Program has been tested with edge cases when there are no predictions for the 1,2 hour as well as no predictions for the last couple of hours.
