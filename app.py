from flask import Flask, render_template, request, jsonify
from process import Generator

app = Flask(__name__)
generator = Generator()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    user_input_data = request.get_json()
    if user_input_data is None:
        return "Error: No JSON data found in request", 400
    
    user_input = user_input_data.get("user_input")

    if user_input is None:
        return "Error: No user input found in JSON request", 400
    
    response_text = generator.gemini_process(user_input)
    
    #JSON response
    response_data = {
        "text": response_text,
        "audio_file": "static/ella_response.mp3"
    }
    
    return jsonify(response_data)




if __name__ == "__main__":
    app.run(debug=True)
