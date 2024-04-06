from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Read the Excel file into a pandas DataFrame
df = pd.read_csv(r"C:\Users\mbvar\Desktop\Folder\foldercs\news website\New folder\static\excel\simout_data.csv")

# Route to serve the frontend HTML file
@app.route('/')
def index():
    return render_template('visualization.html')

# Define an API endpoint to return the data as JSON
@app.route('/data')
def get_data():
    data = df.to_json(orient='records')
    return data

if __name__ == '__main__':
    app.run(debug=True)
