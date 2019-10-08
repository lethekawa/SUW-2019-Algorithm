# 1.sort -> 5. Quick Sort
def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
           i+=1
           arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

def select(A, p, r, i):
    if p == r:
        return A[p]
    q = partition(A,p,r)
    k = q - p + 1
    if i < k:
        return select(A , p , q-1, i)
    elif i == k:
        return A[k]
    else:
        return select(A, q+1, r, i-k)


testcase = [393, 317, 18, 499, 451, 123, 156, 379, 999, 444, 348, 282, 329, 329, 328, 26, 177, 163, 398, 211, 172, 39, 53, 62, 249, 215, 92, 463, 79, 282, 243, 230, 327, 327, 460, 46, 279, 73, 22, 60, 97, 186, 409, 195, 126, 207, 255, 194, 174, 52, 448, 498, 37, 49, 213, 183, 212, 423, 107, 228, 464, 89, 319, 49, 498, 120, 383, 338, 356, 45, 292, 103, 80, 226, 251, 112, 85, 311, 252, 7, 187, 359, 357, 434, 186, 383, 25, 170, 282, 190, 186, 379, 70, 60, 448, 200, 425, 484, 392, 288, 488, 163, 74, 104, 341, 499, 8, 341, 175, 272, 32, 42, 70, 494, 232, 353, 316, 296, 470, 426, 359, 265, 334, 114, 423, 499, 401, 100, 154, 279, 102, 113, 373, 390, 68, 79, 188, 240, 171, 25, 145, 383, 361, 11, 222, 214, 211, 198, 235, 253, 223, 324, 189, 218, 294, 446, 294, 164, 230, 7, 107, 99, 358, 61, 472, 385, 262, 148, 131, 400, 164, 362, 302, 87, 306, 183, 347, 116, 123, 80, 385, 202, 330, 103, 284, 320, 187, 428, 30, 254, 288, 171, 163, 256, 411, 497, 176, 59, 63, 186, 437, 462]
num = int(input("select n : "))
print("Select", select(testcase, 0, len(testcase) - 1, num))
