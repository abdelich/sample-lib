from sample import Sample
import matplotlib.pyplot as plt

samples = [
    Sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [146, 97, 73, 34, 23, 10, 6, 3, 4, 2, 2]),
    Sample([250, 750, 1250, 1750, 2250, 2750], [58, 96, 239, 328, 147, 132]),
    Sample([5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25], [1, 3, 6, 11, 15, 20, 14, 12, 10, 6, 2]),
    Sample([85, 34, 96, 102, 103], [2, 5, 11, 8, 4]),
]

for sample in samples:
    sample.info()
