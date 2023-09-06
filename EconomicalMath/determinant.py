"""Module determinant calculating determinant """

baseArray3x3 = [[1.0, 2.0, 3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]]
result = float(0)

#for i in range(len(baseArray3x3)) :
#    for j in range(len(baseArray3x3[i])) :
#        print(baseArray3x3[i][j])

result1 = baseArray3x3[0][0]*baseArray3x3[1][1]*baseArray3x3[2][2]
print("Step 1: {0,0 * 1,1 * 2,2} :" , baseArray3x3[0][0]  , " * " , baseArray3x3[1][1] , " * " , baseArray3x3[2][2], "=", result1)
result2 = baseArray3x3[0][1]*baseArray3x3[1][2]*baseArray3x3[2][0]
print("Step 2: {0,1 * 1,2 * 2,0} :" , baseArray3x3[0][1]  , " * " , baseArray3x3[1][2] , " * " , baseArray3x3[2][0], "=", result2)
result3 = baseArray3x3[0][2]*baseArray3x3[1][0]*baseArray3x3[2][1]
print("Step 3: {0,2 * 1,0 * 2,1} :" , baseArray3x3[0][2]  , " * " , baseArray3x3[1][0] , " * " , baseArray3x3[2][1], "=", result3)

result4 = baseArray3x3[0][2]*baseArray3x3[1][1]*baseArray3x3[2][0]
print("Step 4: {0,2 * 1,1 * 2,0} :" , baseArray3x3[0][2]  , " * " , baseArray3x3[1][1] , " * " , baseArray3x3[2][0], "=", result4)
result5 = baseArray3x3[0][1]*baseArray3x3[1][0]*baseArray3x3[2][2]
print("Step 5: {0,1 * 1,0 * 2,0} :" , baseArray3x3[0][1]  , " * " , baseArray3x3[1][0] , " * " , baseArray3x3[2][2], "=", result5)
result6 = baseArray3x3[0][0]*baseArray3x3[1][2]*baseArray3x3[2][1]
print("Step 6: {0,0 * 1,2 * 2,1} :" , baseArray3x3[0][0]  , " * " , baseArray3x3[1][2] , " * " , baseArray3x3[2][1], "=", result6)
finalResult = result1+result2+result3-result4-result5-result6
print("Final step: {",result1,"+",result2,"+",result3,"-",result4,"-",result5,"-",result6,"} :",finalResult)