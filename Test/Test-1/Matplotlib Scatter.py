# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# #day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show() 







# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

# plt.scatter(x, y, c=colors, cmap='viridis')

# plt.colorbar()

# plt.show() 






# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()





# import numpy as np
# import matplotlib.pyplot as plt

# x = np.random.normal(170, 10, 25000)
# y = np.random.normal(170, 10, 25000)
# plt.scatter(x, y)
# x = np.random.normal(1, 10, 25000)
# y = np.random.normal(1, 10, 25000)
# plt.scatter(x, y)
# x = np.random.normal(300, 10, 25000)
# y = np.random.normal(300, 10, 25000)
# plt.scatter(x, y)
# x = np.random.normal(35, 10, 25000)
# y = np.random.normal(35, 10, 25000)
# plt.scatter(x, y)
# plt.subplots(x,y)
# plt.show()





# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.show()




import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show() 