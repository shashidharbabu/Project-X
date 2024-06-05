from flask import Flask, render_template, request, jsonify
from process import Generator
from maps import Maps
import json

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

@app.route("/therapists")
def search():
    return render_template("maps.html")
    
    
@app.route('/therapist_search', methods=['GET', 'POST'])
def find_therapists():
  # Extract user location from request data
    user_location = request.form.get('location')
    specialties = request.form.get('specialties')

    print(user_location)
    # Call Google Maps API Text Search function (implementation details not shown here)
    raw_therapist_results = Maps.google_maps_query(user_location, specialties)
    print("#####################")

    print(raw_therapist_results)

    print("#####################")
    # raw_data = json.loads(raw_therapist_results)
    # names = [result['name'] for result in raw_therapist_results['results']]
    therapists = []
    
    for therapist in raw_therapist_results['results']:
        name = therapist['name']
        formatted_address = therapist['formatted_address']
        # open_now_text = "Yes" if therapist['opening_hours'].get('open_now', False) else "No"  # Ternary operator for open_now
        rating = therapist['rating']

        # Print therapist details in a formatted way
        print(f"Name: {name}")
        print(f"Address: {formatted_address}")
        # print(f"Open Now: {open_now_text}")  # Print "Yes" or "No"
        print(f"Rating: {rating}")
        print("-" * 30)  # Separator between therapists

        therapist_data = {
            'name': name,
            'address': formatted_address,
            # 'open_now': open_now_text,
            'rating': rating
        }
        therapists.append(therapist_data)
            
    # return jsonify(final_therapist_results)
    return jsonify(therapists)

if __name__ == "__main__":
    app.run(debug=True)
