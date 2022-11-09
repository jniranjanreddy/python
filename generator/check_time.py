import random
import time

names = ['raji','chinnu','sandy','bunty']
subjects = ['Python','Java','Ansible']

def student_list(num):
    results=[]
    for i in range(num):
        student={'id':i, 'name':random.choice(names),'subject':
        random.choice(subjects)}
        results.append(student)
    return results

t1 = time.clock()
students = student_list(100000)
t2 = time.clock()
student_list(10)
print("The time taken to prepare list: ", t2-t1)

def student_generator(num):
    for i in range(num):
        student={'id':i, 'name':random.choice(names),'subject':
        random.choice(subjects)}
        yield student


t1 = time.clock()
students = student_generator(100000)
t2 = time.clock()
student_list(10)
print("The time taken to prepare Student generator list: ", t2-t1)
