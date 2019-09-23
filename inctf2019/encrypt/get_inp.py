from z3 import *
import base64

arr_check0 = [159, 94, 94, 111, 1, 6, 93, 132, 193, 193, 48, 23, 40, 80, 191, 44, 206, 1, 84, 14, 238, 185, 134, 87, 248, 184, 211, 21, 45, 2, 242, 153, 136, 95, 124, 134, 200, 161, 222, 208, 72, 203, 121, 28, 76, 196, 24, 31, 223, 165, 45, 192, 218, 72, 71, 68, 96, 93, 93, 236, 21, 170, 251, 255, 209, 48, 120, 244, 186, 27, 227, 123, 99, 48, 34, 135, 135, 18, 100, 221, 11, 163, 142, 137, 85, 9, 103, 166, 183, 60, 128, 102, 240, 108, 239, 141, 216, 91, 7, 198, 98, 172, 223, 215, 215, 73, 158, 252, 171, 100, 72, 157, 238, 25, 231, 81, 151, 44, 208, 136, 182, 19, 198, 248, 211, 25, 209, 152, 23, 71, 53, 182, 250, 140, 51, 181, 216, 159, 202, 171, 121, 89, 143, 157, 247, 105, 144, 100, 64, 120, 154, 179, 17, 29, 122, 134, 153, 170, 45, 179, 22, 228, 20, 6, 100, 227, 178, 158, 233, 90, 211, 116, 27, 16, 219, 52, 205, 138, 232, 193, 125, 251, 223, 96, 103, 220, 6, 179, 194, 117, 196, 122, 29, 212, 4, 145, 97, 189, 183, 42, 202, 93, 67, 13, 160, 202, 175, 167, 134, 156, 92, 224, 79, 65, 233, 247, 91, 243, 13, 14, 173, 148, 96, 32, 91, 104, 53, 137, 26, 227, 206, 7, 220, 157, 82, 70, 112, 179, 21, 192, 59, 88, 118, 143, 127, 152, 22, 247, 101, 225, 240, 16, 47, 37, 195, 124, 79, 236, 63, 201, 228, 147, 131, 179, 64, 246, 87, 90, 87, 202, 102, 126, 166, 228, 195, 121, 180, 5, 133, 36, 106, 233, 108, 4, 125, 88, 64, 79, 131, 111, 5, 137, 242, 46, 80, 123, 3, 152, 177, 2, 12, 179, 102, 148, 248, 33, 153, 75, 246, 160, 143, 33, 88, 116, 204, 154, 6, 204, 247, 30, 148, 99, 177, 206, 78, 84, 80, 106, 119, 68, 91, 55, 19, 8, 74, 90, 117, 236, 122, 132, 136, 125, 78, 43, 180, 60, 196, 76, 85, 83, 95, 240, 7, 162, 230, 37, 109, 89, 156, 241, 126, 233, 214, 245, 96, 208, 72, 196, 93, 129, 123, 234, 243, 189, 177, 56, 9, 38, 116, 123, 20, 17, 149, 123, 214, 176, 121, 138, 152, 105, 16, 226, 187, 26, 9, 160, 103, 36, 54, 28, 243, 220, 64, 253, 44, 65, 22, 52, 222, 194, 44, 50, 166, 240, 10, 50, 234, 246, 17, 197, 174, 145, 178, 138, 217, 100, 65, 252, 170, 40, 182, 249, 76, 100, 247, 128, 113, 198, 38, 98, 116, 103, 147, 170, 120, 128, 45, 16, 178, 111, 35, 239, 13, 13, 111, 56, 105, 195, 159, 168, 58, 218, 250, 159, 250, 143, 101, 76, 81, 253, 140, 250, 211, 159, 190, 250, 125, 153, 92, 68, 17, 84, 138, 7, 108, 112, 113, 229, 145, 120, 1, 228, 175, 134, 4, 94, 35, 177, 163, 14, 73, 34, 37, 93, 18, 66, 25, 131, 20, 156, 239, 121, 193, 53, 2, 184, 244, 237, 179, 135, 63, 180, 49, 200, 250, 179, 155, 28, 35, 100, 228, 65, 31, 52, 26, 120, 230, 95, 100, 98, 221, 202, 70, 220, 109, 126, 41, 81, 95, 89, 191, 44, 135, 146, 143, 77, 177, 117, 54, 14, 89, 26, 156, 21, 207, 90, 243, 230, 242, 146, 242, 193, 201, 144, 76, 95, 160, 137, 203, 147, 252, 72, 42, 144, 111, 82, 22, 46, 243, 1, 106, 72, 12, 40, 84, 202, 51, 28, 207, 184, 48, 23, 198, 66, 166, 217, 203, 167, 156, 102, 59, 156, 231, 48, 21, 126, 175, 142, 241, 15, 17, 237, 241, 185, 159, 1, 192, 203, 72, 230, 156, 147, 247, 70, 74, 93, 137, 11, 122, 199, 197, 243, 23, 188, 54, 74, 131, 22, 40, 89, 24, 128, 139, 125, 236, 159, 107, 18, 216, 85, 30, 159, 44, 211, 245, 116, 100, 178, 37, 107, 175, 52, 143, 155, 174, 246, 22, 209, 23, 101, 150, 12, 196, 86, 118, 242, 106, 168, 172, 46, 166, 198, 225, 198, 75, 78, 96, 226, 6, 66, 167, 255, 119, 117, 90, 125, 216, 215, 217, 108, 88, 189, 239, 206, 106, 228, 194, 134, 223, 49, 155, 234, 86, 110, 137, 152, 110, 159, 189, 201, 241, 6, 137, 224, 71, 239, 73, 241, 149, 166, 178, 195, 90, 42, 24, 100, 16, 132, 16, 21, 41, 224, 237, 66, 74, 48, 255, 20, 38, 109, 240, 194, 46, 56, 90, 223, 33, 107, 237, 65, 65, 208, 133, 252, 96, 254, 72, 2, 241, 103, 98, 92, 93, 118, 37, 189, 30, 205, 106, 25, 166, 1, 158, 194, 173, 13, 66, 46, 224, 46, 154, 147, 165, 164, 80, 0, 99, 155, 250, 248, 156, 189, 212, 203, 254, 82, 222, 88, 53, 59, 106, 133, 162, 148, 193, 210, 162, 161, 169, 135, 95, 91, 246, 11, 190, 53, 98, 242, 191, 6, 161, 110, 79, 29, 211, 128, 105, 205, 159, 189, 60, 5, 100, 182, 116, 65, 35, 200, 239, 253, 34, 227, 22, 235, 148, 7, 233, 251, 195, 222, 147, 249, 35, 247, 150, 46, 40, 102, 61, 195, 185, 138, 21, 218, 99, 60, 242, 37, 49, 113, 4, 154, 60, 207, 16, 46, 39, 211, 170, 15, 39, 76, 116, 42, 32, 35, 51, 0, 217, 234, 117, 240, 87, 233, 130, 250, 109, 56, 26, 172, 77, 250, 226, 250, 9, 248, 90, 241, 117, 29, 48, 207, 110, 103, 63, 107, 251, 121, 227, 89, 234, 219, 19, 195, 48, 174, 174, 211, 55, 43, 220, 202, 1, 106, 11, 145, 220, 50, 133, 63, 67, 85, 107, 123, 136, 219, 191, 33, 53, 3, 126, 133, 184, 236, 193, 17, 46, 74, 205, 205, 247, 212, 79, 81, 12, 22, 15, 150, 5, 121, 244, 217, 245, 85, 208, 148, 0, 251, 91, 82, 207, 26, 71, 65, 224, 15, 67, 159, 95, 226, 114, 64, 111, 239, 41, 164, 186, 246, 139, 193, 161, 96, 52, 33, 247, 223, 210, 50, 171, 85, 153, 59, 5, 74, 242, 216, 210, 2, 200, 204, 30, 149, 75, 112, 12, 114, 138, 121, 88, 49, 220, 247, 17, 32, 218, 4, 36, 28, 38, 237, 5, 227, 172, 15, 32, 45, 58, 53, 203, 143, 4, 9, 189, 243, 181, 143, 246, 217, 99, 58, 3, 206, 91, 167, 194, 161, 121, 74, 30, 233, 33, 158, 109, 117, 141, 40, 158, 179, 79, 134, 52, 9, 44, 116, 167, 26, 100, 43, 20, 80, 111, 163, 238, 172, 15, 122, 157, 18, 201, 77, 18, 3, 105, 103, 179, 136, 100, 104, 150, 245, 53, 34, 127, 191, 85, 73, 166, 176, 195, 155, 230, 39, 141, 168, 34, 75, 179, 43, 252, 138, 102, 82, 232, 201, 252, 216, 178, 58, 84, 237, 90, 249, 217, 149, 73, 148, 128, 82, 60, 52, 60, 72, 104, 27, 36, 8, 145, 83, 13, 86, 84, 214, 81, 43, 189, 227, 152, 215, 235, 54, 164, 181, 135, 242, 68, 183, 118, 180, 247, 136, 47, 96, 125, 228, 144, 96, 149, 55, 180, 190, 235, 15, 173, 115, 122, 210, 125, 207, 72, 127, 246, 70, 51, 105, 222, 6, 39, 50, 8, 137, 134, 137, 5, 159, 87, 44, 174, 123, 137, 6, 97, 122, 92, 109, 120, 104, 188, 98, 216, 86, 45, 157, 230, 56, 250, 133, 83, 86, 60, 74, 88, 240, 246, 36, 18, 205, 212, 101, 71, 196, 43, 89, 115, 81, 52, 148, 235, 252, 195, 61]
arr_check1 = [61, 18, 0, 68, 1, 88, 24, 21, 55, 57, 99, 71, 59, 101, 127, 1, 47, 0, 58, 9, 5, 29, 42, 26, 3, 88, 28, 13, 53, 12, 20, 64, 2, 58, 62, 67, 41, 123, 28, 78, 61, 43, 58, 29, 0, 44, 24, 83, 48, 58, 8, 9, 5, 0, 41, 77]


def firstfilename (arr_check0):
    for i in range(len(arr_check0)):
        if arr_check0[i] == arr_check0[(arr_check0[i] * 3 + 30) % len(arr_check0)]:
            print('firstfilename: ', chr(arr_check0[i]))
    return 0

def findName(firstchr, arr_check0):
    s = Solver()
    n = 15
    X = [BitVec('x_%s' % i, 8) for i in range(n)]

    var0 = ord(firstchr)
    for i in range(n):
    	var1 = (var0 * 3 + 30) % len(arr_check0)
    	s.add(X[i] ^ i == arr_check0[var1])
    	var0 = var1

    filename = ''
    if s.check() == sat:
    	m = s.model()
    	for i in range(n):
    		filename += chr(m[X[i]].as_long())
    return filename

def findkey(findname, arr_check1):
    key = ''
    var0 = findname
    for i in range(len(arr_check1)):
        key += chr(arr_check1[i] ^ ord(var0[i % len(var0)]))
    return base64.b64decode(key).decode("utf-8")

def get_inp(key):
    #bruteforce
    inp = []
    for i in range(41):
        inp.append([])
        for j in range(0x20, 0x7f):
            if i == 0:
                if ord(key[i]) == 97 + (j + 11) % 0x1a:
                    inp[i].append(chr(j))
            else:
                if ord(key[i]) == 97 + (j + ord(key[i - 1]) + 3) % 0x1a:
                    inp[i].append(chr(j))
    for i in range(len(key)):
        print(inp[i])
    #after guessing i got
    input = 'CYb3r_$3CuriTy_is_@_$#@r3d_R3$p0^$ibiliTy'
    # i got it because i did this challenge before organizers limit chr set
    return input

firstfilename(arr_check0)
print(findName('t', arr_check0))
print(findkey(base64.b64encode(findName('t', arr_check0)), arr_check1))
print(get_inp(findkey(base64.b64encode(findName('t', arr_check0)), arr_check1)))
