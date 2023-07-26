import streamlit as st
from streamlit_antd_components import menu, MenuItem, divider
from authenticate import class0_login, class1_login
from class1_exercise import (
				class1_prep, 
				class1_hw1, 
				class1_ex1, 
				class1_ch1, 
				class1_ex2, 
				class1_ch2, 
				class1_ex3, 
				class1_ch3,
				class1_ex4, 
				class1_ch4, 
				class1_ex5, 
				class1_ch6, 
				class1_ex6, 
				class1_ex7, 
				class1_ex8, 
				class1_ch8, 
				class1_ex9,  
				class1_ex10, 
				class1_ch10,
				)

class0 = "Python Basics"
class1 = "Build Chatbot"
prep = "Setup"
hw1 = 'Hello World App'
ex1 = "Exercise 1"
ch1 = "Challenge 1"
ex2 = "Exercise 2"
ch2 = "Challenge 2"
ex3 = "Exercise 3"
ch3 = "Challenge 3"
ex4 = "Exercise 4"
ch4 = "Challenge 4"
ex5 = "Exercise 5"
ch6 = "Challenge 6"
ex6 = "Exercise 6"
ex7 = "Exercise 7"
ex8 = "Exercise 8"
ch8 = "Challenge 8"
ex9 = "Exercise 9"
ex10 = "Exercise 10"
ch10 = "Challenge 10"

st.set_page_config(layout="wide")

def main():
	st.title("ITD Sharing Workshops 2023")
	
	if 'login_key' not in st.session_state:
		st.session_state.login_key = False
	
	cls = class1

	# if 'option_key' not in st.session_state:
	# 	st.session_state.option_key = ""
	# st.session_state.option_key
	if cls == class0 and st.session_state.login_key == False:
		placeholder1 = st.empty()
		with placeholder1:
			divider(label='Class login', icon='door-open', align='left')
			col1, col2 = st.columns([2,4])
			with col1:
				lg = class0_login()
				if lg == True:
					st.session_state.login_key = True
					placeholder1.empty()
				

	elif cls == class1 and st.session_state.login_key == False:
		placeholder1 = st.empty()
		with placeholder1:
			divider(label='Class login', icon='door-open', align='left')
			col1, col2 = st.columns([2,4])
			with col1:
				lg = class1_login()
				if lg == True:
					st.session_state.login_key = True
					placeholder1.empty()
	
	with st.sidebar: #options for sidebar
		if st.session_state.login_key == True:
			option = menu([MenuItem(prep, icon='journal-code'),
					MenuItem(hw1, icon='journal-code'),
		      		MenuItem('Part 1', icon='journal-code', children=[
					MenuItem(ex1, icon='journal-code'),
					MenuItem(ex2, icon='journal-code'),
					MenuItem(ex3, icon='journal-code'),
					MenuItem(ex4, icon='journal-code'),
					MenuItem(ch1, icon='journal-code'),
					MenuItem(ch2, icon='journal-code'),
					MenuItem(ch3, icon='journal-code'),
					MenuItem(ch4, icon='journal-code'),
    			]),
					
		      		MenuItem('Part 2', icon='journal-code', children=[
					MenuItem(ex5, icon='journal-code'),
					MenuItem(ex6, icon='journal-code'),
					MenuItem(ch6, icon='journal-code'),
    			]),
		      		MenuItem('Part 3', icon='journal-code', children=[
					MenuItem(ex7, icon='journal-code'),
					MenuItem(ex8, icon='journal-code'),
					MenuItem(ch8, icon='journal-code'),
					MenuItem(ex9, icon='journal-code'),
    			]),
		      		MenuItem('Part 4', icon='journal-code', children=[
					MenuItem(ex10, icon='journal-code'),
					MenuItem(ch10, icon='journal-code'),
    			], dashed=True),
					
				MenuItem(type='divider'),
				MenuItem('Logout', icon='box-arrow-right'),],open_all=True)
			if option == 'Logout':
				for key in st.session_state.keys():
					del st.session_state[key]
				st.experimental_rerun()
			pass
		else:#not login yet
			cls = menu([MenuItem(class1, icon='laptop')])
			pass
	
	if cls == class1 and st.session_state.login_key == True:
		divider(label='Workshop 1 - Building a Chatbot using LLM API', icon='journal-code', align='left')
		if option == prep:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_prep()

		elif option == hw1:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_hw1()
	
		elif option == ex1:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex1()

		elif option == ch1:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ch1()

		elif option == ex2:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex2()

		elif option == ch2:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ch2()
		
		elif option == ex3:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex3()

		elif option == ch3:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ch3()
		elif option == ex4:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex4()

		elif option == ch4:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ch4()
		elif option == ex5:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex5()

		elif option == ch6:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ch6()

		elif option == ex6:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex6()

		elif option == ex7:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex7()

		elif option == ex8:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex8()

		elif option == ch8:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ch8()
		
		elif option == ex9:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex9()

		elif option == ex10:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ex10()

		elif option == ch10:
			placeholder2 = st.empty()
			with placeholder2.container():
				class1_ch10()
		

if __name__ == "__main__":
	main()