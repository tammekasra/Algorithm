

from re import I
import numpy as np
import matplotlib.pyplot as plt
import time
import minmax
import math



''' Someone recommended me this performacne test via peer-reviews '''

def loops(board,turn):
    times = []

    for i in range(10):
        startTime = time.time() 
        minmax.minimax(board, i, -math.inf, math.inf, True,turn) 
        endTime = time.time()

        times.append(endTime-startTime) 
   

    return times

function = loops(np.array(np.zeros((6,7)) ), 2)

print(function)


depths = [i for i in range(10)]
plt.plot(depths, function, '-b', label='Start of the game')
plt.legend(loc = 'upper left')
plt.ylim(-0.5,25)
plt.xlabel('Level of Depth')
plt.ylabel('Measured time in s')
plt.title('Test how fast is minmax regard to depth')
plt.show()