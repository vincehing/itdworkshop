# Exercise 2 : Input , Output and Variables
def ex2():
	name = st.text_input("Enter your name")
	# only prints the Hello {name} if input box is not empty
	if name:
		st.write("Hello " + name)

def main():
	ex2()

if __name__ == "__main__":
	main()