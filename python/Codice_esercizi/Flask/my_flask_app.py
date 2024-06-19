from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    return jsonify({"message": data.get("message", "No message sent")})

if __name__ == '__main__':
    app.run(debug=True)
