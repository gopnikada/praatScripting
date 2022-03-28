import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(0, 1.2, 112)


y = 60791.6260573 * x ** 9 - 345947.2544127 * x ** 8 + 851364.0141563 * x ** 7 - (1.1868097 * 10 ** 6) * x ** 6 + (
            1.0198374 * 10 ** 6) * x ** 5 - 543695.8197947 * x ** 4 + 171110.5805037 * x ** 3 - 28846.7857594 * x ** 2 + 2351.6135838 * x + 48.5959481

y2 = 60791.6260573 * (x*1.5) ** 9 - 345947.2544127 * (x*1.5) ** 8 + 851364.0141563 * (x*1.5) ** 7 - (1.1868097 * 10 ** 6) * (x*1.5) ** 6 + (
            1.0198374 * 10 ** 6) * (x*1.5) ** 5 - 543695.8197947 * (x*1.5) ** 4 + 171110.5805037 * (x*1.5) ** 3 - 28846.7857594 * (x*1.5) ** 2 + 2351.6135838 * (x*1.5) + 48.5959481


outList = []
for i in zip(x,y2):
    if i[0] <= 0.8 and i[0] > 0:
        outList.append(f'{i[0]}\t{i[1]}')


with open('out.txt', 'w') as f:
    f.write('\n'.join(outList))

