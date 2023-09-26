import streamlit as st
from streamlit_antd_components import menu, MenuItem, divider
from authenticate import class0_login, class1_login
from class1_exercise import (
				class1_prep, 
				objectives,
				workshop_outline,
				team_introduction,
				workshop_rules,
				resources,
				vscode_ui,
				command_palette_indent,
				part1_intro1,
				class1_hw1, 
				class1_ex1, 
				class1_ch1, 
				class1_ex2, 
				class1_ch2, 
				class1_ex3, 
				class1_ex4a, 
				class1_ex4b, 
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
				class1_ex11, 
				class1_ch11,
				class1_ex12,
				class1_ch12,
				class1_ex13,
				class1_ex14,
				class1_ex15,
				class1_ch15,
				class1_ex16,
				class1_ex17,
				class1_ex18,
				final_product
				)

class0 = "Python Basics"
class1 = "Build Chatbot"
prep = "Setup"
hw1 = "Hello World App"
obj = "Objectives"
outline = "Workshop Outline"
intro = "Hello Team"
rules = "Workshop Rules"
res = "Useful resources"
ui = "Navigating VS Code"
indent = "Indenting Code"
part1_1 = "What is Streamlit"
ex1 = "Exercise 1"
ch1 = "Challenge 1"
ex2 = "Exercise 2"
ch2 = "Challenge 2"
ex3 = "Exercise 3"
ch3 = "Challenge 3"
ex4a = "Exercise 4a"
ex4b = "Exercise 4b"
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
ex11 = "Exercise 11"
ch11 = "Challenge 11"
ex12 = "Exercise 12"
ch12 = "Challenge 12"
ex13 = "Exercise 13"
ex14 = "Exercise 14"
ex15 = "Exercise 15"
ch15 = "Challenge 15"
ex16 = "Exercise 16"
ex17 = "Exercise 17"
ex18 = "Exercise 18"
final = "Yoda Chatbot"

st.set_page_config(layout="wide")
st.session_state.login_key = True

def main():
	st.title("ITD Sharing Workshops 2023") 
	divider(label='One Day Workshop - Exploring Generative AI and LLMs', icon='journal-code', align='left')

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
			option = menu([
					MenuItem('Part 1', icon='file-slides', href='https://docs.google.com/presentation/d/169KpD9qmabZ00mdAQEawhpPqv1MLMijW6jiPV_nKbLk/edit?usp=sharing'),
					MenuItem('Pre-workshop prep', icon='', children=[
					MenuItem(prep, icon='journal-code'),
					MenuItem(hw1, icon='journal-code'),
				]),
					MenuItem('Introduction', icon='', children=[
					# 	MenuItem(obj, icon='journal-code'),
					#	MenuItem(outline, icon='journal-code'),
					MenuItem(final, icon='journal-code'),
					# 	MenuItem(rules, icon='journal-code'),
					# 	MenuItem(intro, icon='journal-code'),
					MenuItem(res, icon='journal-code'),
				]),
		      		MenuItem('Intro to Streamlit', icon='', children=[
					# MenuItem(ui, icon='journal-code'),
					# MenuItem(indent, icon='journal-code'),
					# MenuItem(part1_1, icon='journal-code'),
					MenuItem(ex1, icon='journal-code'),
					# MenuItem(ch1, icon='journal-code'),
					MenuItem(ex2, icon='journal-code'),
					MenuItem(ch2, icon='journal-code'),
					MenuItem(ex3, icon='journal-code'),
					# MecnuItem(ch3, icon='journal-code'),
					MenuItem(ex4a, icon='journal-code'),
					MenuItem(ex4b, icon='journal-code'),
					MenuItem(ch4, icon='journal-code'),
    			]),
					
		      		MenuItem('Rule-based chatbot', icon='', children=[
					MenuItem(ex5, icon='journal-code'),
					MenuItem(ex6, icon='journal-code'),
					MenuItem(ch6, icon='journal-code'),
    			]),
		      		MenuItem('Integrate OpenAI API', icon='', children=[
					MenuItem(ex7, icon='journal-code'),
					MenuItem(ex8, icon='journal-code'),
					MenuItem(ch8, icon='journal-code'),
					MenuItem(ex9, icon='journal-code'),
    			]),
		      		MenuItem('Prompt Engineering', icon='', children=[
					MenuItem(ex10, icon='journal-code'),
					MenuItem(ch10, icon='journal-code'),
    			]), 
					MenuItem('Part 2', icon='file-slides', href='https://docs.google.com/presentation/d/1yNb4WmWDvQfdu05_5M8aEl5g-2evSK_fCdybJGupdKA/edit?usp=drive_link'),
					MenuItem('Prompt Template', icon='', children=[
					MenuItem(ex11, icon='journal-code'),
					MenuItem(ch11, icon='journal-code'),
    			]), 
				MenuItem('Memory', icon='', children=[
					MenuItem(ex12, icon='journal-code'),
					MenuItem(ch12, icon='journal-code'),
    			]), 
				MenuItem('Vector Store', icon='', children=[
					MenuItem(ex13, icon='journal-code'),
					MenuItem(ex14, icon='journal-code'),
    			]), 
				MenuItem('Database', icon='', children=[
					MenuItem(ex15, icon='journal-code'),
					MenuItem(ch15, icon='journal-code'),
    			]), 
				MenuItem('Part 3', icon='file-slides', href='https://docs.google.com/presentation/d/1fvMGaUC-K49ws1NaCdENB3CC4L7WZr337yTcsLqak1k/edit?usp=sharing'),
				MenuItem('Smart Agent', icon='', children=[
					MenuItem(ex16, icon='journal-code'),
    			]), 
				MenuItem('Smart Agent&Vector store', icon='', children=[
					MenuItem(ex17, icon='journal-code'),
    			]), 
				MenuItem('Part 4', icon='file-slides', href='https://docs.google.com/presentation/d/16j8UJOVTj06oU93CCZjioE7zlipZs36GbTgEMaECVuE/edit?usp=sharing'),
				MenuItem('Data Analytics', icon='', children=[
					MenuItem(ex18, icon='journal-code'),
    			]), 
				MenuItem(type='divider',dashed=True),
				MenuItem('Logout', icon='box-arrow-right'),],open_all=False)
			if option == 'Logout':
				for key in st.session_state.keys():
					del st.session_state[key]
				st.experimental_rerun()
			pass
		else:#not login yet
			cls = menu([MenuItem(class1, icon='laptop')])
	
	if cls == class1 and st.session_state.login_key == True:

		# initialize session state, from ch4
		if "name" not in st.session_state:
			st.session_state.name = "Yoda"

		if "age" not in st.session_state:
			st.session_state.age = 999

		if "gender" not in st.session_state:
			st.session_state.gender = "male"

		if "prompt_template" not in st.session_state:
			st.session_state.prompt_template = "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"

		if option == "Part 1":
			st.write("Welcome to the workshop! Link to slide decks and code exercises are on the left.")

		placeholder2 = st.empty()

		if option == prep:
			with placeholder2.container():
				class1_prep()

		elif option == obj:
			with placeholder2.container():
				objectives()

		elif option == outline:
			with placeholder2.container():
				workshop_outline()
		
		elif option == intro:
			with placeholder2.container():
				team_introduction()
		
		elif option == hw1:
			with placeholder2.container():
				class1_hw1()

		elif option == rules:
			with placeholder2.container():
				workshop_rules()

		elif option == res:
			with placeholder2.container():
				resources()

		elif option == ui:
			with placeholder2.container():
				vscode_ui()

		elif option == indent:
			with placeholder2.container():
				command_palette_indent()

		elif option == final:
			with placeholder2.container():
				final_product()

		elif option == part1_1:
			with placeholder2.container():
				part1_intro1()
	
		elif option == ex1:
			with placeholder2.container():
				class1_ex1()

		elif option == ch1:
			with placeholder2.container():
				class1_ch1()

		elif option == ex2:
			with placeholder2.container():
				class1_ex2()

		elif option == ch2:
			with placeholder2.container():
				class1_ch2()
		
		elif option == ex3:
			with placeholder2.container():
				class1_ex3()

		elif option == ex4a:
			with placeholder2.container():
				class1_ex4a()

		elif option == ex4b:
			with placeholder2.container():
				class1_ex4b()

		elif option == ch4:
			with placeholder2.container():
				class1_ch4()
		elif option == ex5:
			with placeholder2.container():
				class1_ex5()

		elif option == ch6:
			with placeholder2.container():
				class1_ch6()

		elif option == ex6:
			with placeholder2.container():
				class1_ex6()

		elif option == ex7:
			with placeholder2.container():
				class1_ex7()

		elif option == ex8:
			with placeholder2.container():
				class1_ex8()

		elif option == ch8:
			with placeholder2.container():
				class1_ch8()
		
		elif option == ex9:
			with placeholder2.container():
				class1_ex9()

		elif option == ex10:
			with placeholder2.container():
				class1_ex10()

		elif option == ch10:
			with placeholder2.container():
				class1_ch10()

		elif option == ex11:
			with placeholder2.container():
				class1_ex11()

		elif option == ch11:
			with placeholder2.container():
				class1_ch11()

		elif option == ex12:
			with placeholder2.container():
				class1_ex12()

		elif option == ch12:
			with placeholder2.container():
				class1_ch12()
		
		elif option == ex13:
			with placeholder2.container():
				class1_ex13()

		elif option == ex14:
			with placeholder2.container():
				class1_ex14()
		
		elif option == ex15:
			with placeholder2.container():
				class1_ex15()
	
		elif option == ch15:
			with placeholder2.container():
				class1_ch15()

		elif option == ex16:
			with placeholder2.container():
				class1_ex16()
		
		elif option == ex17:
			with placeholder2.container():
				class1_ex17()

		elif option == ex18:
			with placeholder2.container():
				class1_ex18()
		
if __name__ == "__main__":
	main()
