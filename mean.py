import numpy as np

Test_1 = float(input("Test 1 value is : "))
Test_2 = float(input("Test 2 value is : "))
Test_3 = float(input("Test 3 value is : "))

scores = [Test_1, Test_2, Test_3]

average = np.average(scores)

print(f"Average is : {average}")
