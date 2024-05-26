from flask import Flask, render_template, request
from process import Generator

app = Flask(__name__)
generator = Generator()

# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "GET":
#         return render_template("home.html")  # Render the form template
#     else:
#         user_input = request.form["user_input"]
#         print(user_input)
#         process_output = generator.gemini_process(user_input)
#         return render_template("home.html", user_input=user_input, process_output=process_output)  # Pass data to template
#         # return f"You entered: {user_input}"  # Example response
        
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    user_input = request.form["user_input"]
    response_text = generator.gemini_process(user_input)
    return render_template("index.html", user_input=user_input, response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
