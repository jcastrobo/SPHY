import time, shutil, os, glob, configparser, sys, csv, math
import pandas as pd
import pcraster as pcr
import pcraster.framework as pcrm
import numpy as np

#tic = time.clock()

# Read the model configuration file
config = configparser.RawConfigParser()
#config.read(sys.argv[1])
xx= config.getint('MODULES','GlacFLAG')
xx