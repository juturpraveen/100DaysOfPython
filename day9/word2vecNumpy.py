import re
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')
# logging.disable()

def tokenize(text):
    # obtains tokens with a least 1 alphabet
    pattern = re.compile(r'[A-Za-z]+[\w^\']*|[\w^\']*[A-Za-z]+[\w^\']*')
    return pattern.findall(text.lower())

def mapping_tokens(tokens):
    word_to_id = {}
    id_to_word = {}

    for i, v in enumerate(tokens):
        word_to_id[v] = i
        id_to_word[i] = v
    return word_to_id, id_to_word

def generate_training_data(tokens, word_to_id, window_size):
    N = len(tokens)
    w = window_size
    X, Y = [], []
    for i in range(N):
        contextIndices = list(range(max(0, i-w), i)) + list(range(i+1, min(N, i+w+1)))
        # logging.debug(contextIndices)
        for j in contextIndices:
            X.append(word2Id[tokens[i]])
            Y.append(word2Id[tokens[j]])

    X = np.array(X)
    X = np.expand_dims(X, axis=0)
    Y = np.array(Y)
    Y = np.expand_dims(Y, axis=0)

    return X, Y

str = "This sentence should contain more than ten words other wise this would not be a good tutorial at all."
tokens = tokenize(str)
word2Id, id2Word = mapping_tokens(tokens)
X, Y = generate_training_data(tokens, word2Id, 3)
vocab_size = len(id2Word)
m = Y.shape[1]
print(m)
#Turn Y into onehot vector
Y_one_hot = np.zeros((vocab_size, m))
print(Y_one_hot.shape)
Y_one_hot[Y.flatten(), np.arange(m)] = 1
print(Y_one_hot.shape)