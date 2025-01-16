app = Flask(__name__)

@app.route('/')
def home():
    return render_template('template.html')  # Ensure template.html is in a 'templates' folder

@app.route('/generate', methods=['POST'])
def generate():
    character = request.form.get('character')
    activity = request.form.get('activity')
    food_brand_name = request.form.get('food_brand_name')
    gender = request.form.get('gender')

    pet_name = f"{character}_{activity}_{food_brand_name}_{'M' if gender.lower() == 'm' else 'F'}"
    return jsonify({"pet_name": pet_name})

if __name__ == '__main__':
    app.run(debug=True)
