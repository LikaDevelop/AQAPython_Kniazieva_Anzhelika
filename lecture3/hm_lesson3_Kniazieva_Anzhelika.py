list_7_elements: int = [1, 2, 4, 2, 4, 2, 6]
salary_dict = {'salary': 100, 'bonys': 25, 'prime': 50}

#Sum of elements in list
def sum_elements_in_list(list_elements):
    sum = 0
    for el in list_elements:
        sum = el + sum
    return sum

print(sum_elements_in_list(list_7_elements))


#Unic element in list

unic_list = set(list_7_elements)
print(unic_list)

#Sum 3th element from list and salary

print(list_7_elements[2]+salary_dict['salary'])

#Full income from dict

print(salary_dict['salary']+salary_dict['bonys']+salary_dict['prime'])

#Change salary

salary_dict['salary'] = salary_dict['salary'] + salary_dict['prime']
print(salary_dict['salary'])