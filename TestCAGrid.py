from CellularAutomaton import *
import numpy as np


# mydtype = np.dytpe('f')
# data = np.array([[0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11.], [10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20, 21],
#              [20., 21., 22., 23., 24., 25., 26., 27., 28., 29., 30, 31]])
# data = np.array([[ (1.,),  (2.,),  (3.,),  (4.,),  (5.,),  (6.,),  (7.,),  (8.,),  (9.,), (10.,)], \
#                [(11.,), (12.,), (13.,), (14.,), (15.,), (16.,), (17.,), (18.,), (19.,), (20.,)], \
#               [(21.,), (22.,), (23.,), (24.,), (25.,), (26.,), (27.,), (28.,), (29.,), (30.,)]], dtype=mydtype)
# x = CAGrid((3,10),mydtype, buffer=data)


def test_setboundary():
    Rows = 3
    Columns = 6
    mydtype = np.dtype([('Value','i')])
    MyGrid = CAGrid((Rows,Columns),mydtype)

    for yy in range(Rows):
         for xx in range(Columns):
             MyGrid['Value'][yy][xx] = 10*yy + xx + 100

    print('Before Set Boundary ************')
    print(MyGrid)
    print('The base is')
    print(MyGrid.Base)

    MyGrid.SetBoundary()
    print('After Set Boundary*******************')
    print(MyGrid)
    print('The base is')
    print(MyGrid.Base)

def test_update(rows, columns, interations, states):
    mydtype = np.dtype([('Value','b')])
    MyGrid = CAGrid((rows,columns),mydtype)

    i=0
    for y in range(rows):
        for x in range(columns):
            MyGrid["Value"][y][x]=states[i]
            i = i + 1
    MyGrid.SetBoundary()
    print('After Initialization')
    print(MyGrid)

    for i in range(interations):
        MyGrid.Update()
        print('After Update i = {}'.format(i+1))
        print(MyGrid)





#test_setboundary()
test_update(3, 3, 2, states = (0,1,0,1,0,1,0,1,0))
print('next should give a stable block in upper right corner.')
test_update(3, 3, 2, states = (1,1,0,1,1,0,0,0,0))
print('next should go from vertical line to filled, to dead,')
test_update(3, 3, 2, states = (0,0,0,1,1,1,0,0,0))
print('next should go give a line blinker')
test_update(4, 5, 5, states = (0,0,0,0,0,
                               0,0,0,0,0,
                               0,1,1,1,0,
                               0,0,0,0,0))
print('next')
test_update(3,3,3,states = (0,1,0,1,0,1,0,1,0))


