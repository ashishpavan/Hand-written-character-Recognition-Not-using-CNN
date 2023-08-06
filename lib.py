#importing the required library
import numpy as np
import pandas as pd
import PIL
from PIL import Image
from PIL import ImageTk,ImageDraw
from tkinter import ttk, colorchooser
from tkinter import *
from collections import Counter
from matplotlib import pyplot as plt
from sklearn import model_selection
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.decomposition import PCA
import random as rd

from time import time