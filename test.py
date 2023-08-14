def ch10():
	#Challenge 10: Make the bot speak like someone you know
	st.title("ChatGPT-like clone with Prompt Engineering")

	openai.api_key = st.secrets["openapi_key"]

	prompt_template = st.chat_input("Enter a prompt to make your bot speak like someone you know!")

	if "openai_model" not in st.session_state:
		st.session_state["openai_model"] = "gpt-3.5-turbo"

	if "msg_bot" not in st.session_state:
		st.session_state.msg_bot = []

	if prompt_template := st.text_input("Enter a prompt to make your bot speak like someone you know!"):
		st.session_state.msg_bot.append({"role": "user", "content": prompt_template})
		with st.chat_message("user"):
			st.markdown(prompt_template)

		with st.chat_message("assistant"):
			full_response = "Nice! Now, let's test out your prompt template. Enter a prompt below to see how your bot responds."
			st.markdown(full_response)
		st.session_state.msg_bot.append({"role": "assistant", "content": full_response})

		try:

			if prompt := st.text_input("What is up?"):
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
				prompt = ""
				st.session_state.msg_bot.append({"role": "assistant", "content": full_response})

		except Exception as e:
			st.error(e)