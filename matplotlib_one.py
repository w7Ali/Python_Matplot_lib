import matplotlib.pyplot as plt

#age_x = [25,26, 27 ,28, 29, 30, 31,32,33,34,35]
age_x = list(range(25,36))
print(age_x)
print(type(age_x))
salary_y = [38496, 42000, 46742, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Giving the x and y list values
plt.plot(age_x,salary_y)

# Labeling
plt.title('"Median Salary (USD) by Age')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')

# Showing the plot
plt.show()