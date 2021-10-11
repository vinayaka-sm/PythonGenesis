""" 
TEAM 5
PATTERN MATCHING
TEST FILE

"""
from a import *
import pytest

def test_myfile():
    #checking if string "lorem" is present on file
    db1 = Demo()
    assert db1.process_file("lorem") > 1           #pass
''''
def test_myfile2():
    #checking if string "leo" is present on file and also if it is repeated 5000 times
    db1 = Demo()
    assert db1.process_file("leo") ==5000          #fail

def test_myfile3():
    #checking other strings other than user input
    db1 = Demo()
    assert db1.process_file("vinayaka") > 1        #fail
'''
def test_myfile4():
     #cheeking if "leo" is repeated for 1219
    db1 = Demo()
    assert db1.process_file("leo") ==1219          #pass


def test_myfile5():
    db1 = Demo()
    assert db1.process_file("vinayaka") ==0         #pass

def test_myfile6():
    #Alpanumeric values checking
    db1 = Demo()
    assert db1.process_file("m249") >1              #pass

def test_myfile7():
    db1 = Demo()
    assert db1.process_file("ak47") ==1             #pass
