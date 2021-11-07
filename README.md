# User Authentication Based On Keystroke Dynamics using Artificial Neural Network

## Introduction
This repository contains the data and code for the MIES term project. The project aims to detect unauthorized people to prohibit access to the particular system
and private data of users on the basis of keystroke dynamics. 

We run the code provided to us for feature extraction. Given the continuous data collected,
the extracted features are as follows:
* 26 hold times for the letters A to Z
* 676 (26 x 26) latency values for each pairing: AA,AB...ZY,ZZ

We ignore the hold and latency times of other characters on the keyboard like ‘Spacebar’ or
other keys like Tab, Ctrl or Backspace.
We take these 26 + 26 x 26 = 702 values as a feature vector for one class and use it to
classify from several classes. We take the average of all hold time and latency values for
one particular key or one particular pair of keys as this helps in smoothing the values and
returns an accurate representation of the several values.

## Dependencies
For successfully execution of the scripts, following libraries 
must be installed on your machine.
* numpy
* pandas
* sklearn

## Running 
To compute hold time vector and latency matrix from continuous mood data, we use 
`extract_feature.py` for each individual files.

To convert hold time vector and latency matrix to create dataset, run
```shell
$ python make_dataset.py
```
To train and test ANN on the dataset, run
```shell
$ python main.py --hidden_layers 100 25 --max_iter 500 --random_state 42
```
Above instruction will create a neural network with two hidden layers having 
number of nodes as 100 and 25 
in the order respectively.
The output will be displayed on the command line itself. 
## Sample Output
In the command line, you can expect to see the following output:
```
C:\Users\Utkarsh\Documents\MIES Term Project>python make_dataset.py
100%|████████████████████████████████████████████████████████████████████████████████| 180/180 [00:09<00:00, 19.29it/s]

C:\Users\Utkarsh\Documents\MIES Term Project>python main.py --hidden_layers 100 25 --max_iter 1000 --random_state 42
Fold 1:
        Training accuracy: 1.0
        Test accuracy: 0.6388888888888888

Fold 2:
        Training accuracy: 1.0
        Test accuracy: 0.5833333333333334

Fold 3:
        Training accuracy: 1.0
        Test accuracy: 0.6666666666666666

Fold 4:
        Training accuracy: 1.0
        Test accuracy: 0.6666666666666666

Fold 5:
        Training accuracy: 1.0
        Test accuracy: 0.6666666666666666

Five-fold cross validation result:
        Training accuracy: 1.0
        Test accuracy: 0.6444444444444444

DONE.
```
