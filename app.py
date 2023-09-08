```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import api
import data_storage
import caching
import inference

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file_id = data_storage.save_file(file)
        occupancy = inference.predict(file)
        caching.save(file_id, occupancy)
        return jsonify({'file_id': file_id, 'occupancy': occupancy}), 200
    else:
        return jsonify({'error': 'No file provided'}), 400

@app.route('/occupancy/<id>', methods=['GET'])
def get_occupancy(id):
    occupancy = caching.get(id)
    if occupancy is None:
        occupancy = inference.predict(data_storage.get_file(id))
        caching.save(id, occupancy)
    return jsonify({'occupancy': occupancy}), 200

@app.route('/api-key', methods=['GET'])
def get_api_key():
    return jsonify({'api_key': api.generate_key()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
