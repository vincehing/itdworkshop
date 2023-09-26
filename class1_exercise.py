from PIL import Image
import streamlit as st
import openai
#exercise 11
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#exercis 12
from langchain.memory import ConversationBufferWindowMemory
#exercise 13
from langchain.document_loaders import TextLoader,PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import LanceDB
import lancedb
import os
import tempfile
#exercise 15
import sqlite3
import pandas as pd
import datetime
#exercise 16
from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.tools import DuckDuckGoSearchRun
#Exercise 17
from langchain.agents import tool
import json
#Exercise 18
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt

#Global ex 13
cwd = os.getcwd()
WORKING_DIRECTORY = os.path.join(cwd, "database")

if not os.path.exists(WORKING_DIRECTORY):
	os.makedirs(WORKING_DIRECTORY)
#ex15
DB_NAME = os.path.join(WORKING_DIRECTORY, "default_db")

def template():
	st.subheader("Template")
	st.write("Instruction lines.")

	st.markdown("**:blue[Code]**")
	st.code('''
#exercise code here
''')
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
#challenge code here
''')	  
	st.markdown("**:red[Code Output]**")
	# Actual code here

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
	name = st.text_input("Enter your name")
	if name:
		st.write("Hello " + name)
	 
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
	# only prints the Hello {name} if input box is not empty
	name = st.text_input("Enter your name")
	if name:
		st.write("Hello " + name)

def class1_ch1():
	pass

def class1_ex2_old():
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

def class1_ex2():
	st.subheader("Exercise 2: The Streamlit sidebar")
	st.markdown("In your ***main.py***, copy the code below into the file.")
	st.markdown("**:blue[Code]**")
	st.code('''
# Exercise 2 : Streamlit sidebar
def ex2():
	placeholder = st.empty()
	
	with st.sidebar:
		option = st.selectbox("My sidebar", ["", "Option 1", "Option 2"])

	if option == "Option 1":
		with placeholder.container():
			st.write("You selected option 1")
	elif option == "Option 2":
		with placeholder.container():
			st.write("You selected option 2")
	else:
		st.write("Please select an option from the sidebar")
''')
	st.write("Refresh the browser to see the changes.")

	st.markdown("You should see the following selectbox in the sidebar on the left:")
	st.markdown("**:red[Code Output]**")
	
	my_option = st.selectbox("My sidebar", ["", "Option 1", "Option 2"])
	if my_option == "Option 1":
		st.write("You selected option 1")
	elif my_option == "Option 2":
		st.write("You selected option 2")
	else:
		st.write("Please select an option from the sidebar")

def class1_ch2():
	st.subheader("Challenge 2: The Streamlit sidebar ")
	st.markdown("""Copy the code for ***ex2()*** and paste in the ***main()*** function. Change the title to ***Code Exercises*** and name the options ***ex1()***, ***ex2()***, and so on.""")
	st.write("This way, just by selecting the options in the sidebar, you can run the different exercises.")
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
def main():
	placeholder = st.empty()
		 
	with st.sidebar:
		option = st.selectbox("Code Exercises", ["", "ex1()", "ex2()", "ex3()"])
	
	if option == "ex1":
		with placeholder.container():
			ex1()
	
	elif option == "ex2":
		with placeholder.container():
			ex2()
		  
	elif option == "ex3":
		with placeholder.container():
			ex3()
''')

def class1_ex3_old():
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

def class1_ex3():
	st.subheader("Exercise 3: Data and Loops ")
	st.write("We can store data in a list or dictionary and display the data using a for loop.")
	st.write("Append the following code to the ***main.py*** file. Refresh the browser to see the changes.")
	st.write("You should see output similar to the *Code Output* below.")
	st.markdown("**:blue[Code]**")
	st.code('''
#Exercise 3 : Data and Loops 
def ex3():
	# Data list
	fruits = ["apple", "banana", "orange"]

	# For loop to show list
	st.subheader("Fruits list:")
	for fruit in fruits:
		st.write(fruit)

	# Dictionary
	person = {"name": "John", "age": 30, "city": "New York"}
		 
	# Print out the items in the dictionary
	st.write("Here is your dictionary: ")
	st.write(person)

	# for loop to show dictionary list
	st.write("You can also show individual items in the dictionary like this: ")
	for key, value in person.items():
		st.write(key + ": " + str(value))
''')
	st.markdown("**:red[Code Output]**")
	# Data list
	fruits = ["apple", "banana", "orange"]

	# For loop to show list
	for fruit in fruits:
		st.write(fruit)

	# Dictionary
	person = {"name": "John", "age": 30, "city": "New York"}

	# Print out the items in the dictionary
	st.write("Here is your dictionary: ")
	st.write(person)

	# for loop to show dictionary list
	st.write("You can also show individual items in the dictionary like this: ")
	for key, value in person.items():
		st.write(key + ": " + str(value))

def ex4a():
	st.subheader("Session Data:")
	if "session_data" not in st.session_state:
		st.session_state.session_data = ["alpha", "omega"]
	
	if "name" not in st.session_state:
		st.session_state.name = ""
	
	if "age" not in st.session_state:
		st.session_state.age = ""

	if "gender" not in st.session_state:
		st.session_state.gender = ""
	
	# For loop to show list
	for data in st.session_state.session_data:
		st.write("session_data: ", data)

	st.write("name: ", st.session_state.name)
	st.write("age: ", st.session_state.age)
	st.write("gender: ", st.session_state.gender)

def class1_ex4a():
	st.subheader("Exercise 4: Session Data")
	st.write("We can create variables to store data in a user session. Session data persist within a user session.")

	st.markdown("**:blue[Code]**")
	st.code('''
# Exercise 4: Session State
def ex4a():
	st.subheader("Session Data:")
	if "session_data" not in st.session_state:
		st.session_state.session_data = ["alpha", "omega"]
	
	if "name" not in st.session_state:
		st.session_state.name = ""
	
	if "age" not in st.session_state:
		st.session_state.age = ""

	if "gender" not in st.session_state:
		st.session_state.gender = ""
	
	# For loop to show list
	for data in st.session_state.session_data:
		st.write("session_data: ", data)

	st.write("name: ", st.session_state.name)
	st.write("age: ", st.session_state.age)
	st.write("gender: ", st.session_state.gender)
''')
		 
	st.markdown("**:red[Code Output]**")
	ex4a()

def ex4b():
	st.subheader("Session Data:")
	userName = st.text_input("Enter your name")
	userAge = st.text_input("State your age")
	userGender = st.selectbox("State your gender", ["", "Male", "Female"])

	if userName:
		st.session_state.name = userName
		st.write("name: ", st.session_state.name)
	if userAge:
		st.session_state.age = int(userAge)
		st.write("age: ", st.session_state.age)
	if userGender:
		st.session_state.gender = userGender
		st.write("gender: ", st.session_state.gender)

def class1_ex4b():
	st.subheader("Session Data")
	st.write("Lets now get input from the user and store it in the session data.")
	st.write("Now run *ex4a()* again to check the session data. Note that it persists.")

	st.markdown("**:blue[Code]**")
	st.code('''
def ex4b():
	st.subheader("Session Data:")
	userName = st.text_input("Enter your name")
	userAge = st.text_input("State your age")
	userGender = st.selectbox("State your gender", ["", "Male", "Female"])

	if userName:
		st.session_state.name = userName
		st.write("name: ", st.session_state.name)
	if userAge:
		st.session_state.age = int(userAge)
		st.write("age: ", st.session_state.age)
	if userGender:
		st.session_state.gender = userGender
		st.write("gender: ", st.session_state.gender)
''')
	st.markdown("**:red[Code Output]**")
	ex4b()

def class1_ch4():
	st.subheader("Challenge 4: Session Data")
	st.markdown("""
		 Add a new function called ***ch4()*** to the ***main.py*** file and call it in the main function.\n
		 In *ch4()*, modify the code in Exercise 4b to include the following:
		 * Create session data for ***name***, ***age*** and ***gender***
		 * Create session data for ***prompt_template*** with the following value:
			 "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"
		 * Include this code in ***main*** as well, because we need the session data for later exercises.\n
		 Hint:
		 * To check that the session data is created, you can print out the session data using ***st.write()***:
		 """)
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
def ch4():
	if "name" not in st.session_state:
		st.session_state.name = "Yoda"

	if "age" not in st.session_state:
		st.session_state.age = 999

	if "gender" not in st.session_state:
		st.session_state.gender = "male"

	if "prompt_template" not in st.session_state:
		st.session_state.prompt_template = "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"

	st.write("session_state.name: ", st.session_state.name)
	st.write("session_state.age: ", st.session_state.age)
	st.write("session_state.gender: ", st.session_state.gender)
	st.write("session_state.prompt_template: ", st.session_state.prompt_template)

def main():
	# initialize session state, from ch4
	if "name" not in st.session_state:
		st.session_state.name = "Yoda"

	if "age" not in st.session_state:
		st.session_state.age = 999

	if "gender" not in st.session_state:
		st.session_state.gender = "male"

	if "prompt_template" not in st.session_state:
		st.session_state.prompt_template = "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"
		  
	#the rest of your code is below
''')
		  
	st.markdown("**:red[Code Output]**")
	if "name" not in st.session_state:
		st.session_state.name = "Yoda"

	if "age" not in st.session_state:
		st.session_state.age = 999

	if "gender" not in st.session_state:
		st.session_state.gender = "male"

	if "prompt_template" not in st.session_state:
		st.session_state.prompt_template = "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"

	st.write("session_state.name: ", st.session_state.name)
	st.write("session_state.age: ", st.session_state.age)
	st.write("session_state.gender: ", st.session_state.gender)
	st.write("session_state.prompt_template: ", st.session_state.prompt_template)

def class1_ex4_old():
	# st.subheader("Exercise 4: Functions")
	# st.write("For this exercise, we will rewrite our previous code to use functions.")
	# st.write("Append the following function to the ***main.py*** file.")
	# st.write("Don't forget to call the new function in your code. Refresh the browser to see the changes.")
	# st.markdown("**:blue[Code]**")
	# st.code('''
	#  	#Exercise 4: Functions
	# 	#function to check age and gender        
	# 	def check_age_gender(age, gender):
	# 		if age >= 21:
	# 			if gender == "male":
	# 				st.write("You are an adult male")
	# 			elif gender == "female":
	# 				st.write("You are an adult female")
	# 		else:
	# 			if gender == "male":
	# 				st.write("You are a young boy")
	# 			elif gender == "female":
	# 				st.write("You are a young girl")
				
	# 	def ex4():
				
	# 		st.title("Age and Gender Check")
	# 		#Note that age is converted from string to int
	# 		age = int(st.text_input("State your age", 18))
	# 		gender = st.selectbox("Select your gender:", ["male", "female"])
	# 		#calling function check_age_gender
	# 		check_age_gender(age, gender)
				
	# 	if __name__ == "__main__":
	# 		ex4()

	# ''')
	# st.markdown("**:red[Code Output]**")
	# st.markdown("**Age and Gender Check**")
	# age = int(st.text_input("State your age", 18))
	# gender = st.selectbox("Select your gender:", ["male", "female"])
	# #calling function check_age_gender
	# check_age_gender(age, gender)
	pass

def my_list_func():
	pass
	# name = st.text_input("Enter your name")
	# gender = st.selectbox("State your gender", ["male", "female"])
	# age = int(st.text_input("State your age", 18))

	# mydict = {}
	# mydict["name"] = name
	# mydict["gender"] = gender
	# mydict["age"] = age

	# check_age_gender(age, gender)
	# st.write(mydict)
	# return mydict

def class1_ch4_old():
	st.subheader("Challenge 4: Functions ")
	st.write("For this challenge, we will rearrange our code from the previous exercise to use functions.")
	st.markdown("""
		 Remember our previous code that gets input for the user's name, gender and age, enter them into a dictionary and display the dictionary?\n
		 Remember our previous ***check_age_gender()*** function?
		 Put all the above code in a new function called ***ch4()*** and call this function as your first running function.\n
		 Run the code to see if it works. Refresh the browser to see the changes.\n
		 """)
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
		# Challenge 4: Functions
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

		def ch4():
			my_list_func()

		if __name__ == "__main__":
			ch4()
		
		''')
	st.markdown("**:red[Code Output]**")
	my_list_func()

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
		 * Human : “Hello”,  Assistant: “Hi there what can I do for you”\n
		 * Human : “What is your name?”,  Assistant: “My name is EAI , an electronic artificial being”\n	
		 * Human : “How old are you?”,  Assistant: “Today is my birthday!”\n
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
	st.title("My first LLM Chatbot")

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

#For exercise 9
def chat_completion_stream(prompt):
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "You are a helpful assistant"},
			{"role": "user", "content": prompt},
		],
		temperature=0,  # temperature
		stream=True,  # stream option
	)
	return response

def ex9_basebot():
	# Initialize chat history
	if "chat_msg" not in st.session_state:
		st.session_state.chat_msg = []

	# Showing Chat history
	for message in st.session_state.chat_msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			# set user prompt in chat history
			st.session_state.chat_msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				# streaming function
				for response in chat_completion_stream(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.chat_msg.append(
				{"role": "assistant", "content": full_response}
			)

	except Exception as e:
		st.error(e)

def class1_ex9():
	st.subheader("Exercise 9: Building a ChatGPT-like clone with streaming responses")
	st.write("Now, we will incorporate a streaming response from the LLM API into our chatbot to mimic the behaviour of ChatGPT.")
	st.write("Copy and run the code below to see the streaming responses.")
	st.markdown("**:blue[Code]**")
	st.code('''
# Exercise 9 : Using the OpenAI API with streaming option
def chat_completion_stream(prompt):
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "You are a helpful assistant"},
			{"role": "user", "content": prompt},
		],
		temperature=0,  # temperature
		stream=True,  # stream option
	)
	return response


# integration API call into streamlit chat components
def ex9_basebot():
	# Initialize chat history
	if "chat_msg" not in st.session_state:
		st.session_state.chat_msg = []

	# Showing Chat history
	for message in st.session_state.chat_msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			# set user prompt in chat history
			st.session_state.chat_msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				# streaming function
				for response in chat_completion_stream(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.chat_msg.append(
				{"role": "assistant", "content": full_response}
			)

	except Exception as e:
		st.error(e)
''')
	st.markdown("**:red[Code Output]**")
	ex9_basebot()

def class1_ch9():
	pass

def class1_ex10():
	st.subheader("Exercise 10: Basic Prompt Engineering")
	st.markdown("""
		 Now, we are going to create a chatbot with a personality by using a default prompt for our chatbot. \n
		 This is the default prompt that will be used for every conversation.\n
		 Let's make it a chatbot that speaks like Yoda from Star Wars.\n
		 We will use the ***prompt_template*** that is already in our ***main()*** for this.
		 """)
	st.code('''
if "prompt_template" not in st.session_state:
	st.session_state.prompt_template = "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"
	''')
	st.markdown("""
		 Copy and run the code below. You should get the same chatbot behaviour as the code output below.\n
		 Try varying the temperature setting (0.0 to 1.0) to see how it affects the chatbot's response.\n
		 """)
	st.markdown("**:blue[Code]**")
	st.code('''
# Exercise 10: Basic prompt engineering
def ex10():
	#prompt_template in session state already set in main()
	st.title("Api Call")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": st.session_state.prompt_template},
			{
				"role": "user",
				"content": "Tell me about Singapore in the 1970s in 50 words",
			},
		],
		temperature=0,
	)
	st.markdown("**LLM Response:**")
	st.write(response["choices"][0]["message"]["content"].strip())
	st.markdown("**Total tokens:**")
	st.write(str(response["usage"]["total_tokens"]))
''')
	st.markdown("**:red[Code Output]**")
	#prompt_template in session state already set in main()
	st.title("Api Call")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": st.session_state.prompt_template},
			{
				"role": "user",
				"content": "Tell me about Singapore in the 1970s in 50 words",
			},
		],
		temperature=0,
	)
	st.markdown("**LLM Response:**")
	st.write(response["choices"][0]["message"]["content"].strip())
	st.markdown("**Total tokens:**")
	st.write(str(response["usage"]["total_tokens"]))

#Challenge 10
#mod chat complete stream function by replacing system content to session_state prompt template
def chat_completion_stream_prompt(prompt):
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo" #consider changing this to session_state
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": st.session_state.prompt_template},
			{"role": "user", "content": prompt},
		],
		temperature= 0, # temperature
		stream=True #stream option
	)
	return response

# Challenge 10: Make the bot speak like someone you know
def ch10_basebot():
	if my_prompt_template := st.text_input("Enter a system prompt template. E.g. Speak like Yoda from Star Wars."):
		st.session_state.prompt_template = my_prompt_template
		st.write("new prompt template set! ", st.session_state.prompt_template)

  #call the function in your base bot
	#Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	#Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			#set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				#streaming function
				for response in chat_completion_stream_prompt(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})

	except Exception as e:
		st.error(e)

def class1_ch10():
	st.subheader("Challenge 10: Make your bot like someone you know!")
	st.write("Now, let's create your own prompt to make your bot speak like someone you know!") 
	st.write("Modify the ***prompt_template*** in your ***main()*** to your own liking.")
	st.write("Be imaginative!")
	st.write("You can use the streaming chat_completion function you wrote earlier.")
	st.write("Don't forget to replace the system prompt with your own prompt_template!")
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
#Challenge 10
#mod chat complete stream function by replacing system content to session_state prompt template
def chat_completion_stream_prompt(prompt):
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo" #consider changing this to session_state
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": st.session_state.prompt_template},
			{"role": "user", "content": prompt},
		],
		temperature= 0, # temperature
		stream=True #stream option
	)
	return response

# Challenge 10: Make the bot speak like someone you know
def ch10_basebot():
	if my_prompt_template := st.text_input("Enter a system prompt template. E.g. Speak like Yoda from Star Wars."):
		st.session_state.prompt_template = my_prompt_template
		st.write("new prompt template set! ", st.session_state.prompt_template)

	# call the function in your base bot
	# Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	# Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			#set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				#streaming function
				for response in chat_completion_stream_prompt(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})

	except Exception as e:
		st.error(e)
''')
	st.markdown("**:red[Code Output]**")
	st.title("ChatGPT-like clone with Prompt Engineering")

	ch10_basebot()

#https://python.langchain.com/docs/modules/chains/
def ex11a(): #change in ex11a
	#langchain prompt template
	os.environ['OPENAI_API_KEY'] = st.secrets["openapi_key"]
	prompt = PromptTemplate(
		input_variables=["subject", "topic"],
		template="""Design a lesson plan on {subject} on the topic of {topic} for primary 1 students"""
		)
	
	openai_api_key = st.secrets["openapi_key"]
	llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True, max_tokens=100, temperature=0.9)
	
	#creating a LLM chain with the langchain call and prompt template
	chain = LLMChain(llm=llm, prompt=prompt)
	if st.button("Run my chain"):
		input_prompt = prompt.format(subject="English", topic="Verbs")
		#Showing what is sent to LLM Chain
		st.write("Input prompt: ", input_prompt)
		#Showing the output from LLM Chain
		st.write(chain.run({
							'subject': "English",
							'topic': "Verbs"
							}))
		
def class1_ex11a():
	st.subheader("Exercise 11a: Prompt Template with LangChain")
	st.write("LangChain helps you to create a more complext prompt template for your chatbot.")

	st.markdown("**:blue[Code]**")
	st.code('''
#https://python.langchain.com/docs/modules/chains/
def ex11a(): #change in ex11a
	#langchain prompt template
	os.environ['OPENAI_API_KEY'] = st.secrets["openapi_key"]
	prompt = PromptTemplate(
		input_variables=["subject", "topic"],
		template="""Design a lesson plan on {subject} on the topic of {topic} for primary 1 students"""
		)
	
	openai_api_key = st.secrets["openapi_key"]
	llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True, max_tokens=100, temperature=0.9)
	
	#creating a LLM chain with the langchain call and prompt template
	chain = LLMChain(llm=llm, prompt=prompt)
	if st.button("Run my chain"):
		input_prompt = prompt.format(subject="English", topic="Verbs")
		#Showing what is sent to LLM Chain
		st.write("Input prompt: ", input_prompt)
		#Showing the output from LLM Chain
		st.write(chain.run({
							'subject': "English",
							'topic': "Verbs"
							}))
''')
	st.markdown("**:red[Code Output]**")
	#actual code here
	ex11a()

def prompt_inputs_form(): #Using st.form, create the starting prompt to your prompt template, this is an expert on a topic that is talking to a user of a certain age
	#langchain prompt template
	os.environ['OPENAI_API_KEY'] = st.secrets["openapi_key"]
	with st.form("Prompt Template"):
		occupation = st.text_input("Enter the occupation:")
		topic = st.text_input("Enter the topic:")
		age = st.text_input("Enter the age:")

	# Every form must have a submit button.
		submitted = st.form_submit_button("Submit")
	#return a dictionary of the values
	if submitted:
		return {
			'occupation': occupation,
			'topic': topic,
			'age': age
		}

def ex11b():
	#create your template 
	prompt_template = PromptTemplate(
				input_variables=["occupation", "topic", "age"],
				template="""Imagine you are a {occupation} who is an expert on the  topic of {topic} , you are going to help , teach and provide information
						to the person who is {age} years old, if you do not not know the answer, you must tell the person , do not make any answer up"""
				)
	#create a langchain function call to openai
	openai_api_key = st.secrets["openapi_key"]
	llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True, max_tokens=100, temperature=0.9)	#create a LLM chain with the langchain call and prompt template 
	chain = LLMChain(llm=llm, prompt=prompt_template)
	#call the prompt_inputs_form()
	dict_inputs = prompt_inputs_form()
	if dict_inputs:
		st.write(chain.run(dict_inputs))

def class1_ex11b():
	st.subheader("Exercise 11b")
	st.write("Now, we will create a chatbot with a prompt template that is more complex.")
	st.write("We will use the ***prompt_inputs_form()*** function to get the user's input for the prompt template.")
	st.write("Copy and run the code below to see the chatbot in action.")

	st.markdown("**:blue[Code]**")
	st.code('''
def prompt_inputs_form(): #Using st.form, create the starting prompt to your prompt template, this is an expert on a topic that is talking to a user of a certain age
	#langchain prompt template
	os.environ['OPENAI_API_KEY'] = st.secrets["openapi_key"]
	with st.form("Prompt Template"):
		occupation = st.text_input("Enter the occupation:")
		topic = st.text_input("Enter the topic:")
		age = st.text_input("Enter the age:")

	# Every form must have a submit button.
		submitted = st.form_submit_button("Submit")
	#return a dictionary of the values
	if submitted:
		return {
			'occupation': occupation,
			'topic': topic,
			'age': age
		}

def ex11b():
	#create your template
	prompt_template = PromptTemplate(
				input_variables=["occupation", "topic", "age"],
				template="""Imagine you are a {occupation} who is an expert on the  topic of {topic} , you are going to help , teach and provide information
						to the person who is {age} years old, if you do not not know the answer, you must tell the person , do not make any answer up"""
				)
	#create a langchain function call to openai
	openai_api_key = st.secrets["openapi_key"]
	llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True, max_tokens=100, temperature=0.9)	#create a LLM chain with the langchain call and prompt template 
	chain = LLMChain(llm=llm, prompt=prompt_template)
	#call the prompt_inputs_form()
	dict_inputs = prompt_inputs_form()
	if dict_inputs:
		st.write(chain.run(dict_inputs))
''')
	
	st.markdown("**:red[Code Output]**")
	# Actual code here
	ex11b()

def ch11():
	#instead of running of the langchain, we are going to use the prompt template and run it the chatbot using format
	prompt_template = PromptTemplate(
				input_variables=["occupation", "topic", "age"],
				template="""Imagine you are a {occupation} who is an expert on the  topic of {topic} , you are going to help , teach and provide information to the person who is {age} years old, if you do not not know the answer, you must tell the person , do not make any answer up"""
				)
	dict_inputs = prompt_inputs_form()
	if dict_inputs:
		input_prompt = prompt_template.format(occupation=dict_inputs["occupation"], topic=dict_inputs["topic"], age=dict_inputs["age"])
		# set session_state.prompt_template 
		st.session_state.prompt_template = input_prompt
		st.write("New session_state.prompt_template: ", input_prompt)
	# call ch10_basebot() with the new session_state.prompt_template
	ch10_basebot()

def class1_ch11():
	st.subheader("Challenge 11: Prompt Template with LangChain")
	st.write("Now, let's incorporate the prompt template into our chatbot from the previous exercise.")
	st.write("We will use the ***prompt_inputs_form()*** function to get the user's input for the prompt template.")
	st.write("You can use the ***ch10_basebot()*** function from the previous exercise to do the llm api call with the updated session_state.prompt_template.")
	st.write("Ignore the text input field that asks for a system prompt template from ch10_basebot(), since we will be using the prompt template from the user's input.")
	st.write("As you interact with the chatbot, observe that the prompt template is updated with the latest user input as seen from the code output.")

	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
def ch11():
	#instead of running of the langchain, we are going to use the prompt template and run it the chatbot using format
	prompt_template = PromptTemplate(
				input_variables=["occupation", "topic", "age"],
				template="""Imagine you are a {occupation} who is an expert on the  topic of {topic} , you are going to help , teach and provide information to the person who is {age} years old, if you do not not know the answer, you must tell the person , do not make any answer up"""
				)
	dict_inputs = prompt_inputs_form()
	if dict_inputs:
		input_prompt = prompt_template.format(occupation=dict_inputs["occupation"], topic=dict_inputs["topic"], age=dict_inputs["age"])
		# set session_state.prompt_template 
		st.session_state.prompt_template = input_prompt
		st.write("New session_state.prompt_template: ", input_prompt)
	# call ch10_basebot() with the new session_state.prompt_template
	ch10_basebot()
''')
		  
	st.markdown("**:red[Code Output]**")
	# actual code here
	ch11()

def ex12():
	memory = ConversationBufferWindowMemory(k=3)
	memory.save_context({"input": "hi"}, {"output": "whats up?"})
	memory.save_context({"input": "not much"}, {"output": "what can I help you with?"})

	st.write(memory.load_memory_variables({}))
   
	memory = ConversationBufferWindowMemory( k=3, return_messages=True)
	memory.save_context({"input": "hi"}, {"output": "whats up?"})
	memory.save_context({"input": "not much"}, {"output": "what can I help you with?"})

	st.write(memory.load_memory_variables({}))

def class1_ex12():
	st.subheader("Exercise 12: Chatbot with memory")
	st.write("Now, we will create a chatbot with memory.")
	st.write("You can determine the number of previous messages to remember by setting the ***k*** parameter.")

	st.markdown("**:blue[Code]**")
	st.code('''
def ex12():
	memory = ConversationBufferWindowMemory(k=3)
	memory.save_context({"input": "hi"}, {"output": "whats up?"})
	memory.save_context({"input": "not much"}, {"output": "what can I help you with?"})

	st.write(memory.load_memory_variables({}))
   
	memory = ConversationBufferWindowMemory( k=3, return_messages=True)
	memory.save_context({"input": "hi"}, {"output": "whats up?"})
	memory.save_context({"input": "not much"}, {"output": "what can I help you with?"})

	st.write(memory.load_memory_variables({}))
''')  
	st.markdown("**:red[Code Output]**")
	#actual code here
	ex12()

def ch12():
	#Prompt_template form from ex11
	prompt_template = PromptTemplate(
				input_variables=["occupation", "topic", "age"],
				template="""Imagine you are a {occupation} who is an expert on the  topic of {topic} , you are going to help , teach and provide information
						to the person who is {age} years old, if you do not not know the answer, you must tell the person , do not make any answer up"""
				)
	dict_inputs = prompt_inputs_form()
	if dict_inputs:
		input_prompt = prompt_template.format(occupation =dict_inputs["occupation"], topic=dict_inputs["topic"], age=dict_inputs["age"])
	else:
		input_prompt = "You are a helpful assistant. "

	st.write("input prompt: ", input_prompt)

	if "memory" not in st.session_state:
		st.session_state.memory = ConversationBufferWindowMemory(k=3)

	#step 1 save the memory from your chatbot 
	#step 2 integrate the memory in the prompt_template (st.session_state.prompt_template) show a hint
	memory_data = st.session_state.memory.load_memory_variables({})
	st.write("Memory Data: ", memory_data)
	st.session_state.prompt_template = f"""{input_prompt}\n\nBelow is the conversation history between the AI and Users so far\n\n{memory_data}
										"""

	st.write("New prompt template: \n", st.session_state.prompt_template)
	#call the function in your base bot
	#Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	#Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			#set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				#streaming function
				for response in chat_completion_stream_prompt(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})
			st.session_state.memory.save_context({"input": prompt}, {"output": full_response})

	except Exception as e:
		st.error(e)
	pass

def class1_ch12():
	st.subheader("Challenge 12: Chatbot with memory")
	st.write("Now, let's incorporate the memory into the session state prompt template.")
	st.write("The chatbot should remember the previous user input and use it as the prompt template for the next conversation.")
	st.write("Start with the following code and modify ex12() to create a chatbot with memory.")
	st.write("Get the *{input_prompt}* using *prompt_inputs_form()*.")
	st.write("As you interact with the chatbot, observe that the memory is updated with the latest k number of user input and output as seen from the code output.")
	st.markdown("**:blue[Code]**")
	st.code('''
if "memory" not in st.session_state:
	st.session_state.memory = ConversationBufferWindowMemory(k=5)

	#step 1 save the memory from your chatbot 
	#step 2 integrate the memory in the prompt_template (st.session_state.prompt_template) 
	memory_data = st.session_state.memory.load_memory_variables({})
	st.write(memory_data)
	st.session_state.prompt_template = f"""{input_prompt}\n\nBelow is the conversation history between the AI and Users so far\n\n{memory_data}"""
''')
	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
def ch12():
	#Prompt_template form from ex11
	prompt_template = PromptTemplate(
				input_variables=["occupation", "topic", "age"],
				template="""Imagine you are a {occupation} who is an expert on the  topic of {topic} , you are going to help , teach and provide information
						to the person who is {age} years old, if you do not not know the answer, you must tell the person , do not make any answer up"""
				)
	dict_inputs = prompt_inputs_form()
	if dict_inputs:
		input_prompt = prompt_template.format(occupation =dict_inputs["occupation"], topic=dict_inputs["topic"], age=dict_inputs["age"])
	else:
		input_prompt = "You are a helpful assistant. "

	st.write("input prompt: ", input_prompt)

	if "memory" not in st.session_state:
		st.session_state.memory = ConversationBufferWindowMemory(k=3)

	#step 1 save the memory from your chatbot 
	#step 2 integrate the memory in the prompt_template (st.session_state.prompt_template) show a hint
	memory_data = st.session_state.memory.load_memory_variables({})
	st.write("Memory Data: ", memory_data)
	st.session_state.prompt_template = f"""{input_prompt}\n\nBelow is the conversation history between the AI and Users so far\n\n{memory_data}
										"""

	st.write("New prompt template: ", st.session_state.prompt_template)
	#call the function in your base bot
	#Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	#Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			#set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				#streaming function
				for response in chat_completion_stream_prompt(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})
			st.session_state.memory.save_context({"input": prompt}, {"output": full_response})

	except Exception as e:
		st.error(e)
	pass
''')
		  
	st.markdown("**:red[Code Output]**")
	#actual code here
	ch12()

#exercise 13 - loading
def upload_file_streamlit():

	def get_file_extension(file_name):
		return os.path.splitext(file_name)[1]

	st.subheader("Upload your docs")

	# Streamlit file uploader to accept file input
	uploaded_file = st.file_uploader("Choose a file", type=['docx', 'txt', 'pdf'])

	if uploaded_file:

		# Reading file content
		file_content = uploaded_file.read()

		# Determine the suffix based on uploaded file's name
		file_suffix = get_file_extension(uploaded_file.name)

		# Saving the uploaded file temporarily to process it
		with tempfile.NamedTemporaryFile(delete=False, suffix=file_suffix) as temp_file:
			temp_file.write(file_content)
			temp_file.flush()  # Ensure the data is written to the file
			temp_file_path = temp_file.name
		return temp_file_path
	
#exercise 13 - split and chunk, embeddings and storing in vectorstores for reference
def vecstore_creator(query):
	if "vectorstore" not in st.session_state:
		st.session_state.vectorstore = False
	
	os.environ['OPENAI_API_KEY'] = st.secrets["openapi_key"]
	# Process the temporary file using UnstructuredFileLoader (or any other method you need)
	embeddings = OpenAIEmbeddings()
	db = lancedb.connect("/tmp/lancedb")
	table = db.create_table(
		"my_table",
		data=[
			{
				"vector": embeddings.embed_query("Hello World"),
				"text": "Hello World",
				"id": "1",
			}
		],
		mode="overwrite",
	)
	#st.write(temp_file_path)
	temp_file_path = upload_file_streamlit()
	if temp_file_path:
		loader = PyPDFLoader(temp_file_path )
		documents = loader.load_and_split()
		vectorestore = LanceDB.from_documents(documents, OpenAIEmbeddings(), connection=table)
		st.session_state.vectorstore = vectorestore
		if query:
			docs = vectorestore.similarity_search(query)
			st.write(docs[0].page_content)

def ex13_vectorstore_creator():
	query = st.text_input("Enter a query")
	vecstore_creator(query)

def class1_ex13():
	st.subheader("Exercise 13: Create a vector store")
	st.write("Now, we will create a vector store to store the user's document.")
	st.write("This process uses OpenAI to generate embeddings and LanceDB for storing these embeddings.")
	st.write("You will need to run the following commands in terminal to install new libaries:")
	st.code('''
pip install pypdf
pip install lancedb
''')

	st.markdown("**:blue[Code]**")
	st.code('''
#exercise 13 - loading
def upload_file_streamlit():

	def get_file_extension(file_name):
		return os.path.splitext(file_name)[1]

	st.subheader("Upload your docs")

	# Streamlit file uploader to accept file input
	uploaded_file = st.file_uploader("Choose a file", type=['docx', 'txt', 'pdf'])

	if uploaded_file:

		# Reading file content
		file_content = uploaded_file.read()

		# Determine the suffix based on uploaded file's name
		file_suffix = get_file_extension(uploaded_file.name)

		# Saving the uploaded file temporarily to process it
		with tempfile.NamedTemporaryFile(delete=False, suffix=file_suffix) as temp_file:
			temp_file.write(file_content)
			temp_file.flush()  # Ensure the data is written to the file
			temp_file_path = temp_file.name
		return temp_file_path
	
#exercise 13 - split and chunk, embeddings and storing in vectorstores for reference
def vecstore_creator(query):
	if "vectorstore" not in st.session_state:
		st.session_state.vectorstore = False
	
	os.environ['OPENAI_API_KEY'] = st.secrets["openapi_key"]
	# Process the temporary file using UnstructuredFileLoader (or any other method you need)
	embeddings = OpenAIEmbeddings()
	db = lancedb.connect("/tmp/lancedb")
	table = db.create_table(
		"my_table",
		data=[
			{
				"vector": embeddings.embed_query("Hello World"),
				"text": "Hello World",
				"id": "1",
			}
		],
		mode="overwrite",
	)
	#st.write(temp_file_path)
	temp_file_path = upload_file_streamlit()
	if temp_file_path:
		loader = PyPDFLoader(temp_file_path )
		documents = loader.load_and_split()
		vectorestore = LanceDB.from_documents(documents, OpenAIEmbeddings(), connection=table)
		st.session_state.vectorstore = vectorestore
		if query:
			docs = vectorestore.similarity_search(query)
			st.write(docs[0].page_content)

def ex13_vectorstore_creator():
	query = st.text_input("Enter a query")
	vecstore_creator(query)
''')
		  
	st.markdown("**:red[Code Output]**")
	ex13_vectorstore_creator()

def class1_ex14():
	st.subheader("Exercise 14: Semantic search")
	st.write("In this exercise. we will do a semantic search on the vector store in our chatbot.")
	st.write("At the same time, the chatbot is able to remember its conversation history to some extent.")
	st.write("This code integrates advanced features like semantic search and context-aware prompts to provide a more engaging and helpful conversational experience.")
	st.write("Copy and run the code below to see the chatbot in action.")

	st.markdown("**:blue[Code]**")
	st.code('''
#save the vectorstore in st.session_state
#add semantic search prompt into memory prompt
#integrate back into your chatbot
def ex14():

	vecstore_creator(False)
	
	if "memory" not in st.session_state:
		st.session_state.memory = ConversationBufferWindowMemory(k=5)

	#step 1 save the memory from your chatbot 
	#step 2 integrate the memory in the prompt_template (st.session_state.prompt_template) 
	memory_data = st.session_state.memory.load_memory_variables({})
	st.write("memory_data: ", memory_data)
	st.session_state.prompt_template = f"""You are a helpful assistant
										This is the last conversation history
										{memory_data}
										"""
	 #call the function in your base bot
	#Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	#Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			#query information
			if st.session_state.vectorstore:
				docs = st.session_state.vectorstore.similarity_search(prompt)
				docs = docs[0].page_content 
				#add your query prompt
				vs_prompt = f"""You should reference this search result to help your answer,
								{docs}
				if the search result does not anwer the query, please say you are unable to answer, do not make up an answer"""
			else:
				vs_prompt = ""
			#add query prompt to your memory prompt and send it to LLM
			st.session_state.prompt_template = st.session_state.prompt_template + vs_prompt
			#set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				#streaming function
				for response in chat_completion_stream_prompt(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})
			st.session_state.memory.save_context({"input": prompt}, {"output": full_response})

	except Exception as e:
		st.error(e)
''')

	st.markdown("**:red[Code Output]**")
	#save the vectorstore in st.session_state
	#add semantic search prompt into memory prompt
	#integrate back into your chatbot
	vecstore_creator(False)
	
	if "memory" not in st.session_state:
		st.session_state.memory = ConversationBufferWindowMemory(k=5)

	#step 1 save the memory from your chatbot 
	#step 2 integrate the memory in the prompt_template (st.session_state.prompt_template) 
	memory_data = st.session_state.memory.load_memory_variables({})
	st.write("memory_data: ", memory_data)
	st.session_state.prompt_template = f"""You are a helpful assistant
										This is the last conversation history
										{memory_data}
										"""
	 #call the function in your base bot
	#Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	#Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			#query information
			if st.session_state.vectorstore:
				docs = st.session_state.vectorstore.similarity_search(prompt)
				docs = docs[0].page_content 
				#add your query prompt
				vs_prompt = f"""You should reference this search result to help your answer,
								{docs}
				if the search result does not anwer the query, please say you are unable to answer, do not make up an answer"""
			else:
				vs_prompt = ""
			#add query prompt to your memory prompt and send it to LLM
			st.session_state.prompt_template = st.session_state.prompt_template + vs_prompt
			#set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				#streaming function
				for response in chat_completion_stream_prompt(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})
			st.session_state.memory.save_context({"input": prompt}, {"output": full_response})

	except Exception as e:
		st.error(e)

def class1_ex15():
	st.subheader("Exercise 15: Using a database")
	st.write("In this exercise, we will demonstrate how to create a database, as well as how to store and retrieve data from it.")
	st.write("There are three code sections in this exercise.")
	st.write("1. The following piece of code creates a local SQLite database and a specific table to store the conversation data.")

	st.markdown("**:blue[Code]**")
	st.code("""
def ex15():
	# Create or check for the 'database' directory in the current working directory
	cwd = os.getcwd()
	database_path = os.path.join(cwd, "database")

	if not os.path.exists(database_path):
		os.makedirs(database_path)

	# Set DB_NAME to be within the 'database' directory
	DB_NAME = os.path.join(database_path, "default_db")

	# Connect to the SQLite database
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	# Conversation data table
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS data_table (
			id INTEGER PRIMARY KEY,
			date TEXT NOT NULL UNIQUE,
			username TEXT NOT NULL,
			chatbot_ans TEXT NOT NULL,
			user_prompt TEXT NOT NULL,
			tokens TEXT
		)
	''')
	conn.commit()
	conn.close()
""")
	st.write("2. The following piece of code connects to a local SQLite database, fetches all records from a specific table, and displays them as a DataFrame.")
	st.write("This function is useful for viewing stored conversational data.")

	st.markdown("**:blue[Code]**")
	st.code("""
#implementing data collection and displaying 
def ex15_display():
#display data
	cwd = os.getcwd()
	database_path = os.path.join(cwd, "database")

	if not os.path.exists(database_path):
		os.makedirs(database_path)

	# Set DB_NAME to be within the 'database' directory
	DB_NAME = os.path.join(database_path, "default_db")
	# Connect to the specified database
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	# Fetch all data from data_table
	cursor.execute("SELECT * FROM data_table")
	rows = cursor.fetchall()
	column_names = [description[0] for description in cursor.description]
	df = pd.DataFrame(rows, columns=column_names)
	st.dataframe(df)
	conn.close()
""")
	st.write("3.. The following piece of code collects real time data from a chatbot and stores the data in a local database.")
	st.write("This function is useful for performing data analytics and user behaviour understanding.")

	st.markdown("**:blue[Code]**")
	st.code("""
def ex15_collect(username, chatbot, prompt):
#collect data from bot and store in sql database
	cwd = os.getcwd()
	database_path = os.path.join(cwd, "database")

	if not os.path.exists(database_path):
		os.makedirs(database_path)

	# Set DB_NAME to be within the 'database' directory
	DB_NAME = os.path.join(database_path, "default_db")
	conn = sqlite3.connect("database")
	cursor = conn.cursor()
	now = datetime.now() # Using ISO format for date
	tokens = len(chatbot)*1.3
	cursor.execute('''
		INSERT INTO data_table (date, username,chatbot_ans, user_prompt, tokens)
		VALUES (?, ?, ?, ?, ?, ?)
	''', (now, username, chatbot, prompt, tokens))
	conn.commit()
	conn.close()
""")
	#st.markdown("**:red[Code Output]**")
	# Actual code here

#collecting data using sql server
def ex15():
	# Create or check for the 'database' directory in the current working directory
	cwd = os.getcwd()
	database_path = os.path.join(cwd, "database")

	if not os.path.exists(database_path):
		os.makedirs(database_path)

	# Set DB_NAME to be within the 'database' directory
	DB_NAME = os.path.join(database_path, "default_db")

	# Connect to the SQLite database
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	# Conversation data table
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS data_table (
			id INTEGER PRIMARY KEY,
			date TEXT NOT NULL UNIQUE,
			username TEXT NOT NULL,
			chatbot_ans TEXT NOT NULL,
			user_prompt TEXT NOT NULL,
			tokens TEXT
		)
	''')
	conn.commit()
	conn.close()

#implementing data collection and displaying 
def ex15_display():
#display data
	cwd = os.getcwd()
	database_path = os.path.join(cwd, "database")

	if not os.path.exists(database_path):
		os.makedirs(database_path)

	# Set DB_NAME to be within the 'database' directory
	DB_NAME = os.path.join(database_path, "default_db")
	# Connect to the specified database
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	# Fetch all data from data_table
	cursor.execute("SELECT * FROM data_table")
	rows = cursor.fetchall()
	column_names = [description[0] for description in cursor.description]
	df = pd.DataFrame(rows, columns=column_names)
	st.dataframe(df)
	conn.close()

def ex15_collect(username, chatbot, prompt):
#collect data from bot and store in sql database
	cwd = os.getcwd()
	database_path = os.path.join(cwd, "database")

	if not os.path.exists(database_path):
		os.makedirs(database_path)

	# Set DB_NAME to be within the 'database' directory
	DB_NAME = os.path.join(database_path, "default_db")
	conn = sqlite3.connect("database")
	cursor = conn.cursor()
	now = datetime.now() # Using ISO format for date
	tokens = len(chatbot)*1.3
	cursor.execute('''
		INSERT INTO data_table (date, username,chatbot_ans, user_prompt, tokens)
		VALUES (?, ?, ?, ?, ?, ?)
	''', (now, username, chatbot, prompt, tokens))
	conn.commit()
	conn.close()

def class1_ch15():
	st.subheader("Challenge 15: Using a database")
	st.write("For this challenge, we will incorporate using a database from our previous exercise.")
	st.write("Copy the code from ***ex14()*** and use the ***ex15_display()*** function before the user interaction to view the the conversation data in a local database.")
	st.write("Call ***ex15() first to create the local database and table.")
	st.write("Use the ***ex15_collect()*** function to collect and store data in the local database after each user conversation interaction.")

	st.markdown("**:blue[Code]**")
	with st.expander("Reveal Code"):
		st.code('''
def ch15_chatbot():
	vecstore_creator(False)
	ex15_display()
	if "memory" not in st.session_state:
		st.session_state.memory = ConversationBufferWindowMemory(k=5)

	#step 1 save the memory from your chatbot 
	#step 2 integrate the memory in the prompt_template (st.session_state.prompt_template) 
	memory_data = st.session_state.memory.load_memory_variables({})
	st.write("memory data: ", memory_data)
	st.session_state.prompt_template = f"""You are a helpful assistant
										This is the last conversation history
										{memory_data}
										"""
	 #call the function in your base bot
	#Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	#Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			#query information
			if st.session_state.vectorstore:
				docs = st.session_state.vectorstore.similarity_search(prompt)
				docs = docs[0].page_content
				#add your query prompt
				vs_prompt = f"""You should reference this search result to help your answer,
								{docs}
								if the search result does not anwer the query, please say you are unable to answer, do not make up an answer"""
			else:
				vs_prompt = ""
			#add query prompt to your memory prompt and send it to LLM
			st.session_state.prompt_template = st.session_state.prompt_template + vs_prompt
			#set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				#streaming function
				for response in chat_completion_stream_prompt(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})
			st.session_state.memory.save_context({"input": prompt}, {"output": full_response})
			#collect data
			ex15_collect("username", full_response, prompt)

	except Exception as e:
		st.error(e)
''')
		  
	st.markdown("**:red[Code Output]**")
	# Actual code here
	vecstore_creator(False)
	ex15()
	ex15_display()
	if "memory" not in st.session_state:
		st.session_state.memory = ConversationBufferWindowMemory(k=5)

	#step 1 save the memory from your chatbot 
	#step 2 integrate the memory in the prompt_template (st.session_state.prompt_template) 
	memory_data = st.session_state.memory.load_memory_variables({})
	st.write("memory data: ", memory_data)
	st.session_state.prompt_template = f"""You are a helpful assistant
										This is the last conversation history
										{memory_data}
										"""
	 #call the function in your base bot
	#Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	#Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		#
		if prompt := st.chat_input("What is up?"):
			#query information
			if st.session_state.vectorstore:
				docs = st.session_state.vectorstore.similarity_search(prompt)
				docs = docs[0].page_content
				#add your query prompt
				vs_prompt = f"""You should reference this search result to help your answer,
								{docs}
								if the search result does not anwer the query, please say you are unable to answer, do not make up an answer"""
			else:
				vs_prompt = ""
			#add query prompt to your memory prompt and send it to LLM
			st.session_state.prompt_template = st.session_state.prompt_template + vs_prompt
			#set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				#streaming function
				for response in chat_completion_stream_prompt(prompt):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})
			st.session_state.memory.save_context({"input": prompt}, {"output": full_response})
			#collect data
			ex15_collect("username", full_response, prompt)

	except Exception as e:
		st.error(e)

def class1_ex16():
	st.subheader("Exercise 16: Smart agent")
	st.write("In this exercise, we will configure a chatbot with an internet search tool that shows all intermediate steps and tool logs.")
	st.write("This overcomes the limitation of the training data that is only up to a certain point in time, by being able to access the current internet to search for answers.")

	st.markdown("**:blue[Code]**")
	st.code('''
#smart agents accessing the internet for free
#https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/search_and_chat.py
def ex16():
	st.title("🦜 LangChain: Chat with search")

	openai_api_key = st.secrets["openapi_key"]

	msgs = StreamlitChatMessageHistory()
	memory = ConversationBufferMemory(
		chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
	)
	if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
		msgs.clear()
		msgs.add_ai_message("How can I help you?")
		st.session_state.steps = {}

	avatars = {"human": "user", "ai": "assistant"}
	for idx, msg in enumerate(msgs.messages):
		with st.chat_message(avatars[msg.type]):
			# Render intermediate steps if any were saved
			for step in st.session_state.steps.get(str(idx), []):
				if step[0].tool == "_Exception":
					continue
				with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
					st.write(step[0].log)
					st.write(step[1])
			st.write(msg.content)

	if prompt := st.chat_input(placeholder="Enter a query on the Internet"):
		st.chat_message("user").write(prompt)

		llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
		tools = [DuckDuckGoSearchRun(name="Search")]
		chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)
		executor = AgentExecutor.from_agent_and_tools(
			agent=chat_agent,
			tools=tools,
			memory=memory,
			return_intermediate_steps=True,
			handle_parsing_errors=True,
		)
		with st.chat_message("assistant"):
			st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
			response = executor(prompt, callbacks=[st_cb])
			st.write(response["output"])
			st.session_state.steps[str(len(msgs.messages) - 1)] = response["intermediate_steps"]
''')

	st.markdown("**:red[Code Output]**")
	# Actual code here
	ex16()

#smart agents accessing the internet for free
#https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/search_and_chat.py
def ex16():
	st.title("🦜 LangChain: Chat with search")

	openai_api_key = st.secrets["openapi_key"]

	msgs = StreamlitChatMessageHistory()
	memory = ConversationBufferMemory(
		chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
	)
	if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
		msgs.clear()
		msgs.add_ai_message("How can I help you?")
		st.session_state.steps = {}

	avatars = {"human": "user", "ai": "assistant"}
	for idx, msg in enumerate(msgs.messages):
		with st.chat_message(avatars[msg.type]):
			# Render intermediate steps if any were saved
			for step in st.session_state.steps.get(str(idx), []):
				if step[0].tool == "_Exception":
					continue
				with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
					st.write(step[0].log)
					st.write(step[1])
			st.write(msg.content)

	if prompt := st.chat_input(placeholder="Enter a query on the Internet"):
		st.chat_message("user").write(prompt)

		llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
		tools = [DuckDuckGoSearchRun(name="Search")]
		chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)
		executor = AgentExecutor.from_agent_and_tools(
			agent=chat_agent,
			tools=tools,
			memory=memory,
			return_intermediate_steps=True,
			handle_parsing_errors=True,
		)
		with st.chat_message("assistant"):
			st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
			response = executor(prompt, callbacks=[st_cb])
			st.write(response["output"])
			st.session_state.steps[str(len(msgs.messages) - 1)] = response["intermediate_steps"]

#agents ,vectorstores, wiki 
#https://python.langchain.com/docs/modules/agents/how_to/custom_agent_with_tool_retrieval
#note tool
@tool("Document search")
def document_search(query: str) ->str:
	"Use this function first to search for documents pertaining to the query before going into the internet"
	docs = st.session_state.vectorstore.similarity_search(query)
	docs = docs[0].page_content
	json_string = json.dumps(docs, ensure_ascii=False, indent=4)
	return json_string

def ex17():
	vecstore_creator(False)
	#st.session_state.vectorstore

	st.title("🦜 LangChain: Chat with search")

	openai_api_key = st.secrets["openapi_key"]

	msgs = StreamlitChatMessageHistory()
	memory = ConversationBufferMemory(
		chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
	)
	if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
		msgs.clear()
		msgs.add_ai_message("How can I help you?")
		st.session_state.steps = {}

	avatars = {"human": "user", "ai": "assistant"}
	for idx, msg in enumerate(msgs.messages):
		with st.chat_message(avatars[msg.type]):
			# Render intermediate steps if any were saved
			for step in st.session_state.steps.get(str(idx), []):
				if step[0].tool == "_Exception":
					continue
				with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
					st.write(step[0].log)
					st.write(step[1])
			st.write(msg.content)

	if prompt := st.chat_input(placeholder="Enter a query on the Internet"):
		st.chat_message("user").write(prompt)

		llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
		tools = [DuckDuckGoSearchRun(name="Internet Search"), document_search]
		chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)
		executor = AgentExecutor.from_agent_and_tools(
			agent=chat_agent,
			tools=tools,
			memory=memory,
			return_intermediate_steps=True,
			handle_parsing_errors=True,
		)
		with st.chat_message("assistant"):
			st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
			response = executor(prompt, callbacks=[st_cb])
			st.write(response["output"])
			st.session_state.steps[str(len(msgs.messages) - 1)] = response["intermediate_steps"]

def class1_ex17():
	st.subheader("Exercise 17: Smart agent with vector store")
	st.write("In this exercise, we will combine the vector store with the smart agent.")
	st.write("This allows the chatbot to search for answers from the vector store and the internet.")
	st.write("The @tool(\"Document search\") function is an enhancement to the chatbot. It allows for an initial internal document search based on the user query before resorting to external internet searches. ")
	st.write("Copy and run the code below to see the chatbot in action.")

	st.markdown("**:blue[Code]**")
	st.code('''
#agents ,vectorstores, wiki 
#https://python.langchain.com/docs/modules/agents/how_to/custom_agent_with_tool_retrieval
#note tool
@tool("Document search")
def document_search(query: str) ->str:
	"Use this function first to search for documents pertaining to the query before going into the internet"
	docs = st.session_state.vectorstore.similarity_search(query)
	docs = docs[0].page_content
	json_string = json.dumps(docs, ensure_ascii=False, indent=4)
	return json_string

def ex17():
	vecstore_creator(False)
	#st.session_state.vectorstore

	st.title("🦜 LangChain: Chat with search")

	openai_api_key = st.secrets["openapi_key"]

	msgs = StreamlitChatMessageHistory()
	memory = ConversationBufferMemory(
		chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
	)
	if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
		msgs.clear()
		msgs.add_ai_message("How can I help you?")
		st.session_state.steps = {}

	avatars = {"human": "user", "ai": "assistant"}
	for idx, msg in enumerate(msgs.messages):
		with st.chat_message(avatars[msg.type]):
			# Render intermediate steps if any were saved
			for step in st.session_state.steps.get(str(idx), []):
				if step[0].tool == "_Exception":
					continue
				with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
					st.write(step[0].log)
					st.write(step[1])
			st.write(msg.content)

	if prompt := st.chat_input(placeholder="Enter a query on the Internet"):
		st.chat_message("user").write(prompt)

		llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
		tools = [DuckDuckGoSearchRun(name="Internet Search"), document_search]
		chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)
		executor = AgentExecutor.from_agent_and_tools(
			agent=chat_agent,
			tools=tools,
			memory=memory,
			return_intermediate_steps=True,
			handle_parsing_errors=True,
		)
		with st.chat_message("assistant"):
			st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
			response = executor(prompt, callbacks=[st_cb])
			st.write(response["output"])
			st.session_state.steps[str(len(msgs.messages) - 1)] = response["intermediate_steps"]
''')
		  
	st.markdown("**:red[Code Output]**")
	# Actual code here
	ex17()

#Pandai - A smart agent that can do visual analytics
def ex18():
	st.title("pandas-ai streamlit interface")

	# Upload CSV file using st.file_uploader
	uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
	if "openai_key" not in st.session_state:
		st.session_state.openai_key = st.secrets["openapi_key"]
		st.session_state.prompt_history = []
		st.session_state.df = None
	
	if st.session_state.df is None:
		# If a file is uploaded, read it with pandas and display the DataFrame
		if uploaded_file is not None:
			try:
				df = pd.read_csv(uploaded_file)
				st.session_state.df = df
			except Exception as e:
				st.write("There was an error processing the CSV file.")
				st.write(e)

	# Check if df is a DataFrame instance
	if  st.session_state.df is None:
		st.session_state.df = pd.DataFrame({
			"country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
			"gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
			"happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
		})
	
	with st.form("Question"):
		question = st.text_input("Question", value="", type="default")
		submitted = st.form_submit_button("Submit")
		if submitted:
			with st.spinner():
				llm = OpenAI(api_token=st.session_state.openai_key)
				df = SmartDataframe(st.session_state.df, config={"llm": llm})
				response = df.chat(question)  # Using 'chat' method based on your context.
			
				# After generating the chart (if applicable), display it:
				chart_path = os.path.join("exports/charts", "temp_chart.png")
				if os.path.exists(chart_path):
					plt.savefig(chart_path)
					st.image(chart_path, caption="Generated Chart", use_column_width=True)
				
				# Display the textual response (if any):
				if response:
					st.write(response)
				
				# Append the question to the history:
				st.session_state.prompt_history.append(question)

	if st.session_state.df is not None:
		st.subheader("Current dataframe:")
		st.write(st.session_state.df)

	st.subheader("Prompt history:")
	st.write(st.session_state.prompt_history)

	if st.button("Clear"):
		st.session_state.prompt_history = []
		st.session_state.df = None

def class1_ex18():
	st.subheader("Exercise 18: Data Analytics")
	st.write("In this exercise, we will use the Pandas AI library to perform data analytics.")
	st.write("The Pandas AI library is a smart agent that can perform data analytics on a dataframe.")
	st.write("Copy and run the code below to see the chatbot in action.")

	st.markdown("**:blue[Code]**")
	st.code('''
#Pandai - A smart agent that can do visual analytics
def ex18():
	st.title("pandas-ai streamlit interface")

	# Upload CSV file using st.file_uploader
	uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
	if "openai_key" not in st.session_state:
		st.session_state.openai_key = st.secrets["openapi_key"]
		st.session_state.prompt_history = []
		st.session_state.df = None
	
	if st.session_state.df is None:
		# If a file is uploaded, read it with pandas and display the DataFrame
		if uploaded_file is not None:
			try:
				df = pd.read_csv(uploaded_file)
				st.session_state.df = df
			except Exception as e:
				st.write("There was an error processing the CSV file.")
				st.write(e)

	# Check if df is a DataFrame instance
	if  st.session_state.df is None:
		st.session_state.df = pd.DataFrame({
			"country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
			"gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
			"happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
		})
	
	with st.form("Question"):
		question = st.text_input("Question", value="", type="default")
		submitted = st.form_submit_button("Submit")
		if submitted:
			with st.spinner():
				llm = OpenAI(api_token=st.session_state.openai_key)
				df = SmartDataframe(st.session_state.df, config={"llm": llm})
				response = df.chat(question)  # Using 'chat' method based on your context.
			
				# After generating the chart (if applicable), display it:
				chart_path = os.path.join("exports/charts", "temp_chart.png")
				if os.path.exists(chart_path):
					plt.savefig(chart_path)
					st.image(chart_path, caption="Generated Chart", use_column_width=True)
				
				# Display the textual response (if any):
				if response:
					st.write(response)
				
				# Append the question to the history:
				st.session_state.prompt_history.append(question)

	if st.session_state.df is not None:
		st.subheader("Current dataframe:")
		st.write(st.session_state.df)

	st.subheader("Prompt history:")
	st.write(st.session_state.prompt_history)

	if st.button("Clear"):
		st.session_state.prompt_history = []
		st.session_state.df = None
''')
	  
	st.markdown("**:red[Code Output]**")
	ex18()