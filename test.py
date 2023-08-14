# Exercise 4 : Data and Loops 
def ex4():
	# Data list
	fruits = ["apple", "banana", "orange"]

	# Dictionary
	person = {"name": "John", "age": 30, "city": "New York"}

	# For loop to show list
	st.subheader("Fruits list:")
	for fruit in fruits:
		st.write(fruit)

	#for loop to show dictionary list
	st.subheader("Person dictionary:")
	for key, value in person.items():
		st.write(key + ": " + str(value))