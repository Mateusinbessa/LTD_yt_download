from flask import Flask, request, jsonify
from functions import download_audio, download_video
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['TIMEOUT'] = 60
app.config['SERVER_TIMEOUT'] = 60

@app.route('/audio', methods=['POST'])
def baixar_audio():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'status': 'error', 'message': 'URL não fornecida'}), 400

    res = download_audio(url=url, path='audios')
    return jsonify(res)

@app.route('/video', methods=['POST'])
def baixar_video():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'status': 'error', 'message': 'URL não fornecida'}), 400

    res = download_video(url=url, path='videos')
    return jsonify(res)

if __name__ == "__main__":
    app.run()
