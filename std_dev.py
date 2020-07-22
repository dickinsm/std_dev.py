# Author: Makaliah Dickinson
# Date: 7/21/2020
# Description: Write a class called Person that includes the name and age. Write another function that returns the standar d
#              standard deviation of their ages (the classroom).

class Person:

    def __init__(self, name, age):


        self.name = name

        self.age = age

def basic_stats(person_list):


#list to store ages from person_list

    age = []

#for loop for get age from each object of class Person

for p in person_list:

#appending age into list age from each object of class Person

    age.append(p.age)


#calculating mean of ages

age_mean = statistics.mean(age)


#calculating median of ages

age_median = statistics.median(age)


#calculating mode of ages

age_mode = statistics.mode(age)


#returns mean, median, mode of ages


#objects of class Person

p1 = Person("Kyoungmin", 73)

p2 = Person("Mercedes", 24)

p3 = Person("Avanika", 48)

p4 = Person("Marta", 24)

#list of objects

person_list = [p1, p2, p3, p4]

#calling function basic_stats and prints a tuple

print(basic_stats(person_list)) # should print a tuple of three values
