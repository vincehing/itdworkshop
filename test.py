# Challenge 3 : Logical Conditioning
def ch3():
	gender = st.selectbox("State your gender", ["Male", "Female"])
	age = int(st.text_input("State your age", 18))
	photo = st.camera_input("Smile! take a picture here.")

	# conditional logic to run different statements
	if age >= 21 and gender == "Male":
		st.write("You are a male adult")
	elif age < 21 and gender == "Male":
		st.write("You are a young boy")
	elif age >= 21 and gender == "Female":
		st.write("You are a female adult")
	elif age < 21 and gender == "Female":
		st.write("You are a young girl")

	if photo:
		st.write("Here is your photo: ")
		st.image(photo)
	else:
		st.write("No photo taken")