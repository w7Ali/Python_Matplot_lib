# Ploting two axis over single graph
import matplotlib.pyplot as plt

# data
ages_x = list(range(25,36))
salary_y = [38496, 42000, 46742, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
python_ai_salary = [45372, 48876, 53850, 57287, 63016, 65998, 70000, 70003, 71496, 75370, 83640]

plt.plot(ages_x, salary_y, label='All programmer')
plt.plot(ages_x, python_ai_salary, label='Python programmer')

plt.title('Average salary in USD')
plt.xlabel('Ages')
plt.ylabel('Salary in USD')
plt.legend()
plt.show()
