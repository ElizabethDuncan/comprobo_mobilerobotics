#!/usr/bin/env python
import pickle

data = pickle.load( open( "exampleArray.p", "rb" ) )
print type(data)
print data[1]