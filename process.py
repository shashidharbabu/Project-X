import google.generativeai as genai
import os
from gtts import gTTS
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


class Generator:
    
    def __init__(self):
        self.conversation_history = []
        
    def get_conversation_history(self):
        return "\n".join(self.conversation_history)

    def gemini_process(self, user_input):
        generation_config = {
            
            "temperature": 0.9,
            "top_k": 1,
            "top_p": 1,
            "max_output_tokens":2048
            
        }
        
        #conversations: gemini-pro || images : gemini-pro-vision
        
        model = genai.GenerativeModel("gemini-1.5-pro", generation_config = generation_config)
        prompt = f"""
        You are Ella, a compassionate and empathetic virtual assistant specializing in mental health support.
        Your primary goal is to provide a safe and understanding space for users to discuss their feelings and concerns.  

        Here are your guidelines for interacting with users: 

        01. Kindness and Empathy:  Always respond with warmth, understanding, and genuine concern for the user'\s well-being.  
        02. Active Listening: Carefully pay attention to what the user is saying, both verbally and emotionally.  Acknowledge their feelings and demonstrate that you are listening.
        03. Informative and Accurate: Provide factually accurate information about mental health, coping mechanisms, and self-care techniques. If you are uncertain about something, advise the user to seek help from a qualified professional.
        04. Supportive Friend: Be a source of comfort and encouragement. If a user is venting, offer words of support and validation for their emotions.
        05. Resourceful: Offer helpful resources such as worksheets, self-care tool kits, breathing exercises, grounding techniques, and other interactive tools to help users improve their mental well-being. 
        06. Awareness:  Provide accurate and up-to-date information about various mental health topics.  
        07. Crisis Support:  If a user expresses thoughts of self-harm or indicates they are in a crisis, provide them with appropriate hotline numbers and urge them to seek immediate professional help.

        Rules to Remember: 
        01. You are not a replacement for a mental health professional.
        02. Remove your name infront of the responses

        **Keep track of the conversation history to provide personalized and relevant responses.** 
        **Conversation History:**
        {self.get_conversation_history()}  # Function to retrieve conversation history (optional)

        Respond to: {user_input}
        """

        response = model.generate_content(prompt)
        self.conversation_history.append(f"You: {user_input}\nElla: {response.text}")

        # self.conversation_history.append(f"Ella: {response.text}")

        
        #Converting text to speech 
        speech = gTTS(text=response.text, lang='en', slow= False)  # Change 'en' for other languages
        speech.save("static/ella_response.mp3")

        print(response.text)
        return response.text
    
# generator = Generator() 

# # Start the conversation loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "quit":
#         break
#     generator.gemini_process(user_input)

        