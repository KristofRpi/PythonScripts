from collections import defaultdict

l = [44, 86, 22, 29, 29, 16, 54, 88, 95, 65, 79, 94, 126, 43, 32, 9, 9, 2, 70, 83, 26, 26, 16, 15, 73, 30, 21, 12, 1, 22, 85, 66, 1, 0, 30, 66, 18, 20, 12, 16, 25, 12, 77, 2, 10, 16, 22, 72, 20, 9, 1, 77, 87, 1, 28, 4, 16, 1, 28, 31, 80, 14, 0, 0, 68, 22, 76, 46, 57, 28, 49, 71, 91, 16, 67, 73, 9, 21, 12, 1, 10, 81, 22, 76, 12, 25, 17, 4, 26, 29, 88, 78, 16, 2, 5, 29, 83, 3, 83, 11, 26, 4, 25, 84, 83, 24, 12, 73, 99, 99, 11, 31, 29, 83, 21, 84, 16, 24, 13, 8, 67, 83, 26, 7, 67, 26, 27, 24, 19, 27, 26, 28, 79, 17, 66, 104, 103, 60, 121, 39, 1, 89, 29, 73, 26, 25, 3, 31, 83, 67, 7, 76, 17, 5, 84, 83, 31, 8, 67, 26, 73, 0, 21, 28, 0, 18, 70, 7, 76, 18, 8, 17, 7, 1, 8, 94, 29, 4, 4, 4, 79, 5, 26, 64, 66, 9, 8, 12, 88, 31, 93, 73, 121, 0, 73, 2, 2, 11, 22, 1, 1, 22, 3, 69, 4, 95, 16, 1, 12, 81, 29, 12, 77, 31, 26, 1, 83, 82, 7, 15, 16, 31, 88, 7, 10, 69, 61, 100, 8, 1, 28, 79, 30, 22, 82, 17, 13, 2, 8, 66, 83, 91, 0, 94, 13, 5, 24, 20, 6, 29, 20, 1, 22, 4, 0, 77, 94, 29, 22, 73, 82, 11, 5, 2, 7, 70, 83, 4, 72, 14, 0, 69, 15, 84, 83, 7, 27, 81, 29, 4, 4, 4, 27, 22, 23, 1, 22, 3, 69, 25, 89, 22, 83, 40, 96, 39, 73, 31, 17, 27, 27, 22, 83, 66, 24, 13, 12, 95, 83, 22, 4, 81, 7, 5, 67, 125, 101, 39, 27, 68, 66, 45, 53, 36, 17, 4, 26, 5, 92, 78, 4, 12, 27, 10, 83, 0, 84, 16, 9, 69, 25, 89, 22, 83, 4, 85, 29, 26, 12, 23, 10, 83, 26, 82, 66, 9, 11, 14, 67, 10, 3, 29, 85, 10, 73, 29, 2, 0, 3, 22, 83, 14, 21, 69, 15, 84, 21, 28, 27, 85, 78, 28, 29, 28, 0, 18, 23, 72, 12, 11, 69, 25, 94, 83, 3, 27, 85, 24, 12, 3, 4, 79, 17, 18, 69, 66, 8, 4, 25, 80, 126, 121, 65, 68, 6, 8, 25, 80, 1, 22, 1, 69, 66, 46, 9, 8, 88, 16, 27, 12, 94, 12, 8, 14, 24, 10, 1, 83, 82, 3, 21, 22, 77, 69, 27, 26, 26, 16, 7, 26, 3, 87, 27, 83, 0, 68, 1, 25, 23, 8, 29, 83, 17, 28, 68, 78, 30, 5, 17, 27, 83, 23, 78, 7, 31, 69, 5, 84, 83, 24, 7, 95, 25, 86, 68, 94, 98, 121, 42, 78, 23, 76, 6, 12, 95, 83, 18, 10, 83, 11, 26, 30, 80, 27, 27, 26, 82, 66, 45, 53, 36, 17, 17, 10, 73, 96, 33, 58, 57, 25, 1, 20, 83, 64, 12, 76, 0, 3, 82, 1, 10, 25, 68, 11, 13, 77, 29, 10, 0, 0, 64, 5, 9, 69, 4, 95, 83, 7, 1, 85, 78, 15, 2, 2, 2, 83, 8, 3, 15, 9, 22, 30, 80, 20, 22, 75, 10, 78, 75, 8, 30, 12, 1, 10, 81, 22, 9, 1, 50, 66, 7, 1, 0, 94, 9, 75, 16, 125, 101, 7, 28, 1, 64, 67, 71, 67, 17, 62, 18, 2, 85, 78, 26, 24, 2, 10, 83, 10, 78, 23, 76, 1, 2, 95, 84, 7, 73, 86, 1, 27, 10, 21, 27, 83, 7, 78, 66, 4, 0, 21, 17, 22, 29, 10, 95, 10, 12, 77, 25, 27, 93, 126, 43, 111, 102, 44, 11, 17, 10, 28, 28, 16, 0, 12, 8, 20, 79, 7, 28, 1, 17, 9, 11, 9, 17, 18, 29, 16, 95, 0, 12, 77, 17, 79, 30, 22, 82, 17, 13, 2, 8, 29, 83, 1, 12, 93, 11, 4, 15, 21, 29, 83, 7, 73, 3, 24, 69, 8, 71, 22, 1, 16, 16, 15, 14, 8, 30, 27, 0, 84, 1, 18, 25, 7, 1, 88, 16, 83, 2, 85, 23, 100, 103, 25, 28, 83, 81, 102, 39, 56, 72, 12, 83, 31, 22, 75, 16, 15, 26, 77, 7, 10, 31, 31, 15, 66, 87, 76, 96, 59, 126, 121, 46, 95, 1, 13, 77, 28, 26, 16, 24, 1, 13, 25, 17, 77, 69, 27, 22, 27, 85, 99, 99, 64, 80, 55, 66, 67, 17, 111, 102, 104, 103, 28, 94, 94, 68, 16, 44, 44, 42, 57, 33, 83, 32, 100, 33, 62, 32, 57, 17, 54, 61, 42, 98, 55, 57, 57, 53, 43, 83, 62, 100, 49, 63, 36, 42, 116, 83, 94, 68, 29, 67, 100, 103, 18, 14, 16, 74, 18, 84, 15, 87, 94, 80, 74, 18, 12, 82, 88, 89, 15, 64, 12, 66, 75, 24, 83, 10, 86, 9, 2, 68, 70, 88, 1, 13, 90, 11, 18, 10, 74, 18, 17, 86, 91, 4, 94, 7, 65, 70, 15, 85, 94, 81, 14, 64, 91, 66, 71, 16, 90, 10, 81, 89, 0, 17, 70, 80, 82, 89, 89, 9, 72, 10, 74, 66, 71, 83, 15, 80, 88, 82, 22, 70, 90, 6, 91, 12, 15, 22, 91, 21, 21, 20, 6, 91, 86, 95, 87, 75, 23, 93, 82, 10, 89, 91, 20, 11, 71, 75, 21, 81, 9, 84, 8, 85, 65, 68, 13, 2, 87, 13, 84, 17, 86, 17, 66, 69, 4, 94, 83, 94, 4, 71, 74, 10, 86, 89, 93, 88, 66, 87, 18, 74, 17, 90, 88, 80, 95, 80, 17, 66, 12, 9, 8, 88, 14, 19, 88, 70, 23, 66, 1, 94, 81, 90, 4, 70, 23, 88, 1, 8, 95, 88, 68, 88, 66, 71, 64, 91, 9, 85, 12, 9, 74, 16, 91, 86, 92, 15, 14, 66, 95, 16, 16, 22, 7, 90, 81, 84, 5, 71, 68, 93, 86, 10, 11, 8, 64, 9, 67, 68, 67, 82, 10, 87, 14, 80, 74, 67, 12, 4, 90, 15, 12, 68, 94, 70, 23, 21, 7, 14, 82, 8, 85, 67, 16, 81, 4, 92, 10, 93, 17, 91, 70, 65, 17, 87, 92, 80, 92, 87, 23, 64, 8, 8, 87, 91, 12, 64, 98, 121, 94, 12, 79, 65, 69, 40, 127, 55, 83, 58, 117, 45, 59, 40, 36, 79, 54, 61, 98, 48, 53, 53, 57, 116, 55, 83, 36, 117, 61, 58, 44, 55, 42, 83, 94, 12, 79, 65, 104, 103, 60, 121, 39, 1, 89, 29, 73, 0, 21, 28, 0, 18, 70, 7, 76, 18, 4, 93, 31, 83, 26, 85, 2, 15, 64, 20, 10, 0, 7, 83, 23, 15, 17, 77, 88, 29, 83, 88, 0, 78, 26, 8, 19, 0, 29, 23, 82, 76, 66, 75, 67, 31, 93]

d = defaultdict(int)

for i in l:
    d[i] += 1

total = sum(d.values())

for i in d.keys():
    d[i] = (d[i]/float(total))*100.00

for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)
