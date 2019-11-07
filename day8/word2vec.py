from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

#Training data 
'''
The training date to be replaced by a function that scrapes data from web; tokenizes text.
'''
sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
             ['this', 'is', 'the', 'second', 'sentence'], ['yet', 'another', 'sentence'],
             ['one', 'more', 'sentence'],
             ['and', 'the', 'final', 'sentence']]

# Training the model
'''
window = Default is 5. 
Minimum count refers to the min count a word should have in its context, otherwise it is ignored.
size - number of dimensions for each vector, default 100
sg = 0 -> CBOW
sg = 1 -> SkipGram
windo
'''
model = Word2Vec(sentences, size=100,sg=0,min_count=1)
print(model)

#Vocabulary
words = list(model.wv.vocab)
print(words)

#Print vector represnetation of a word
print('sentence: ', model['sentence'])

#Save model to a file in binary format
model.save('model.bin')

#Reload the save model
new_model = Word2Vec.load('model.bin')

# #Print the words of new model
# print(list(new_model.wv.vocab))

