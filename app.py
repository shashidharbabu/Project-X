from flask import Flask, render_template, request
from process import Generator
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")  # Render the form template
    else:
        user_input = request.form["user_input"]
        print(user_input)
        process_output = Generator.gemini_process(user_input)
        return render_template("home.html", user_input=user_input, process_output=process_output)  # Pass data to template
        # return f"You entered: {user_input}"  # Example response

if __name__ == "__main__":
    app.run(debug=True)
