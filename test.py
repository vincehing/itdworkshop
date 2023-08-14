#Challenge 4 : Data and Loops
def ch4():
	name = st.text_input("Enter your name")
	gender = st.selectbox("State your gender", ["Male", "Female"])
	age = st.text_input("State your age", 18)
	#declare empty dictionary
	mydict = {}
	mydict["name"] = name
	mydict["gender"] = gender
	mydict["age"] = age
	#Print out the items in the dictionary
	st.write("Here is your dictionary: ")
	st.write(mydict)

	#show individual items in dictionary
	st.write("You can also show individual items in the dictionary like this: ")
	for key, value in mydict.items():
		st.write(key + ": " + str(value))