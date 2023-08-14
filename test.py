#Exercise 3 : Logical Conditioning
def ex3(): 
	age = st.text_input("State your age", 18)
	#if else statement
	age = int(age)
	if age >= 21:
		st.write("You are an adult")
	else:
		st.write("You are not an adult")