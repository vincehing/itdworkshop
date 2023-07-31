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
	st.markdown("""2. Copy the code below and paste it in the newly created main.py file.""")
	st.markdown("**:blue[Code]**")
	st.code('''
			import streamlit as st
			#my first Hello World app
			st.write("Hello World")
		''')
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

def class1_ex1():
	st.subheader("Exercise 1: Input , Output and Variables ")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
	# Exercise 1 : Input , Output and Variables
	import streamlit as st
	
	name = st.text_input("Enter your name")
	# only prints the Hello {name} if input box is not empty
	if name:
		st.write("Hello " + name)
	''')
	st.markdown("**:red[Code Output]**")
	# Exercise 1 : Input , Output and Variables
	name = st.text_input("Enter your name")
	# only prints the Hello {name} if input box is not empty
	if name:
		st.write("Hello " + name)

def class1_ch1():
	st.subheader("Challenge 1: Input , Output and Variables ")
	st.divider()
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
			# Challenge 1 (answer)
	  		import streamlit as st
	  
			name = st.text_input("Enter your name")
			gender = st.selectbox("State your gender", ["Male", "Female"])
			age = st.text_input("State your age", 18)

			if name and gender and age:
				st.text(f"Hello {name}, you are {gender} and this year you are {age} years old")       
			''')
	st.markdown("**:red[Code Output]**")
	
	# Challenge 1 (answer)
	name = st.text_input("Enter your name")
	gender = st.selectbox("State your gender", ["Male", "Female"])
	age = st.text_input("State your age", 18)

	if name and gender and age:
		st.text(f"Hello {name}, you are {gender} and this year you are {age} years old")
	pass

def class1_ex2():
	st.subheader("Exercise 2: Logical Conditioning ")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
	#Exercise 2 : Logical Conditioning
	age = 23
	#if else statement
	if age >= 18:
		st.write("You are an adult ")
	else:
		st.write("You are not an adult")
	''')
	st.markdown("**:red[Code Output]**")
	#Exercise 2 : Logical Conditioning
	age = 23
	#if else statement
	if age >= 18:
		st.write("You are an adult ")
	else:
		st.write("You are not an adult")
	pass

def class1_ch2():
	st.subheader("Challenge 2: Logical Conditioning")
	st.divider()
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
			# Challenge 2 : Logical Conditioning
			name = st.text_input("Enter your name")
			gender = st.selectbox("State your gender", ["Male", "Female"])
			age = int(st.text_input("State your age", 18))
			photo = st.camera_input("Smile! take a picture here.")

			# conditional logic to run different statements
			# All inputs and photo must be provided before any condition below is true
			if name:
				st.write("Hi " + name)
			if age >= 18 and gender == "Male" and photo:
				 st.write("You are a male adult")
				 st.image(photo)
			elif age < 18 and gender == "Male" and photo:
				 st.write("You are a young boy")
				 st.image(photo)
			elif age >= 18 and gender == "Female" and photo:
				 st.write("You are a female adult")
				 st.image(photo)
			elif age < 18 and gender == "Female" and photo:
				 st.write("You are a young girl")
				 st.image(photo)
				''')
	st.markdown("**:red[Code Output]**")
	# Challenge 2 : Logical Conditioning
	name = st.text_input("Enter your name")
	gender = st.selectbox("State your gender", ["Male", "Female"])
	age = int(st.text_input("State your age", 18))
	photo = st.camera_input("Smile! take a picture here.")

	# conditional logic to run different statements
	# All inputs and photo must be provided before any condition below is true
	if name:
		st.write("Hi " + name)
	if age >= 18 and gender == "Male" and photo:
		st.write("You are a male adult")
		st.image(photo)
	elif age < 18 and gender == "Male" and photo:
		st.write("You are a young boy")
		st.image(photo)
	elif age >= 18 and gender == "Female" and photo:
		st.write("You are a female adult")
		st.image(photo)
	elif age < 18 and gender == "Female" and photo:
		st.write("You are a young girl")
		st.image(photo)
	pass

def class1_ex3():
	st.subheader("Exercise 3: Data and Loops ")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
	# Exercise 3 : Data and Loops (part 1)
	# Data list
	fruits = ["apple", "banana", "orange"]

	# Dictionary
	person = {"name": "John", "age": 30, "city": "New York"}

	# For loop to show list
	for fruit in fruits:
		st.write(fruit)

	#for loop to show dictionary list
	for key, value in person.items():
		st.write(key + ": " + str(value))
	''')
	st.markdown("**:red[Code Output]**")
	# Exercise 3 : Data and Loops (part 1)
	# Data list
	fruits = ["apple", "banana", "orange"]

	# Dictionary
	person = {"name": "John", "age": 30, "city": "New York"}

	# For loop to show list
	for fruit in fruits:
		st.write(fruit)

	#for loop to show dictionary list
	for key, value in person.items():
		st.write(key + ": " + str(value))
		pass

def class1_ch3():
	st.subheader("Challenge 3: Data and Loops ")
	st.divider()
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
		# Challenge 3 : Data and Loops
		name = st.text_input("Enter your name")
		gender = st.selectbox("State your gender", ["Male", "Female"])
		age = st.text_input("State your age", 18)
		#declare empty dictionary 
		mydict = {}
		mydict["name"] = name
		mydict["gender"] = gender
		mydict["age"] = age
		#Print out the items in the dictionary
		st.write(mydict)
				
		 #show individual items in dictionary
		for key, value in mydict.items():
			st.write(key + ": " + str(value))

		#Extra challenge:
		mylist = []
		mylist.append(mydict)
	   
		#show dictionary items in mylist
		for dict in mylist:
			st.write(dict)

		''')
	st.markdown("**:red[Code Output]**")
	# Challenge 3 : Data and Loops
	name = st.text_input("Enter your name")
	gender = st.selectbox("State your gender", ["Male", "Female"])
	age = st.text_input("State your age", 18)
	#declare empty dictionary 
	mydict = {}
	mydict["name"] = name
	mydict["gender"] = gender
	mydict["age"] = age

	st.write(mydict)

	#show individual items in dictionary
	for key, value in mydict.items():
		st.write(key + ": " + str(value))

	#Extra challenge:
	mylist = []
	mylist.append(mydict)

	#show dictionary items in mylist
	for dict in mylist:
		st.write(dict)
	pass

#function to check age and gender        
def check_age_gender(age, gender):

	if age >= 18:
		if gender == "male":
			st.write("You are an adult male")
		elif gender == "female":
			st.write("You are an adult female")
	else:
		if gender == "male":
			st.write("You are a young boy")
		elif gender == "female":
			st.write("You are a young girl")


def class1_ex4():
	st.subheader("Exercise 4: Functions")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
		#function to check age and gender        
		def check_age_gender(age, gender):
				
			if age >= 18:
				if gender == "male":
					st.write("You are an adult male")
				elif gender == "female":
					st.write("You are an adult female")
			else:
				if gender == "male":
					st.write("You are a young boy")
				elif gender == "female":
					st.write("You are a young girl")
				
		#main program function, optional but it is a good coding practise in python application
				
		def main():
				
			st.title("Age and Gender Check")
			#Note that age is converted from string to int
			age = int(st.text_input("State your age", 18))
			gender = st.selectbox("Select your gender:", ["male", "female"])
			#calling function check_age_gender
			check_age_gender(age, gender)
				
		if __name__ == "__main__":
			main()

	''')
	st.markdown("**:red[Code Output]**")
	st.title("Age and Gender Check")
	age = int(st.text_input("State your age", 18))
	gender = st.selectbox("Select your gender:", ["male", "female"])
	#calling function check_age_gender
	check_age_gender(age, gender)
	pass


def my_list_func():
	name = st.text_input("Enter your name")
	gender = st.selectbox("State your gender", ["male", "female"])
	age = int(st.text_input("State your age", 18))

	mydict = {}
	mydict["name"] = name
	mydict["gender"] = gender
	mydict["age"] = age

	check_age_gender(age, gender)
	st.write(mydict)
	return mydict

def class1_ch4():
	st.subheader("Challenge 4: Functions ")
	st.divider()
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''

		def my_list_func():
			name = st.text_input("Enter your name")
			gender = st.selectbox("State your gender", ["male", "female"])
			age = int(st.text_input("State your age", 18))

			mydict = {}
			mydict["name"] = name
			mydict["gender"] = gender
			mydict["age"] = age
			check_age_gender(mydict["age"], mydict["gender"])
			st.write(mydict)


		def main():
			my_list_func()

		if __name__ == "__main__":
			main()
		
		''')
	st.markdown("**:red[Code Output]**")
	my_list_func()
	pass

def class1_ex5():
	st.subheader("Exercise 5: Elements of a chatbot")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
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
	''')
	st.markdown("**:red[Code Output]**")
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
	pass

def class1_ex6():
	st.subheader("Exercise 6: Building a simple echo chatbot")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
	import streamlit as st

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
	''')
	st.markdown("**:red[Code Output]**")
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
	pass

def class1_ch6():
	st.subheader("Challenge 6: Rule based chatbot ")
	st.divider()
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
					import streamlit as st

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
		''')
	st.markdown("**:red[Code Output]**")
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
	st.divider()
	st.markdown("""
	In your working directory (chatbot)
	Using VS create a directory called (.streamlit)*Note the dot in front of the directory
	Create a file called secrets.toml
	Get an API key from your OpenAI account and type this in secrets.toml
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
	st.subheader("Exercise 8: Calling OpenAI LLM API")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
		import streamlit as st
		import openai

		st.title("Api Call")
		openai.api_key = st.secrets["openapi_key"]
		MODEL = "gpt-3.5-turbo"

		response = openai.ChatCompletion.create(
			model=MODEL,
			messages=[
				{"role": "system", "content": "You are a helpful assistant."},
				{"role": "user", "content": "Tell me about Singapore in the 1970s"},
			],
			temperature=0,
		)

  		st.write("Raw results: ") 
		st.write(response)
		st.write("LLM Response: " + response["choices"][0]["message"]["content"].strip())
		st.write("Total tokens: " + str(response["usage"]["total_tokens"]))
	''')
	st.markdown("**:red[Code Output]**")
	st.title("Api Call")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": "Tell me about Singapore in the 1970s in 50 words"},
		],
		temperature=0,
	)
	st.write("Raw results: ") 
	st.write(response)
	st.write("LLM Response: " + response["choices"][0]["message"]["content"].strip())
	st.write("Total tokens: " + str(response["usage"]["total_tokens"]))
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
	st.divider()
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
	import streamlit as st
	import openai
	st.title("My LLM Chatbot")
	
	#create chat_completion function
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
	def main():
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
	st.subheader("Exercise 9: Building a ChatGPT clone ")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
	import openai
	import streamlit as st

	st.title("ChatGPT-like clone")
	
	def main():

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
	st.subheader("Exercise 10: Prompt Engineering")
	st.divider()
	st.markdown("**:blue[Code]**")
	st.code('''
	import streamlit as st
	import openai
	 
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
	st.write("Raw results: ") 
	st.write(response)
	st.write("LLM Response: " + response["choices"][0]["message"]["content"].strip())
	st.write("Total tokens: " + str(response["usage"]["total_tokens"]))
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
	st.write("Raw results: ") 
	st.write(response)
	st.write("LLM Response: " + response["choices"][0]["message"]["content"].strip())
	st.write("Total tokens: " + str(response["usage"]["total_tokens"]))
	pass

def class1_ch10():
	st.subheader("Challenge 10: Make your bot like someone you know!")
	st.divider()
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
	import streamlit as st
	import openai
	  
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
