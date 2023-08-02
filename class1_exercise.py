import streamlit as st
import openai
from PIL import Image

def class1_prep():
	# st.subheader("Course Slides")
	# st.markdown("https://go.gov.sg/itdchatbotprototype")
	st.divider()
	st.subheader("Pre-workshop Setup")
	# st.divider()
	st.markdown("""1. Visual Studio (VS Code): this is the Integrated Development Environment (IDE) of choice by many coders and will make it easier for us to code our app.""")
	st.markdown("""2. Python (3.10 release or later): this is the coding language of choice for many data science related apps.""")
	st.write("""
			3. Once you have installed the above, we will need to set up a virtual environment and install the libraries in that environment.\n
				Create a folder named “chatbot” anywhere, e.g. in your Desktop.\n 
				Open VS Code and navigate to the folder in a new terminal window.\n 
				Create a virtual environment and activate it by entering the following commands in the terminal:
			 """)
	st.markdown("   **a) Mac**")
	st.code('''
		python3 -m venv venv
		source venv/bin/activate 
			''')
	st.markdown("(You should see a (venv) appear in your terminal window prompt)")
	st.markdown("#")
	st.markdown("   **b) Windows**")
	st.code('''
		python -m venv venv
		cd venv\Scripts
		activate
			''')
	st.markdown("4. While in your virtual environment, install the libraries using pip which should already be installed together with Python:")
	st.code('''
		pip install streamlit openai
			''')
	st.markdown(" To test if Streamlit is installed properly, run this command:")
	st.code('''
	streamlit hello
			''')
	st.markdown(" You should see a Streamlit application running at http://localhost:8501")
	st.markdown(" Type Ctrl + C in VS Code terminal to stop the Streamlit app")
	pass

def class1_hw1():
	st.subheader("My first Hello World app")
	st.divider()
	st.markdown("""1. Create a new file called 'main.py'.""")
	st.markdown("""2. Copy the code below and paste it in the newly created helloworld.py file.""")
	st.markdown("**:blue[Code]**")
	st.code('''
			import streamlit as st
			#my first Hello World app
			st.write("Hello World")
		''')
	st.markdown("Install the watchdog module by running the command below in the terminal.")
	st.code("pip install watchdog")
	st.markdown("Now you don't have to keep restarting the app to see the changes you make to the code. Just refresh the browser.")
	st.write("Save your file and run the app by typing the following command in the terminal:")
	st.code('''
			streamlit run main.py
		''')
	st.markdown("""3. You should see a Streamlit application running at http://localhost:8501""")
	st.markdown("""4. Type Ctrl + C in VS Code terminal to stop the Streamlit app""")
	st.markdown("**:red[Code Output]**")
	st.write("Hello World")
	pass

def objectives():
	st.subheader("Objectives")
	st.markdown("1. Learn how to use Python and Streamlit library to create an interactive web app.")
	st.markdown("2. Learn how to integrate and use OpenAI's API in their streamlit application to create a simple chatbot.")
	st.markdown("3. Learn how to apply basic prompt engineering to enhance the interaction with the chatbot.")

def workshop_outline():
	st.subheader("Outline")
	st.markdown("Part 0: Workshop introduction and rules")
	st.markdown("Part 1: Introduction to Python and Streamlit")
	st.markdown("Part 2: Creating a rule-based chatbot")
	st.markdown("Part 3: Creating a chatbot using OpenAI's API")
	st.markdown("Part 4: Modifying your chatbot with prompt engineering")

def team_introduction():
	st.write("Do introduce yourself to your teammates:\n", "1) name\n", "2) division\n", "3) role")
	st.write("Please also share your favourite Star Wars character and why!")
	image = Image.open('team_introductions.jpeg')
	st.image(image, caption='Hello there!')

def workshop_rules():
	st.subheader("Workshop Rules")
	st.write("1. Ask if you have questions.")
	st.write("2. Be open to different ways to solve the problem.")
	st.write("3. Try. Fail. Learn. Repeat.")
	st.write("4. Seek help from other team members.")
	st.write("5. Collaborate, if possible, for the challenges.")
	st.write("6. Approach facilitators if your team cannot solve the problem.")
	st.write("7. Toilet break is own-time-own-target.")
	st.write("8. Have fun!")

def vscode_ui():
	st.subheader("Navigating the VS Code interface")
	image = Image.open('VSCode_interface.png')
	st.image(image, caption='VS Code UI layout')
	st.markdown("**A: Activity Bar: this is where you can see the different activities you can do in VS Code.**")
	st.markdown("	Explorer: this is where you can see all the files and folders in your project.")
	st.markdown("	Source Control: this is where you can see the changes you have made to your project.")
	st.markdown("	Extensions: this is where you can install extensions to VS Code.")
	st.markdown("	Run and Debug: this is where you can debug your code.")
	st.markdown("**B: Side Bar: this is where you can see the different views of your project.**")
	st.markdown("**C: Editor: this is where you can see the code you have written in your project.**")
	st.markdown("**D: Panel: this is where you can see the different panels you have opened in your project.**")
	st.markdown("	Terminal: this is where you can run commands in your project.")
	st.markdown("	Output: this is where you can see the output of your code.")
	st.markdown("	Problems: this is where you can see the errors in your code.")
	st.markdown("**E. Status Bar: this is where you can see the status of your project.**")

def command_palette_indent():
	st.markdown("Python is very particular about indentation.\nUse the command palette to automatically indent your code.\n\nWindows: Ctrl-Shift-P  \nMac: Command-Shift-P\n\nSelect the option to *Convert Indentation to Tabs*")
	image = Image.open('command_palette_command.png')
	st.image(image, caption='Command Palette auto-indent command')

def final_product():
	st.write("This is what we will working towards and building by the end of the workshop today.")
	st.write("Do try out the chatbot below!")
	st.subheader("**:green[Feel the force! Yoda Chatbot]**")
	image = Image.open('yoda.jpg')
	st.image(image, caption='Master Yoda at your service')
	st.divider()

	openai.api_key = st.secrets["openapi_key"]

	prompt_template = """
	"Speak like Yoda from Star Wars for every question that was asked, 
	do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"
	"""

	if "openai_model" not in st.session_state:
		st.session_state["openai_model"] = "gpt-3.5-turbo"

	if "msg_bot" not in st.session_state:
		st.session_state.msg_bot = []

	for message in st.session_state.msg_bot:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	
	try:

		if prompt := st.chat_input("What is up?"):
			st.session_state.msg_bot.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				for response in openai.ChatCompletion.create(
					model=st.session_state["openai_model"],
					messages=[
								{"role": "system", "content": prompt_template},
								{"role": "user", "content": prompt},
							],
					stream=True,
				):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg_bot.append({"role": "assistant", "content": full_response})

	except Exception as e:
		st.error(e)
	pass

def resources():
	st.subheader("Useful resources and references")
	st.markdown("1. [Streamlit documentation](https://docs.streamlit.io/en/stable/)")
	st.markdown("2. [OpenAI API documentation](https://beta.openai.com/docs/introduction)")
	st.markdown("3. [VS Code documentation](https://code.visualstudio.com/docs)")
	st.markdown("4. [Python documentation](https://docs.python.org/3/)")
	st.markdown("5. [Python cheatsheet](https://www.pythoncheatsheet.org/)")
	st.markdown("6. [Python for beginners](https://www.python.org/about/gettingstarted/)")
	st.markdown("7. [ChatGPT](https://chat.openai.com/) - you can ask ChatGPT to generate code for you!")
	st.markdown("**Notes for this workshop course:**  \n- you may do a single click to copy all the code  \n- challenge code is hidden, click reveal to see the code")
	st.markdown("Python is very particular about indentation.\nUse the command palette to automatically indent your code.\n\nWindows: Ctrl-Shift-P  \nMac: Command-Shift-P\n\nSelect the option to *Convert Indentation to Tabs*")
	image = Image.open('command_palette_command.png')
	st.image(image, caption='Command Palette auto-indent command')

def part1_intro1():
	st.subheader("Streamlit")
	st.markdown("""
	     * an open-source Python library
	     * used extensively for machine learning and data science
	     * helps to create interactive web apps in just a few lines of code
	     * highly flexible and supports complex interactive apps with highly customisable UI
	     * Some real world examples:
	     	* CherGPT in String
	     	* Metacog for CotF MOE
	     	* AILC prototype for MOE
	     """)
	
def class1_ex1():
	st.subheader("Exercise 1: Functions")
	st.markdown("Create a new file called ***main.py*** and copy the code below into the file.")
	st.write("For this exercise, we will putting the code for *helloworld* inside a Python function")
	st.markdown("**:blue[Code]**")
	st.code('''
	import streamlit as st
	 
	 #Exercise 1: Functions
	 def ex1():
		st.write("Hello World")
	 
	 def main():
		ex1()
	 
	 if __name__ == "__main__":
		main()		
	 ''')
	st.markdown("Run the code by typing the following into the terminal:")
	st.code("streamlit run main.py")
	st.markdown("You should see the following behaviour in your browser window:")
	st.markdown("**:red[Code Output]**")
	# Exercise 1 : Functions
	st.write("Hello World")

def class1_ch1():
	pass

def class1_ex2():
	st.subheader("Exercise 2: Input , Output and Variables ")
	st.markdown("In your ***main.py***, copy the code below into the file.")
	st.markdown("**:blue[Code]**")
	st.code('''
	 # Exercise 2 : Input , Output and Variables
	 def ex2():
		name = st.text_input("Enter your name")
		# only prints the Hello {name} if input box is not empty
		if name:
			st.write("Hello " + name)
	''')
	st.write("We will now call the function *ex2()* in the main function.")
	st.code('''
	 def main():
	 	ex2()
	 
	 if __name__ == "__main__":
	 	main()
	''')
	st.markdown("You should see the following behaviour in your browser window:")
	st.markdown("**:red[Code Output]**")
	# Exercise 2 : Input , Output and Variables
	name = st.text_input("Enter your name")
	# only prints the Hello {name} if input box is not empty
	if name:
		st.write("Hello " + name)

def class1_ch2():
	st.subheader("Challenge 2: Input , Output and Variables ")
	st.markdown("""
	    Reference: [Streamlit documentation](https://docs.streamlit.io/en/stable/)\n\n
	     In the ***main.py*** file, 
	     create and append a new function called *ch2()* and call it in the main function.\n
	     In *ch2()*, modify the code in Exercise 2 to include the following:
	     * Get inputs on the name, gender and age of the user
	     * The user can select 'Male' or 'Female' from a dropdown list
	     * The output should be similar to the *Code Output* below
	    
	     Hint: You can use the st.selectbox() function to create a dropdown list
	""")
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
	  # Challenge 2 : Input , Output and Variables
	  def ch2():	  
	  	name = st.text_input("Enter your name")
		gender = st.selectbox("State your gender", ["Male", "Female"])
		age = st.text_input("State your age", 18)

		if name and gender and age:
			st.text(f"Hello {name}, you are {gender} and this year you are {age} years old")       
	 
	 def main():
		ch2()
	
	 if __name__ == "__main__":
		main()
	''')
	st.markdown("**:red[Code Output]**")
	
	# Challenge 2 (answer)
	name = st.text_input("Enter your name")
	gender = st.selectbox("State your gender", ["Male", "Female"])
	age = st.text_input("State your age", 18)

	if name and gender and age:
		st.text(f"Hello {name}, you are {gender} and this year you are {age} years old")
	pass

def class1_ex3():
	st.subheader("Exercise 3: Logical Conditioning ")
	st.markdown("Append the following code to the ***main.py*** file.")
	st.markdown("**:blue[Code]**")
	st.code('''
#Exercise 3 : Logical Conditioning
def ex3(): 
	age = st.text_input("State your age", 18)
	#if else statement
	age = int(age)
	if age >= 21:
		st.write("You are an adult")
	else:
		st.write("You are not an adult")

 def main():
	ex3()
	 
 if __name__ == "__main__":
	main()
	''')
	st.markdown("**:red[Code Output]**")
	#Exercise 2 : Logical Conditioning
	age = st.text_input("State your age", 18)
	#if else statement
	age = int(age)
	if age >= 21:
		st.write("You are an adult")
	else:
		st.write("You are not an adult")
	pass

def class1_ch3():
	st.subheader("Challenge 3: Logical Conditioning")
	st.markdown("""
	    Reference: [Streamlit documentation](https://docs.streamlit.io/en/stable/)\n\n
	     In the ***main.py*** file, 
	     create and append a new function called *ch3()* and call it in the main function.\n
	     In *ch3()*, modify the code in Exercise 2 & 3 to include the following:
	     * Get inputs on the gender and age of the user
	     * The user can select 'Male' or 'Female' from a dropdown list
	     * The user can take a picture of themselves using the st.camera_input() function
	     * The output should be similar to the *Code Output* below

	     Hint: Use *if / elif / else* statements for the logical conditions, > 21 is an adult, < 21 is a young person
	""")
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
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
 
 def main():
	ch3()
	  
 if __name__ == "__main__":
	 main()
				''')
	st.markdown("**:red[Code Output]**")
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

def class1_ex4():
	st.subheader("Exercise 4: Data and Loops ")
	st.write("We can store data in a list or dictionary and display the data using a for loop.")
	st.write("Append the following code to the ***main.py*** file. Refresh the browser to see the changes.")
	st.write("You should see output similar to the *Code Output* below.")
	st.markdown("**:blue[Code]**")
	st.code('''
	 # Exercise 4 : Data and Loops 
def ex4():
	# Data list
	fruits = ["apple", "banana", "orange"]

	# Dictionary
	person = {"name": "John", "age": 30, "city": "New York"}

	# For loop to show list
	 st.write("Fruits list:")
	for fruit in fruits:
		st.write(fruit)

	#for loop to show dictionary list
	 st.write("Person dictionary:")
	for key, value in person.items():
		st.write(key + ": " + str(value))

 def main():
	ex4()
 
 if __name__ == "__main__":
	main()
	''')
	st.markdown("**:red[Code Output]**")
	# Data list
	fruits = ["apple", "banana", "orange"]

	# Dictionary
	person = {"name": "John", "age": 30, "city": "New York"}

	# For loop to show list
	st.write("Fruits list:")
	for fruit in fruits:
		st.write(fruit)

	#for loop to show dictionary list
	st.write("Person dictionary:")
	for key, value in person.items():
		st.write(key + ": " + str(value))

def class1_ch4():
	st.subheader("Challenge 4: Data and Loops ")
	st.markdown("""
	     Add a new function called ***ch4()*** to the ***main.py*** file and call it in the main function.\n
	     In *ch4()*, modify the code in Exercise 4 to include the following:
	     * Get inputs on the name, age and gender of the user
	     * Store the inputs in a dictionary and display the dictionary\n
	     Hint:
	     * To add a value into a dictionary, you can use the following syntax:
	     """)
	st.code('''	
	 mydict["name"] = name
	 st.write(mydict)
	 ''')
	st.write("The output should look like this:")
	st.code('''
	 {
	 	"name" : "Joe",
	 	"gender" : "Male",
		"age" : 20
	 }
	 ''')
	st.write("For extra challenge, you can try to store the dictionary in a list and display the list. You can use the following syntax:")
	st.code('''
	 mylist = []
	 my_list.append(person)
	 for dict in my_list:
	 st.write(dict)
	 ''')
	st.markdown("""
	     You may need to add a submit button to check for a new dictionary entry and append it to the list each time the button is clicked.
	     In the interest of time, we will not be covering this in class. You can try it out on your own. 
	    """)
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
	  # Challenge 4 : Data and Loops
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
	
	 def main():
		ch4()
	  
	 if __name__ == "__main__":
		main()
		''')

	st.markdown("**:red[Code Output]**")
	# Challenge 4 : Data and Loops
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

#function to check age and gender        
def check_age_gender(age, gender):
	if age >= 21:
		if gender == "male":
			st.write("You are an adult male")
		elif gender == "female":
			st.write("You are an adult female")
	else:
		if gender == "male":
			st.write("You are a young boy")
		elif gender == "female":
			st.write("You are a young girl")

# def class1_ex4():
# 	st.subheader("Exercise 4: Functions")
# 	st.write("For this exercise, we will rewrite our previous code to use functions.")
# 	st.write("Append the following function to the ***main.py*** file.")
# 	st.write("Don't forget to call the new function in your code. Refresh the browser to see the changes.")
# 	st.markdown("**:blue[Code]**")
# 	st.code('''
# 	 	#Exercise 4: Functions
# 		#function to check age and gender        
# 		def check_age_gender(age, gender):
# 			if age >= 21:
# 				if gender == "male":
# 					st.write("You are an adult male")
# 				elif gender == "female":
# 					st.write("You are an adult female")
# 			else:
# 				if gender == "male":
# 					st.write("You are a young boy")
# 				elif gender == "female":
# 					st.write("You are a young girl")
				
# 		def ex4():
				
# 			st.title("Age and Gender Check")
# 			#Note that age is converted from string to int
# 			age = int(st.text_input("State your age", 18))
# 			gender = st.selectbox("Select your gender:", ["male", "female"])
# 			#calling function check_age_gender
# 			check_age_gender(age, gender)
				
# 		if __name__ == "__main__":
# 			ex4()

# 	''')
# 	st.markdown("**:red[Code Output]**")
# 	st.markdown("**Age and Gender Check**")
# 	age = int(st.text_input("State your age", 18))
# 	gender = st.selectbox("Select your gender:", ["male", "female"])
# 	#calling function check_age_gender
# 	check_age_gender(age, gender)

# def my_list_func():
# 	name = st.text_input("Enter your name")
# 	gender = st.selectbox("State your gender", ["male", "female"])
# 	age = int(st.text_input("State your age", 18))

# 	mydict = {}
# 	mydict["name"] = name
# 	mydict["gender"] = gender
# 	mydict["age"] = age

# 	check_age_gender(age, gender)
# 	st.write(mydict)
# 	return mydict

# def class1_ch4():
# 	st.subheader("Challenge 4: Functions ")
# 	st.write("For this challenge, we will rearrange our code from the previous exercise to use functions.")
# 	st.markdown("""
# 	     Remember our previous code that gets input for the user's name, gender and age, enter them into a dictionary and display the dictionary?\n
# 	     Remember our previous ***check_age_gender()*** function?
# 	     Put all the above code in a new function called ***ch4()*** and call this function as your first running function.\n
# 	     Run the code to see if it works. Refresh the browser to see the changes.\n
# 	     """)
# 	st.markdown("**:blue[Code]**")
# 	with st.expander("Reveal Code"):
# 		st.code('''
# 		# Challenge 4: Functions
# 		def my_list_func():
# 			name = st.text_input("Enter your name")
# 			gender = st.selectbox("State your gender", ["male", "female"])
# 			age = int(st.text_input("State your age", 18))

# 			mydict = {}
# 			mydict["name"] = name
# 			mydict["gender"] = gender
# 			mydict["age"] = age
	  
# 			check_age_gender(mydict["age"], mydict["gender"])
# 			st.write(mydict)

# 		def ch4():
# 			my_list_func()

# 		if __name__ == "__main__":
# 			ch4()
		
# 		''')
# 	st.markdown("**:red[Code Output]**")
# 	my_list_func()

def class1_ex5():
	st.subheader("Exercise 5: Elements of a chatbot")
	st.write("We will start creating a user interface for our first chatbot.")
	st.write("Append the following code to the ***main.py*** file.")
	st.write("You should see the output below when you run your programme.")
	st.markdown("**:blue[Code]**")
	st.code('''
	 #Exercise 5 : Chatbot UI
	def ex5():
		st.title("My first chatbot")

		if "store_msg" not in st.session_state:
			st.session_state.store_msg = []

		prompt = st.chat_input("Say something")
		if prompt:
			st.write(f"User has sent the following prompt: {prompt}")
			st.session_state.store_msg.append(prompt)
			for message in st.session_state.store_msg:
				with st.chat_message("user"):
						st.write(message)
				with st.chat_message("assistant"):
					st.write("Hello human, what can I do for you?")

	 def main():
		ex5()
	 
	 if __name__ == "__main__":
		main()
	''')
	st.markdown("**:red[Code Output]**")
	st.markdown("**My first chatbot**")

	if "store_msg" not in st.session_state:
		st.session_state.store_msg = []

	prompt = st.chat_input("Say something")
	if prompt:
		st.write(f"User has sent the following prompt: {prompt}")
		st.session_state.store_msg.append(prompt)
		for message in st.session_state.store_msg:
			with st.chat_message("user"):
					st.write(message)
			with st.chat_message("assistant"):
				st.write("Hello human, what can I do for you?")

def class1_ex6():
	st.subheader("Exercise 6: Building a simple echo chatbot")
	st.write("We will now build a simple echo chatbot.")
	st.write("Append the following code to the ***main.py*** file.")
	st.write("You should see the output below when you run your programme.")
	st.markdown("**:blue[Code]**")
	st.code('''
	 #Exercise 6 : Rule-based Echo Chatbot 
	 def ex6():
		st.title("Echo Bot")

		# Initialize chat history
		if "messages" not in st.session_state:
			st.session_state.messages = []

		# Display chat messages from history on app rerun
		for message in st.session_state.messages:
			with st.chat_message(message["role"]):
				st.markdown(message["content"])

		# React to user input
		if prompt := st.chat_input("What is up?"):
			# Display user message in chat message container
			st.chat_message("user").markdown(prompt)
			# Add user message to chat history
			st.session_state.messages.append({"role": "user", "content": prompt})

			response = f"Echo: {prompt}"
			# Display assistant response in chat message container
			with st.chat_message("assistant"):
				st.markdown(response)
			# Add assistant response to chat history
			st.session_state.messages.append({"role": "assistant", "content": response})
		
	 def main():
		ex6()
	 
	 if __name__ == "__main__":
	 	main()
	 ''')
	st.markdown("**:red[Code Output]**")
	st.markdown("**Echo Bot**")

	# Initialize chat history
	if "messages" not in st.session_state:
		st.session_state.messages = []

	# Display chat messages from history on app rerun
	for message in st.session_state.messages:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])

	# React to user input
	if prompt := st.chat_input("What is up?"):
		# Display user message in chat message container
		st.chat_message("user").markdown(prompt)
		# Add user message to chat history
		st.session_state.messages.append({"role": "user", "content": prompt})

		response = f"Echo: {prompt}"
		# Display assistant response in chat message container
		with st.chat_message("assistant"):
			st.markdown(response)
		# Add assistant response to chat history
		st.session_state.messages.append({"role": "assistant", "content": response})

def class1_ch6():
	st.subheader("Challenge 6: Rule based chatbot ")
	st.markdown("""
	     Create a new function called ***ch6()*** and modify the ***ex6()*** function to create the following rule based chatbot:\n
	     	Human : “Hello”,  Assistant: “Hi there what can I do for you”\n
	     	Human : “What is your name?”,  Assistant: “My name is EAI , an electronic artificial being”\n	
	     	Human : “How old are you?”,  Assistant: “Today is my birthday!”\n
	     For other queries, it will reply “I am sorry, I am unable to help you with your query”\n
	     Use *if / elif / else* statements to create the chatbot behaviour logic.\n 
	     You should see the output below when you run your programme.\n
	     """)
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
	  #Challenge 6 : Rule-based If-Else Chatbot
	  def ch6():
		st.title("Rule Based Bot")
	  
	  	# Initialize chat history
	  	if "messages" not in st.session_state:
		st.session_state.messages = []
	  
	  	# Display chat messages from history on app rerun
		for message in st.session_state.messages:
			with st.chat_message(message["role"]):
				st.markdown(message["content"])
			
		# React to user input
		if prompt := st.chat_input("Enter your query"):
			if prompt == "Hello":
				with st.chat_message("user"):
					st.write("Hello")
					st.session_state.messages.append({"role": "user", "content": prompt})
				with st.chat_message("assistant"):
					reply = "Hi there what can I do for you"
					st.write(reply)
					st.session_state.messages.append(
					{"role": "assistant", "content": reply}
					)

			elif prompt == "What is your name?":
				with st.chat_message("user"):
					st.write("What is your name?")
					st.session_state.messages.append({"role": "user", "content": prompt})
				with st.chat_message("assistant"):
					reply = "My name is EAI , an electronic artificial being"
					st.write(reply)
					st.session_state.messages.append(
					{"role": "assistant", "content": reply}
					)

			elif prompt == "How old are you?":
				with st.chat_message("user"):
					st.write("How old are you?")
					st.session_state.messages.append({"role": "user", "content": prompt})
				with st.chat_message("assistant"):
					reply = "Today is my birthday!"
					st.write(reply)
					st.session_state.messages.append(
					{"role": "assistant", "content": reply}
					)

			else:
				with st.chat_message("user"):
					st.write(prompt)
					st.session_state.messages.append({"role": "user", "content": prompt})
				with st.chat_message("assistant"):
					reply = "I am sorry, I am unable to help you with your query"
					st.write(reply)
					st.session_state.messages.append(
					{"role": "assistant", "content": reply}
					)
	  
	  def main():
		ch6()
	  
	  if __name__ == "__main__":
		main()
		''')
	st.markdown("**:red[Code Output]**")
	st.markdown("**Rule Based Bot**")

	# Initialize chat history
	if "messages" not in st.session_state:
		st.session_state.messages = []

	# # Display chat messages from history on app rerun
	for message in st.session_state.messages:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])

	# React to user input
	if prompt := st.chat_input("Enter your query"):
		if prompt == "Hello":
			with st.chat_message("user"):
				st.write("Hello")
				st.session_state.messages.append({"role": "user", "content": prompt})
			with st.chat_message("assistant"):
				reply = "Hi there what can I do for you"
				st.write(reply)
				st.session_state.messages.append({"role": "assistant", "content": reply})

		elif prompt == "What is your name?":
			with st.chat_message("user"):
				st.write("What is your name?")
				st.session_state.messages.append({"role": "user", "content": prompt})
			with st.chat_message("assistant"):
				reply = "My name is EAI , an electronic artificial being"
				st.write(reply)
				st.session_state.messages.append({"role": "assistant", "content": reply})

		elif prompt == "How old are you?":
			with st.chat_message("user"):
				st.write("How old are you?")
				st.session_state.messages.append({"role": "user", "content": prompt})
			with st.chat_message("assistant"):
				reply = "Today is my birthday!"
				st.write(reply)
				st.session_state.messages.append({"role": "assistant", "content": reply})

		else:
			with st.chat_message("user"):
				st.write(prompt)
				st.session_state.messages.append({"role": "user", "content": prompt})
			with st.chat_message("assistant"):
				reply = "I am sorry, I am unable to help you with your query"
				st.write(reply)
				st.session_state.messages.append({"role": "assistant", "content": reply})
	pass

def class1_ex7():
	st.subheader("Exercise 7: Secrets- Shhh ")
	st.write("In this exercise, we will learn how to hide your API key")
	st.markdown("""
	In your working directory (chatbot), create a directory called **.streamlit**\n
	Note the *dot* in front of the directory\n
	In this folder, create a file called **secrets.toml**\n
	Get an API key from your OpenAI account and type the following in **secrets.toml**:
	""")
	st.markdown("**:blue[Code]**")
	st.code('''
	openapi_key = "xxxxxx"
	''')
	#st.markdown("**:red[Code Output]**")
	pass

def class1_ch7():
	pass

def class1_ex8():
	st.subheader("Exercise 8: Calling the OpenAI LLM API")
	st.write("In this exercise, we will learn how to call the OpenAI LLM API")
	st.write("Note that there is a new import statement **import openai**")
	st.markdown("""
	     Append the following code to your **main.py** and run it.\n
	     You should see the output as shown below.\n
	     """)
	st.markdown("**:blue[Code]**")
	st.code('''
	 import openai
	 
	 #Exercise 8 : Using the OpenAI API
	 def ex8():
	 	st.title("Api Call")
		openai.api_key = st.secrets["openapi_key"]
		MODEL = "gpt-3.5-turbo"

		response = openai.ChatCompletion.create(
			model=MODEL,
			messages=[
				{"role": "system", "content": "You are a helpful assistant."},
				{"role": "user", "content": "Tell me about Singapore in the 1970s in 50 words."},
			],
			temperature=0,
		)

		st.markdown("**This is the raw response:**") 
		st.write(response)
		st.markdown("**This is the extracted response:**")
		st.write(response["choices"][0]["message"]["content"].strip())
		s = str(response["usage"]["total_tokens"])
		st.markdown("**Total tokens used:**")
		st.write(s)
	 
	 def main():
		ex8()
	 
	 if __name__ == "__main__":
		main()
	''')
	st.markdown("**:red[Code Output]**")
	st.title("Api Call")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": "Tell me about Singapore in the 1970s in 50 words."},
		],
		temperature=0,
	)
	st.markdown("**This is the raw response:**") 
	st.write(response)
	st.markdown("**This is the extracted response:**")
	st.write(response["choices"][0]["message"]["content"].strip())
	s = str(response["usage"]["total_tokens"])
	st.markdown("**Total tokens used:**")
	st.write(s)
	pass

def chat_completion(prompt):
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": prompt},
		],
		temperature=0,
	)

	return response["choices"][0]["message"]["content"].strip()

def class1_ch8():
	st.subheader("Challenge 8: Incorporate your LLM API call into your chatbot")
	st.write("In this challenge, we will incorporate the LLM API call into our previous rule-based *Echo* chatbot")
	st.markdown("""
	     Create a new function **ch8()** and copy the code from **ex6()** into it.\n
	     Now, instead of echoing the user's input, we will call the LLM API to generate a response.\n
	     First, copy the code from **ex8** into a function named **chat_completion()**.\n
	     This function should return the response from the LLM API like this:\n
	     """)
	st.code('''return response["choices"][0]["message"]["content"].strip()''')
	st.markdown("""
	     In **chat_completion()**, replace the previous *Tell me the history ..."* prompt from **ex8()** with the current user's input.\n
	     In **ch8()**, you can use the following code to call **chat_completion()**:\n
	     """)
	st.code('''
	 if prompt := st.chat.input("What's up?"):
	 	#display user messgae in chat message container
	 	reply = chat_completion(prompt) 
	 	st.chat_message("user").markdown(prompt)
		''')
	st.write("Don't forget to add the user message to the chat history!")
	st.write("You should see the code output as shown below.")
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''	
	  #Challenge 8: Incorporating the API into your chatbot
	 def chat_completion(prompt):
		openai.api_key = st.secrets["openapi_key"]
		MODEL = "gpt-3.5-turbo"
		response = openai.ChatCompletion.create(
			model=MODEL,
			messages=[
				{"role": "system", "content": "You are a helpful assistant."},
				{"role": "user", "content": prompt},
			],
			temperature=0,
		)
		return response["choices"][0]["message"]["content"].strip()
	  
	def ch8():
	  	st.title("My LLM Chatbot")

		# Initialize chat history
		if "chat_msg" not in st.session_state:
			st.session_state.chat_msg = []

		# Display chat chat_msg from history on app rerun
		for message in st.session_state.chat_msg:
			with st.chat_message(message["role"]):
				st.markdown(message["content"])

		# React to user input
		if prompt := st.chat_input("What's up?"):
			# Display user message in chat message container
			reply = chat_completion(prompt)
			st.chat_message("user").markdown(prompt)
			# Add user message to chat history
			st.session_state.chat_msg.append({"role": "user", "content": prompt})
			# Display assistant response in chat message container
			with st.chat_message("assistant"):
				st.markdown(reply)
			# Add assistant response to chat history
			st.session_state.chat_msg.append({"role": "assistant", "content": reply})
	  
	 def main():
		ch8()
	  
	 if __name__ == "__main__":
		main()

		''')
	st.markdown("**:red[Code Output]**")
	st.title("My LLM Chatbot")

	# Initialize chat history
	if "chat_msg" not in st.session_state:
		st.session_state.chat_msg = []

	# Display chat chat_msg from history on app rerun
	for message in st.session_state.chat_msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])

	# React to user input
	if prompt := st.chat_input("What is up?"):
		# Display user message in chat message container
		reply = chat_completion(prompt)
		st.chat_message("user").markdown(prompt)
		# Add user message to chat history
		st.session_state.chat_msg.append({"role": "user", "content": prompt})
		# Display assistant response in chat message container
		with st.chat_message("assistant"):
			st.markdown(reply)
		# Add assistant response to chat history
		st.session_state.chat_msg.append({"role": "assistant", "content": reply})
	pass

def class1_ex9():
	st.subheader("Exercise 9: Building a ChatGPT-like clone with streaming responses")
	st.write("Now, we will incorporate a streaming response from the LLM API into our chatbot to mimic the behaviour of ChatGPT.")
	st.write("Copy and run the code below to see the streaming responses.")
	st.markdown("**:blue[Code]**")
	st.code('''
	 #Exercise 9 : Building a ChatGPT-like clone with streaming responses
	 def ex9():
		st.title("ChatGPT-like clone")
		openai.api_key = st.secrets["openapi_key"]

		if "openai_model" not in st.session_state:
			st.session_state["openai_model"] = "gpt-3.5-turbo"

		if "msg" not in st.session_state:
			st.session_state.msg = []

		for message in st.session_state.msg:
			with st.chat_message(message["role"]):
				st.markdown(message["content"])
		try:
			if prompt := st.chat_input("What is up?"):
				st.session_state.msg.append({"role": "user", "content": prompt})
				with st.chat_message("user"):
					st.markdown(prompt)

				with st.chat_message("assistant"):
					message_placeholder = st.empty()
					full_response = ""
					for response in openai.ChatCompletion.create(
						model=st.session_state["openai_model"],
						messages=[
							{"role": m["role"], "content": m["content"]}
							for m in st.session_state.msg
						],
						stream=True,
					):
						full_response += response.choices[0].delta.get("content", "")
						message_placeholder.markdown(full_response + "▌")
					message_placeholder.markdown(full_response)
				st.session_state.msg.append({"role": "assistant", "content": full_response})
	 
	 	except Exception as e:
			st.error(e)
	 
	 def main():
		ex9()
	 
	 if __name__ == "__main__":
			main()
	''')
	st.markdown("**:red[Code Output]**")
	st.title("ChatGPT-like clone")

	openai.api_key = st.secrets["openapi_key"]

	if "openai_model" not in st.session_state:
		st.session_state["openai_model"] = "gpt-3.5-turbo"

	if "msg" not in st.session_state:
		st.session_state.msg = []

	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	
	try:

		if prompt := st.chat_input("What is up?"):
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				for response in openai.ChatCompletion.create(
					model=st.session_state["openai_model"],
					messages=[
						{"role": m["role"], "content": m["content"]}
						for m in st.session_state.msg
					],
					stream=True,
				):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})

	except Exception as e:
		st.error(e)
	pass

def class1_ch9():
	pass

def class1_ex10():
	st.subheader("Exercise 10: Basic Prompt Engineering")
	st.markdown("""
	     Now, we are going to create a chatbot with a personality by creating a default prompt for our chatbot.\n
	     Let's make it a chatbot that speaks like Yoda from Star Wars.\n
	     Copy and run the code below. You should get the same chatbot behaviour as the code output below.\n
	     Note the prompt inside the *role* that goes *Speak like Yoda ...*.\n
	     This is the default prompt that will be used for every conversation.\n
	     Try varying the temperature setting (0.0 to 1.0) to see how it affects the chatbot's response.\n
	     """)
	st.markdown("**:blue[Code]**")
	st.code('''
	 #Exercise 10: Basic prompt engineering
	 def ex10():
		st.title("Api Call")
		openai.api_key = st.secrets["openapi_key"]
		MODEL = "gpt-3.5-turbo"
		response = openai.ChatCompletion.create(
			model=MODEL,
			messages=[
				{"role": "system", "content": "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"},
				{"role": "user", "content": "Tell me about Singapore in the 1970s in 50 words"},
			],
			temperature=0,
		)
		st.markdown("**LLM Response:**")
		st.write(response["choices"][0]["message"]["content"].strip())
		st.markdown("**Total tokens:**")
		st.write(str(response["usage"]["total_tokens"]))
	 
	 def main():
			ex10()
	 
	 if __name__ == "__main__":
		main()
	''')
	st.markdown("**:red[Code Output]**")
	st.title("Api Call")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"},
			{"role": "user", "content": "Tell me about Singapore in the 1970s in 50 words"},
		],
		temperature=0,
	)
	st.markdown("**LLM Response:**")
	st.write(response["choices"][0]["message"]["content"].strip())
	st.markdown("**Total tokens:**")
	st.write(str(response["usage"]["total_tokens"]))
	pass

def class1_ch10():
	st.subheader("Challenge 10: Make your bot like someone you know!")
	st.write("Now, let's create a variable to store a prompt to make your bot speak like someone you know!")
	st.write("You can use the code below as a starter template. Note the ***prompt_template*** variable.")
	st.code('''
	for response in openai.ChatCompletion.create(
		model=st.session_state["openai_model"],
		messages=[{"role":"system", "content":prompt_template}, {"role":"user", "content":prompt}],
	''')
	st.write("Best prompt that gets the most votes win a prize!")
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
	  def ch10():
		#Challenge 10: Make the bot speak like someone you know
		st.title("ChatGPT-like clone with Prompt Engineering")

		openai.api_key = st.secrets["openapi_key"]

		prompt_template = """
		"Speak like Yoda from Star Wars for every question that was asked, 
		do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"
		"""

		if "openai_model" not in st.session_state:
			st.session_state["openai_model"] = "gpt-3.5-turbo"

		if "msg_bot" not in st.session_state:
			st.session_state.msg_bot = []

		for message in st.session_state.msg_bot:
			with st.chat_message(message["role"]):
				st.markdown(message["content"])
		
		try:

			if prompt := st.chat_input("What is up?"):
				st.session_state.msg_bot.append({"role": "user", "content": prompt})
				with st.chat_message("user"):
					st.markdown(prompt)

				with st.chat_message("assistant"):
					message_placeholder = st.empty()
					full_response = ""
					for response in openai.ChatCompletion.create(
						model=st.session_state["openai_model"],
						messages=[
									{"role": "system", "content": prompt_template},
									{"role": "user", "content": prompt},
								],
						stream=True,
					):
						full_response += response.choices[0].delta.get("content", "")
						message_placeholder.markdown(full_response + "▌")
					message_placeholder.markdown(full_response)
				st.session_state.msg_bot.append({"role": "assistant", "content": full_response})

		except Exception as e:
			st.error(e)
		
	 def main():
			ch10()
	  
	  if __name__ == "__main__":
		main()	
		''')
	st.markdown("**:red[Code Output]**")
	st.title("ChatGPT-like clone with Prompt Engineering")

	openai.api_key = st.secrets["openapi_key"]

	prompt_template = """
	"Speak like Yoda from Star Wars for every question that was asked, 
	do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"
	"""

	if "openai_model" not in st.session_state:
		st.session_state["openai_model"] = "gpt-3.5-turbo"

	if "msg_bot" not in st.session_state:
		st.session_state.msg_bot = []

	for message in st.session_state.msg_bot:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	
	try:

		if prompt := st.chat_input("What is up?"):
			st.session_state.msg_bot.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				for response in openai.ChatCompletion.create(
					model=st.session_state["openai_model"],
					messages=[
								{"role": "system", "content": prompt_template},
								{"role": "user", "content": prompt},
							],
					stream=True,
				):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg_bot.append({"role": "assistant", "content": full_response})

	except Exception as e:
		st.error(e)
	pass
