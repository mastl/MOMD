# Resources used for the MOMD project
20-06-2016

## Text processing in python
1. [Python course for the humanities by Folgert Karsdorp and Maarten van Gompel](http://nbviewer.jupyter.org/github/fbkarsdorp/python-course/blob/master/Chapter%202%20-%20First%20steps.ipynb)

## Database
1. [MongoDB introduction for Django](https://django-mongodb-engine.readthedocs.io/en/latest/)

## Courses
1. [Youtube-introduction to OOP by Brian will](https://www.youtube.com/watch?v=lbXsrHGhBAU)
	- Main points:
		i. OOP: Data before action.
		+ Classes are blueprints of objects containing fields (data members of class) and methods (function members).
			- Cats: Number of lives is a field. Cats meow is a method.
		+ Principles:
			1. Encapsulation: Only methods of class should be the ways the data (i.e. the fields) can be manipulated.
				- Public vs. private: Fields can only be private to the class.
			2. Inheritance: A type may include all members from another type (classes may overlap).
				- With inheritance we don't have to worry about if all methods from "mammals" are passed to "cats".
				- Sometimes referred to child and parents (cat is child of mammal).
				- Good to model real world objects.
				- Helps to avoid duplication.
				- **Think before applying inheritance**: There needs to be a "is-a"-relationship between objects --> not "has-a" relationship.
				- Multiple inheritance trades off flexibility with simplicity.
				- **Circular inheritance not allowed**.
				- The built-in object class is the most super class. I.e. all classes are objects.
				- It is possible to override. All mammals eat, but we can specify how cats specifically eat.
			3. Dot notation: We call method in classes by object_name.method_name(arg).
		+ Constructors: Sets up an instance at its creation (__init__ in python).
		+ Interface: A set of methods. Common ways to interact with different classes (for example many objects can move and stop).
		+ Abstract class: Not to be instantiated, but just works as parent. Like for example mammal, which only holds methods for the two classes dog and cats.
		+ Prototypical inheritance: OOP without classes - only used in javascript.