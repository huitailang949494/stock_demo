#! /usr/bin/env python

import sys
import os
import time
import numpy as np
from utils import *
from datetime import datetime
from gru_theano import GRUTheano

LEARNING_RATE = float(os.environ.get("LEARNING_RATE", "0.001"))
VOCABULARY_SIZE = int(os.environ.get("VOCABULARY_SIZE", "2192"))
EMBEDDING_DIM = int(os.environ.get("EMBEDDING_DIM", "48"))
HIDDEN_DIM = int(os.environ.get("HIDDEN_DIM", "128"))
NEPOCH = int(os.environ.get("NEPOCH", "20"))
MODEL_OUTPUT_FILE = os.environ.get("MODEL_OUTPUT_FILE")
INPUT_DATA_FILE = os.environ.get("INPUT_DATA_FILE", "/home/lab/stock_demo/Rem/utils/data/data_english.csv")
PRINT_EVERY = int(os.environ.get("PRINT_EVERY", "25000"))

def predict_module(target):
    INPUT_DATA_FILE = os.environ.get("INPUT_DATA_FILE", "/home/lab/stock_demo/Rem/utils/data/data_module.csv")
    x_train, y_train, word_to_index, index_to_word, target_sentence, target_sentence_set = load_data(INPUT_DATA_FILE, VOCABULARY_SIZE)
    model = GRUTheano(VOCABULARY_SIZE, hidden_dim=HIDDEN_DIM, bptt_truncate=-1)
    model = load_model_parameters_theano('/home/lab/stock_demo/Rem/utils/GRU-2017-06-04-22-11-35-48-128.dat.npz')
    stock_module = get_stock_module()
    i = 0
    for t in target:
        if not word_to_index.get(t):
            target[i] = index_to_word[2]
        i = i + 1
    target_sentence = [word_to_index[x] for x in target]
    sentence = predict_sentence(model, index_to_word, word_to_index, target_sentence, stock_module)
    return [index_to_word[x] for x in sentence]

def predict_stock(target):
    stock_module = get_stock_module()
    target_module = [stock_module.get(t).decode('utf-8') for t in target]
    print target_module
    modules = predict_module(target_module)
    print modules
    INPUT_DATA_FILE = os.environ.get("INPUT_DATA_FILE", "/home/lab/stock_demo/Rem/utils/data/data_english.csv")
    x_train, y_train, word_to_index, index_to_word, target_sentence, target_sentence_set = load_data(INPUT_DATA_FILE, VOCABULARY_SIZE)
    model = GRUTheano(VOCABULARY_SIZE, hidden_dim=HIDDEN_DIM, bptt_truncate=-1)
    model = load_model_parameters_theano('/home/lab/stock_demo/Rem/utils/GRU-2017-05-09-12-36-2192-64-256.dat.npz')
    stock_module = get_stock_module()
    target_sentence = [word_to_index[x] for x in target]
    print target_sentence
    sentence = predict_sentence_with_modules(model, index_to_word, word_to_index, target_sentence, stock_module, modules)
    print sentence
    return [index_to_word[x] for x in sentence]

