# from vectors import Point, Vector
import random
import numpy as np

# import collections
'''
v1 = vector(1.45, 2.92, 3.241) #=> Vector(1, 2, 3)
v2 = vector(-2.42, 4.94, -6.12) #=> Vector(2, 4, 6)
print(v1+v2)



def cos_sim(a, b):
	"""Takes 2 vectors a, b and returns the cosine similarity according 
	to the definition of the dot product
	"""
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)


A = np.array(((1.45, 2.92, 3.241), (-2.49, 4.94, -6.12), (1,2,3), (8,2,10)))
print(A[1,1])
#print(A)

#Initialize n and p
n=1
p=1/(1+n)

#print(A[1])

#Create a  new cluster A1
A1=[]
A1.append([])


#Add the first vector to cluster A[0]
A1[n-1].append(A[1])


A1.append(A[1])
A1.append(A[3])
print(A1)

k=0
#print(A1[1,1])

#len(A) gives the total number of rows in A
for i in range(1,len(A)-1):
    r=random.randint(0,1)
    #print("Hello %d"%i)
    if r<p:
        print("R<P")
        n=n+1
        print("n:%d"%n)
        p=1/(1+n)
        A1[n-1]=create_row(A[i])
        #np.vstack((A1,A[i]))
        #print(len(A1[0]))
        print(A1)
    else:
       print(len(A1[0])) 

'''


def cos_sim(a, b):
    """Takes 2 vectors a, b and returns the cosine similarity according
    to the definition of the dot product
    print("a:")
    print(a)
    print("b")
    print(b)
    """
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    # print("norm_a %d"%norm_a)
    # print("norm_b %d"%norm_b)
    return dot_product / (norm_a * norm_b)


from collections import defaultdict

d = defaultdict(list)
Array = np.array(((-0.00310242, -0.00685576, 0.0123638, -0.0110518, -0.00510003, -0.00137864, 0.001443985, -0.01092566,
                   0.00999887, 0.008617, 0.012951, -0.01352084, -0.00384792, -0.01291396, 0.01153752, -0.00395127,
                   -0.00323742, -0.01327466, -0.01536126, -0.01229387, 0.00964621, 0.00071328, 0.00147458, 0.00845054,
                   -0.00716749, 0.00490449, 0.00013596, 0.00829258, -0.00599303, -0.00594364, 0.00912605, -0.0061678),
                  (0.0092035, 0.00743467, 0.01198821, 0.01203646, -0.00268724, -0.01068792, 0.00173238, -0.0141671,
                   -0.01235074, 0.00525341, 0.00735532, 0.00305996, -0.00687516, -0.01232796, 0.00074483, 0.01549168,
                   -0.01398288, 0.00673351, 0.00866384, 0.0074623, 0.01534828, 0.00329491, -0.0005149, 0.00704319,
                   0.01060658, 0.0052655, -0.00386912, -0.00521312, -0.00482798, -0.00043125, 0.0035244, -0.00084577),
                  (-0.01231046, 0.0102633, 0.261738, 0.01457201, 0.00886919, -0.01446168, 0.00207867, 0.01340493,
                   -0.00601739, 0.01460541, 0.0062859 - 0.0117764, 0.01181331, -0.00522275, -0.00363502, 0.00420082,
                   0.01130871, 0.01518725, -0.01140779, 0.01036875, -0.01530109, 0.00288353, 0.00671123, -0.01502704,
                   -0.01242342, -0.00256302, 0.00813321, 0.00475323, -0.00331046, -0.01515651, 0.0001195, 0.00478991,
                   -0.01023836),
                  (-0.0034824, 0.01445437, 0.00198138, -0.0113178, -0.00930163, -0.0121033, -0.00732992, -0.00126221,
                   0.00841909, -0.00426721, -0.00795001, 0.00775621, -0.0126108, -0.00974729, 0.00408183, 0.0110542,
                   -0.00521979, 0.01327743, -0.00488802, 0.01335913, 0.01095606, 0.00237086, 0.0090434, 0.01371366,
                   0.0027896, -0.00057844, 0.00678552, -0.00998028, -0.01147962, 0.00813512, -0.01317593, 0.00128318),
                  (0.01455265, 0.01261902, -0.0116231, -0.01390174, -0.01228218, 0.00220097, -0.01442711, -0.00890185,
                   -0.00661852, -0.00565598, 0.00424325, -0.00146173, -0.00229359, -0.00056029, -0.00942336, 0.00099954,
                   -0.01367431, 0.00815712, 0.00651964, -0.01503303, 0.00910029, 0.01264452, 0.01327908, -0.01009579,
                   0.00354912, 0.01239335, -0.01399444, 0.01354426, -0.01261514, 0.00591605, 0.01482034, 0.01516803),
                  (-0.01249896, -0.01222401, 0.00718367, 0.01201722, 0.00177968, 0.00713157, 0.00064796, 0.0029153,
                   0.00134206, -0.00167771, 0.00863686, 0.00856483, -0.00274196, 0.0106046, -0.00396132, -0.00863387,
                   0.00353155, -0.01092883, -0.00083387, -0.01215021, -0.01487978, -0.01160693, -0.011648, 0.00680635,
                   0.0123895, 0.00982762, -0.00400402, 0.00771988, -0.01467359, 0.00540147, -0.01519807, 0.0025698)))
# a=3
# k=0;
n = 1
p = 1 / (1 + n)
d[1].append(Array[0])
# d[1].append(Array[3])
# d[2].append(Array[1])
# print("length:")
# print(len(Array))
for i in range(1, len(Array)):
    r1 = random.randint(0, 1)
    r2 = random.randint(0, 1)
    r3 = random.randint(0, 1)
    r = (r1 + r2 + r3) / 5
    if r < p:
        # print("r<p")
        n = n + 1
        print("n=n+1")
        p = 1 / (1 + n)
        # print("appending data to [%d,%d]"%(n, p))
        d[n].append(Array[i])
        # print("d[n]:")
        # print(d[n][1])
    else:
        # print("2nd case with n:%d"%n)
        index = 1
        for m in range(1, n):
            ans = 0
            maximum = -1
            # print("D")
            # print(d)
            length = len(d[m])
            for j in range(1, len(d[m])):
                # print("length, m,j:%d,%d,%d"%(len(d[m]),m,j))
                # print("m:%d"%j)
                # print(Array[i])
                # print(d[m][j])
                cos = cos_sim(Array[i], d[m][j])
                print(d[m][j])
                print(cos)
                ans += cos_sim(Array[i], d[m][j])
                # print("similarity %d"%ans)
            sim = ans / length;
            if sim > maximum:
                index = m
        # print("Index :%d"%index)
        d[index].append(Array[i])
print("End of Program")
print(d)

