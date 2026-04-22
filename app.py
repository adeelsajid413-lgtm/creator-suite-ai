from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # Allows HTML to talk to this Python script

@app.route('/check-username', methods=['GET'])
def check_username():
    username = request.args.get('username')
    
    # Common social media platforms
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/"
    }
    
    results = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for platform, url in platforms.items():
        try:
            # We check if the profile exists (200) or not (404)
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 404:
                results[platform] = "Available"
            elif response.status_code == 200:
                results[platform] = "Taken"
            else:
                results[platform] = "Unknown"
        except:
            results[platform] = "Error"
            
    return jsonify(results)

if __name__ == '__main__':
    # Running locally on port 5000
    app.run(debug=True, port=5000)