import numpy as np
import data.load as data_loader

X = data_loader.load_data('data/data.npy')
print data_loader.translate_to_words(X[0])