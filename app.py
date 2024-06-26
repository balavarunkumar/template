from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Read the Excel file into a pandas DataFrame
df = pd.read_csv('simout_data.csv')

# Route to serve the frontend HTML file
@app.route('/')
def index():
    return render_template('visualization.html')

# Define an API endpoint to return the data as JSON
@app.route('/data')
def get_data():
    # Convert DataFrame to JSON string
    data = df.to_json(orient='records')
    # Return JSON data
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
