import google.generativeai as genai
import os
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


class Generator:

    def gemini_process(user_input):
        generation_config = {
            
            "temperature": 0.9,
            "top_k": 1,
            "top_p": 1,
            "max_output_tokens":2048
            
        }
        model = genai.GenerativeModel("gemini-pro", generation_config = generation_config)
        response = model.generate_content([user_input])

        # response = model.generate_content(["Create a study schedule for the whole day."])

        print(response.text)
        
        return response.text

