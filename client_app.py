# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:45:04 2020

@author: gerrl
"""
#imports
import Naive
import KNN
import NeuralNetwork
import time

menu = "\nPlease select the data mining algorithm you would like \
to use.\n -----------------------\n|1 - Naive Bayes\t|\n|2 - Nearest Neighbors\t|\n|\
3 - Neural Networks\t|\n|0 - EXIT\t\t|\n -----------------------\n"
input_val = 1

print("\n\nHello\n")
time.sleep(1)
while(input_val != 0): 
    print(menu)
    input_val = int(input())

    if input_val == 1:
        print("\nNaive Bayes chosen")
        Naive.NaiveBayes_Iris()
    elif input_val == 2:
        print("\nKNN chosen")
        KNN.KNN()
    elif input_val == 3:
        print("\nNeural Network chosen")
        NeuralNetwork.NeuralNetwork()
    elif input_val == 0:
        time.sleep(0.5)
        print("\nGoodbye")
        time.sleep(1)
    else:
        print("\nInvalid Input")

