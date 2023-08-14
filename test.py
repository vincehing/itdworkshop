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