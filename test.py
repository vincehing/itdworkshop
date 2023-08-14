#Challenge 2 : Input , Output and Variables
 def ch2():
  	name = st.text_input("Enter your name")
	gender = st.selectbox("State your gender", ["Male", "Female"])
	age = st.text_input("State your age", 18)

	if name and gender and age:
		st.text(f"Hello {name}, you are {gender} and this year you are {age} years old")