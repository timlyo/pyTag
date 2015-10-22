import os
from pyTag.pyTag import *
import pickle

weights = pickle.load(open(os.path.dirname(os.path.realpath(__file__)) + '/data/dict.pkl', 'rb'))

