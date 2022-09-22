import sys
import os

client = 0

matrix = []
# here you give the right path to the file
with open("C:/Users/Me/Downloads/TSO/nearest/101nodes.txt") as file:
    for line in file:
        matrix.append(line.split())


print(*matrix, sep="\n")


#Example of output for 101nodes.txt:

def nearest_neighbor(matrix):
    global client
    client = int(matrix[0][0])
    matrix = matrix[1:]
    for i in range(client):
        matrix[i] = [int(matrix[i][0])] + [float(matrix[i][1])] + [float(matrix[i][2])]
    return matrix

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def nearest(matrix):
    global client
    path = []
    path.append(matrix[0][0])
    matrix.pop(0)
    for i in range(client-1):
        dist = []
        for j in range(len(matrix)):
            dist.append(distance(matrix[j][1], matrix[j][2], matrix[0][1], matrix[0][2]))
        path.append(matrix[dist.index(min(dist))][0])
        matrix.pop(dist.index(min(dist)))
    return path

print('The path is: ', nearest(nearest_neighbor(matrix)))
