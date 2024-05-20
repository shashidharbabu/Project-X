import streamlit as st
import os
import google.generativeai as genai
from process import Generator  # Assuming process.py holds Generator class

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 0.9,
    "top_k": 1,
    "top_p": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
chat = model.start_chat(history=[])  # Start a new chat session

st.set_page_config(page_title="Ella")

st.header("Talk to Ella")
st.subheader("Your supportive mental health companion")

#setting chat history state if not already present
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

#input and submit
user_input = st.text_input("What's on your mind today?", key="input")
submit_button = st.button("Talk to Ella")



#response generation 
if submit_button and user_input:
    st.write("Generating response...")
    def gemini_process(user_input):
        generation_config = {
            
            "temperature": 0.9,
            "top_k": 1,
            "top_p": 1,
            "max_output_tokens":2048
            
        }
        
        #conversations: gemini-pro || images : gemini-pro-vision
        
        model = genai.GenerativeModel("gemini-pro", generation_config = generation_config)
        prompt = f"""You are Ella, an empathetic mental health assistant who's primary qualities are kindness, 
                    empathy, active listening and asking follow up questions about the question or topic. Now respond 
                    to the following sentence: {user_input}"""
                    
        response = model.generate_content(prompt)

        # response = model.generate_content(["Create a study schedule for the whole day."])

        print(response.text)
        
        return response.text

    st.write("********")
    # task = st.write(gemini_process(user_input))
    # if task is not None:
    response = gemini_process(user_input)
    st.session_state['chat_history'].append(("You", user_input))
    st.subheader("Ella:")
    # for chunk in response:
    print("#####" + response + "THIS IS CHUNK!!!!!!!!!!!!!")
    st.write(response)
    st.write("********")

    st.session_state['chat_history'].append(("Ella", response))

            
    # else:
    #     st.error("Error scheduling response generation")  # Handle potential errors

            
    
st.subheader("The Chat History is")
st.subheader("Chat History:")


for role, text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")