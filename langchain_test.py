from langchain.llms import ChatGoogleGenerativeAI
from langchain.llms import ConversationBufferMemory
from langchain.llms import Prompt

# Initialize LangChain components with your Gemini API key (replace with yours)
memory = ConversationBufferMemory()
llm = ChatGoogleGenerativeAI(api_key = os.getenv("GOOGLE_API_KEY"))
# genai.configure()

def handle_user_input(user_input):
  """Processes user input and generates response using LangChain."""

  chain = llm.chain(
      # Stage 1: Pre-process user input (example)
      lambda x: x.lower(),

      # Stage 2: Retrieve conversation history
      memory.load_memory_variables,

      # Stage 3: Craft prompt for Gemini API
      lambda prompt_vars: Prompt(
          text=f"""
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
        {prompt_vars['conversation_history']}. Respond to: {user_input}
        
          """,
          style="supportive"  # Optional: Specify desired response style
      ),

      # Stage 4: Call Gemini API
      llm,

      # Stage 5: Optional post-processing (example)
      lambda response: f"Ella: {response.capitalize()}",

      # Stage 6: Store user input and response in memory
      memory.store_memory_variables(user_input=user_input, response=response)
  )

  response = chain.run()
  return response

# Example usage
user_input = "I'm having trouble managing my anxiety."
response = handle_user_input(user_input)

print(response)
