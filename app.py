from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "MAP Detector is live!"

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    website_url = data.get('url', '')

    # Fake MAP logic
    if "pattern" in website_url:
        return jsonify({
            "url": website_url,
            "map": "Klaviyo",
            "evidence": "X-Klaviyo: found",
            "status": "success"
        })
    else:
        return jsonify({
            "url": website_url,
            "map": "Unknown",
            "evidence": "No recognizable headers",
            "status": "success"
        })

if __name__ == '__main__':
    print("🟢 Flask is starting...")
    app.run(host='0.0.0.0', port=10000)

    # test_app.py 