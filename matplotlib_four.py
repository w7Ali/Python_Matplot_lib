# Ploting two axis over single graph
import matplotlib.pyplot as plt

# To Check available plot style
#print(plt.style.available)
# To use plot style
#plt.style.use('ggplot')
# Drawing like handwritten plot
plt.xkcd()
# data
ages_x = list(range(25,36))
salary_y = [38496, 42000, 46742, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
python_ai_salary = [45372, 48876, 53850, 57287, 63016, 65998, 70000, 70003, 71496, 75370, 83640]
java_salary = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

# format = [marker][line][color]
plt.plot(ages_x, salary_y, marker='d', linestyle='--',color='r', linewidth=2, label='All')
plt.plot(ages_x, python_ai_salary, marker='o', linestyle='-', color='m', linewidth=2, label='Python')
plt.plot(ages_x, java_salary, marker='|', linestyle=':', color='#5a7d9a',linewidth=2, label='Java Salary')


plt.title('Average salary in USD')
plt.xlabel('Ages')
plt.ylabel('Salary in USD')
plt.legend()
plt.grid(True)
plt.tight_layout()

# to save figure
plt.savefig('plot.png')
plt.show()
