import numpy as np
import math

# mencari distance titik p3 ke garis p1-p2
def getDistance(p1, p2, p3, points) :
    
    a = points[p1]
    b = points[p2]
    c = points[p3]

    # Rumus yang diturunkan dari rumus jarak titik ke garis
    return (c[1] - a[1])*(b[0] - a[0]) - (c[0] - a[0])*(b[1] - a[1])

# mencari posisi dari titik terhadap garis p1-p2
def positionToLine(p1, p2, p3, points) :
    dist = getDistance(p1, p2, p3, points)
    
    if dist > 0 : # berada di atas garis
        return 1
    elif dist < 0: # berada di bawah garis
        return -1
    else : # berada di garis
        return 0

# mencari titik dengan distance terjauh dari garis p1-p2
def getFarthestPoint(p1, p2, points, position) :
    idx = -1 
    maxDist = 0

    for i in range(len(points)) : # perbandingan secara bruteforce
        dist = getDistance(p1, p2, i, points)
    
        if (abs(dist) > maxDist) and (positionToLine(p1, p2, i, points) == position) : 
            idx = i
            maxDist = abs(dist)
            
    return idx

# mencari nilai ekstrim(min, max) berdasarkan nilai x dari himpunan
def getExtremes(points) :
    min = 0
    max = 0

    for i in range(len(points)) : # perbandingan secara bruteforce
        if points[i][0] > points[max][0] :
            max = i
        if points[i][0] < points[min][0] :
            min = i
    
    return max, min

# fungsi divide and conquer dari 
def quickHull(solution, p1, p2, points, position) :
    idxFarthest = getFarthestPoint(p1, p2, points, position)
    
    if (idxFarthest == -1) : # tidak ada lagi titik di luar convexhull yang menghadap garis p1-p2
        solution.append([p1, p2])
        return
    
    # membagi himpunan menjadi 2 bagian sesuai sisi segitiga yang terbentuk dari p1, p2, dan idxFarthest
    quickHull(solution, p1, idxFarthest, points, position)
    quickHull(solution, idxFarthest, p2, points, position)

# fungsi utama dari convexhull
def myConvexHull(points) :
    solution = [] # himpunan hasil

    max, min = getExtremes(points)

    # membagi himpunan jadi dua bagian
    quickHull(solution, max, min, points, 1)
    quickHull(solution, max, min, points, -1)

    return solution