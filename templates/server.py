from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    # Collect the input from the user
    character = request.form.get('character')
    activity = request.form.get('activity')
    food_brand_name = request.form.get('food_brand_name')
    gender = request.form.get('gender')

    # Run your existing pet name generator logic here
    pet_name = f"{character}_{activity}_{food_brand_name}_{'M' if gender.lower() == 'm' else 'F'}"
    return jsonify({"pet_name": pet_name})  # Return the pet name as a JSON object

if __name__ == '__main__':
    app.run(debug=True)
