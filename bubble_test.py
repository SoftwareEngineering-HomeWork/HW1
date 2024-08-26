from main import *

def testsort():
    tosort = [5,4,2,3,1,4,6]
    expectedsort=[1, 2, 3, 4, 4, 5, 6]
    assert bubblesort(tosort)==expectedsort

def testsort2():
    tosort2=[10,14,12,16,100]
    expectedsort2=[12,10,14,16,100]
    #assert bubblesort(tosort2)==expectedsort2

